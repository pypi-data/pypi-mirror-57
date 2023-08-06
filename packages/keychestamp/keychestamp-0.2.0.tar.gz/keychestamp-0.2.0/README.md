# keychestamp - KeyChest ACMEv2 Proxy

A simple proxy that logs activity of ACMEv2 clients (Let's Encrypt being the
main ACMEv2 certificate issuer). The purpose is to provide a single source of data
 to manage use, and detect failures and malfunctioning of ACMEv2 clients.

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


### Install supervisor for automatic restarts

tbd

```
[program:keychestamp]
directory=/tmp
command=keychestamp
user=root
autostart=true
autorestart=true
stderr_logfile=/var/log/keychestamp/error.log
stdout_logfile=/var/log/keychestamp/audit.log
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
 



