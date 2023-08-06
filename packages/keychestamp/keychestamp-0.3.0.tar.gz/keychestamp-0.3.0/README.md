# keychestamp - KeyChest ACMEv2 Proxy

When you start using Let's Encrypt in scale, early detection of of incidents and misconfigurations is paramount. Failure
 to do so may result in hitting rate-limits preventing new certificate requests or even expiry and down-times of your services.

KeychestAmp is an HTTPS proxy that logs activity of ACMEv2 clients when interacting with issuers. (Let's Encrypt being the
main ACMEv2 certificate issuer). The purpose is to provide a single source of data
 to manage use, and detect failures and malfunctioning of ACMEv2 clients.
 
KeychestAmp is a pass-through, MITM proxy. It will not change the messages as they are digitally signed by clients.
 It only does necessary changes to HTTP headers. Our closed-source proxy [**AmpX**](https://keychest.net/stories/lets-encrypt-for-companies-with-keychest) can work as a deep-proxy, where 
 it uses its own ACMEv2 account. This allows it to centralize validation of orders (i.e., certificate requests).

![High-level Keychest Amp proxy](doc/amp_keychest_highlevel.png)

## Just Do It

You can use the following three commands to quickly test it. The example uses certbot against the staging environment.

```shell script
pip install keychestamp
nohup keychestamp --noapi -l debug 1>/tmp/debug.log 2>&1 &
(curl -x "http://127.0.0.1:8443/" -s -k http://amp.keychest.net > /tmp/ca.crt; \
 export HTTPS_PROXY="https://127.0.0.1:8443"; \
 export REQUESTS_CA_BUNDLE=/tmp/ca.crt; \
 certbot renew --dry-run --force-renewal)
```

## Summary

Two big issues of using Let's Encrypt are client failures and rate-limits of Let's Encrypt.
Undetected failures of local clients can happen as a result of server updates, software bugs, or changes in the issuance
ecosystem. The rate-limits can be easily hit by a configuration error in a single
Let's Encrypt client, or with the growth of the Let's Encrypt use.

**keychestamp** is a man-in-the-middle (MITM) proxy that extracts operationally important
data from ACMEv2 requests. The data can be:
 
  - sent via a RESTful API to a monitoring service KeyChest, or
  - log locally into text files as JSON messages.
  
The two options are independent. The former gives access to real-time notifications and online reports, the latter
allows you use the proxy without any external dependencies.


The proxy creates its own "root certificate" that is used to create
local HTTPS connections between itself and ACMEv2 clients.

## Dependencies

**keychestamp** contains all necessary processing code but it depends on its
environment and a correct integration.

## Install

### Install the application

`pip install keychestamp`

or 

`pip install --upgrade --no-cache-dir keychestamp`

It needs read-write access to `/var/log/keychestamp` folder to store local logs, and
optionally read-access to `/etc/keychestamp` for its configuration.

The folders above can be prefixed with a command line switch `env`.

### Usage

The best place to start is https://gitlab.com/keychest/keychestamp for the most up to date
information. However, it's always good to see main options in one place, so here it is:

 - -h, --help - this help, if present it will stop the process
 - -l, --level <DEBUG|ERROR|WARNING|INFO|CRITICAL> - minimum level to log, default is INFO
 - -n, --noapi - disables API logging, starts logging into /var/log/keychestamp/audit.json
 - -f --file <file> - enable local login and set a custom location
 - -p, --port <int> - setting the listening port of the proxy
 - -a, --addr <IP addr> - by default it responds to all requests
 - -e, --etc <folder> - working directory for storing config. data
 - -c, --ca - just returns its root certificate in PEM format and exits

Unless you include one of the '-h', '--help', '-c', '--ca', keychestamp will run continuously until
terminated.

### Install supervisor for automatic restarts

```
[program:keychestamp]
directory=/tmp
command=keychestamp -f /var/log/keychestamp/audit.json
user=root
autostart=true
autorestart=true
stderr_logfile=/var/log/keychestamp/error.log
stdout_logfile=/var/log/keychestamp/messages.log
```

You can adjust parameters as required.

Restart the supervisor:

`systemctl restart supervisord`

`supervisorctl` - is a client, which shows status of processes - it has commands like:
 - start <name>
 - stop <name>
 - restart <name>
 - reread  # reads configuration files and shows changes
 - reload  # loads the new configuration to use for future commands
 

# Log Messages

All messages are in JSON format so they can be efficiently analyzed and visualized in any modern
log processing system.

Messages have a uniform structure with the variability hidden inside its "params" attribute.

```json
{
    "msg": "string: type of the log entry",
    "params": {"object": "type-specific attributes"}, 
    "time": "datetime: time of the event",
    "proxy": "id of the proxy - email @amp.keychest.net",

    "id": "<int: order ID of the log entry>",
    "host": "string: proxy hostname",
    "ip": "string: proxy IP address>",
    "version": "string: the proxy version",
    "backlog": "<int: number of logs in the proxy queue>",
    "log_time": "datetime: time of logging"
}
```

Example:
```json
{
    "msg": "new-acct", 
    "params": {"object": "see definitions below"}, 
    "time": "2019-12-11 08:40:37", 
    "proxy":"i0lxcglxufdwnplehph0kqfp@amp.keychest.net",

    "id": 20, 
    "host": "MacBook2018.local", 
    "ip": "127.0.0.1", 
    "version": "0.2.2", 
    "backlog": 0, 
    "log_time": "2019-12-11 08:40:39"
}
```

As you can see, the items can be split into 2 groups:

 - audit data - actual information collected by a given proxy
 - log management - supporting management of logs when collecting from multiple sources

The values of "msg" are currently:

 - directory
 - new-acct
 - new-nonce
 - new-order
 - revoke-cert
 - key-change
 - auth
 - final
 - chall
 - order

The following sections show the structure of **params** for each of the types.

## directory

An initial message providing ACMEv2 clients with endpoints for all main protocol messages.

```json
"params": {
    "epoch": "<int: epoch time>",
    "client": "client address as identified in ",
    "server": "URL of the ACMEv2 server",
    "agent":  "agent information from HTTP headers",
    "code": "<int: http code>"
}
```

Example:
```json
"params": {
    "epoch": 1575978565,
    "client": "192.168.1.21",
    "server": "acme-staging-v02.api.letsencrypt.org",
    "agent": "CertbotACMEClient/0.33.1 (certbot; darwin 10.15.1) Authenticator/webroot Installer/None (certonly; flags: ) Py/3.7.3",
    "code": 200
}
```

## new-nonce

ACMEv2 servers check that each message contains a unique nonce that must not be re-used. This message requests
the first nonce from a server. New nonces are included in every response from ACMEv2 servers.

```json
"params": {
    "epoch": "<int: epoch time>",
    "client": "client address as identified in ",
    "server": "URL of the ACMEv2 server",
    "agent":  "agent information from HTTP headers",
    "code": "<int: HTTP response code>"
}
```

Example:
```json
"params": {
    "epoch": 1575978568,
    "client": "192.168.1.21",
    "server": "acme-staging-v02.api.letsencrypt.org",
    "agent": "CertbotACMEClient/0.33.1 (certbot; darwin 10.15.1) Authenticator/webroot Installer/None (certonly; flags: ) Py/3.7.3",
    "code": 200
}
```

## new-acct

A request to create a new account at the ACMEv2 server. The server will respond with
a URL of the new account ("kid"), which is linked to a public key provided by the client.

```json
"params": {
    "epoch": "<int: epoch time>",
    "client": "client address as identified in ",
    "server": "URL of the ACMEv2 server",
    "agent":  "agent information from HTTP headers",
    "contact": ["an array of contact information, it can be empty"],
    "email": "an extracted email from 'contact', if empty a default email will be used",
    "account": "path to the account",
    "source": "source IP address as logged by the ACME server",
    "code": "<int: HTTP response code>"
    "status": "valid"
}
```

The default email is defined for Enterprise users with their own URLs for collecting logs in the https://keychest.net 
service.

Example:
```json
"params": {
    "epoch": 1575978565,
    "client": "192.168.1.21",
    "server": "acme-staging-v02.api.letsencrypt.org",
    "agent": "CertbotACMEClient/0.33.1 (certbot; darwin 10.15.1) Authenticator/webroot Installer/None (certonly; flags: ) Py/3.7.3",
    "contact": ["mailto:test@keychest.net"],
    "email": "acme@keychest.net",
    "account": "/acme/acct/11760188",
    "source": "81.174.162.194",
    "status": "valid",
    "code": 201
}
```

## new-order

An initial message starting a certificate request - i.e., an order.

```json
"params": {
    "epoch": "<int: epoch time>",
    "client": "client address as identified in ",
    "server": "URL of the ACMEv2 server",
    "agent":  "agent information from HTTP headers",
    "domains": [ "array of objects, each consisting of 'type' and 'value'"], 
    "authz": [ "array of strings - authentications" ], 
    "finalize": "path to finalize an order, i.e., send CSR", 
    "account": "path to the account", 
    "code": "<int: HTTP response code>"
    "order": "path to the order"
}
```

Example:

```json
"params": {
    "epoch": 1575978566, 
    "client": "192.168.1.21", 
    "server": "acme-staging-v02.api.letsencrypt.org", 
    "agent": "CertbotACMEClient/0.33.1 (certbot; darwin 10.15.1) Authenticator/webroot Installer/None (certonly; flags: ) Py/3.7.3", 
    "domains": [{"type": "dns", "value": "lex.keychest.net"}], 
    "authz": ["/acme/authz-v3/26326044"], 
    "finalize": "/acme/finalize/11760188/65280010", 
    "account": "/acme/acct/11760188", 
    "order": "/acme/order/11760188/65280010",
    "code": 201
}
```

## auth

Each domain in the order has to be validated. A successful validation turns the status
of the relevant authentication (authz) from 'pending' to 'valid'. This message tests the status of ta particular
 validation.

This allows to "split" processing, where the validation can be done offline via DNS changes.

```json
"params": {
    "epoch": "<int: epoch time>",
    "client": "client address as identified in ",
    "server": "URL of the ACMEv2 server",
    "agent":  "agent information from HTTP headers",
    "account": "path to the account", 
    "authz": "path to this particular authz",
    "status": "the status of the authz",
    "expires": "date time of the expiry",
    "code": "<int: HTTP response code>"
    "identifier": { an object representing the domain for which this authz was created }
}
```

Example:
```json
"params": {
    "epoch": 1575978566, 
    "client": "129.168.1.21", 
    "server": "acme-staging-v02.api.letsencrypt.org", 
    "agent": "CertbotACMEClient/0.33.1 (certbot; darwin 10.15.1) Authenticator/webroot Installer/None (certonly; flags: ) Py/3.7.3",
    "account": "/acme/acct/11760188",
    "authz": "/acme/authz-v3/26326044",
    "status": "pending",
    "expires": "2019-12-17T11:49:26Z",
    "identifier": {
        "type": "dns", "value": "lex.keychest.net"
    },
    "code": 200
}
```

As you can see, validations exipre in 7 days as the one above has been created
on December 10 and expires on December 17.

## chall

Each authorization can have several challenges. Successful validation of any of them will
change the status of the authorization to the 'valid' value. ... and failed validation will set the state as 'invalid'.

```json
"params": {
    "epoch": "<int: epoch time>",
    "client": "client address as identified in ",
    "server": "URL of the ACMEv2 server",
    "agent":  "agent information from HTTP headers",
    "account": "path to the account", 
    "chall": "path to this particular challenge",
    "status": "the status of the challenge",
    "code": "<int: HTTP response code>"
}
```

Example:
```json
"params": {
    "epoch": 1575978566, 
    "client": "129.168.1.21", 
    "server": "acme-staging-v02.api.letsencrypt.org", 
    "agent": "CertbotACMEClient/0.33.1 (certbot; darwin 10.15.1) Authenticator/webroot Installer/None (certonly; flags: ) Py/3.7.3",
    "account": "/acme/acct/11760188",
    "chall": "/acme/authz-v3/26326044/fwesDz",
    "status": "pending",
    "code": 200
}
```

## order

Clients can at any time check the status of an order. Once it is completed, it will show a link to download the new 
certificate.

```json
"params": {
    "epoch": "<int: epoch time>",
    "client": "client address as identified in ",
    "server": "URL of the ACMEv2 server",
    "agent":  "agent information from HTTP headers",
    "account": "path to the account", 
    "chall": "path to this particular challenge",
    "status": "the status of the challenge",
    "identifiers": [ "array of objects representing the domain for which this authz was created" ],
    "finalize": "path to finalize an order, i.e., send CSR", 
    "certificate": "path to download the cert or empty",
    "code": "<int: HTTP response code>"
}
```

Example:
```json
"params": {
    "epoch": 1575978566, 
    "client": "129.168.1.21", 
    "server": "acme-staging-v02.api.letsencrypt.org", 
    "agent": "CertbotACMEClient/0.33.1 (certbot; darwin 10.15.1) Authenticator/webroot Installer/None (certonly; flags: ) Py/3.7.3",
    "account": "/acme/acct/11760188",
    "chall": "/acme/authz-v3/26326044/fwesDz",
    "status": "pending",
    "identifiers": [
        {
            "type": "dns", "value": "lex.keychest.net"
        }
    ],
    "finalize": "/acme/finalize/11760188/65280010",
    "certificate": "",
    "code": 200
}
```

## final

Once the order is validated, it has to be finalized by sending a CSR to the ACMEv2 server.

```json
"params": {
    "epoch": "<int: epoch time>",
    "client": "client address as identified in ",
    "server": "URL of the ACMEv2 server",
    "agent":  "agent information from HTTP headers",
    "account": "path to the account", 
    "status": "the status of the challenge",
    "certificate": "path to download the cert or empty",
    "code": "<int: HTTP response code>"
}
```


Example:
```json
"params": {
    "epoch": 1575978566, 
    "client": "129.168.1.21", 
    "server": "acme-staging-v02.api.letsencrypt.org", 
    "agent": "CertbotACMEClient/0.33.1 (certbot; darwin 10.15.1) Authenticator/webroot Installer/None (certonly; flags: ) Py/3.7.3",
    "account": "/acme/acct/11760188",
    "status": "pending",
    "certificate": "",
    "code": 200
}
```

## revoke-cert

Certificate revocation - it can be done by the original account that created and completed an order or another account
with validations for the certificate domains.

We don't do any any parsing of the certificate that is being revoked.

```json
"params": {
    "epoch": "<int: epoch time>",
    "client": "client address as identified in ",
    "server": "URL of the ACMEv2 server",
    "agent":  "agent information from HTTP headers",
    "account": "path to the account",
    "code": "<int: HTTP response code>"
}
```


Example:
```json
"params": {
    "epoch": 1575978566, 
    "client": "129.168.1.21", 
    "server": "acme-staging-v02.api.letsencrypt.org", 
    "agent": "CertbotACMEClient/0.33.1 (certbot; darwin 10.15.1) Authenticator/webroot Installer/None (certonly; flags: ) Py/3.7.3",
    "account": "/acme/acct/11760188",
    "code": 200
}
```

## key-change

A helper method that allows changing the signing key for an account.

```json
"params": {
    "epoch": "<int: epoch time>",
    "client": "client address as identified in ",
    "server": "URL of the ACMEv2 server",
    "agent":  "agent information from HTTP headers",
    "account": "path to the account",
    "code": "<int: HTTP response code>"
}
```


Example:
```json
"params": {
    "epoch": 1575978566, 
    "client": "129.168.1.21", 
    "server": "acme-staging-v02.api.letsencrypt.org", 
    "agent": "CertbotACMEClient/0.33.1 (certbot; darwin 10.15.1) Authenticator/webroot Installer/None (certonly; flags: ) Py/3.7.3",
    "account": "/acme/acct/11760188",
    "code": 200
}
```


## Deep Proxy AmpX

The deep proxy is available as a service integrated with the [KeyChest cert management](https://keychest.net). 

![KeyChest AmpX High-level](doc/deep_proxy_keychest_le.png)

If you have any question about Amp or AmpX, you can reach us at support@keychest.net or +1-512-696-1552.