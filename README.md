# Macrostrat API V3

**Archived** This repository is no longer maintained. As of Jan 7, 2025, the Macrostrat API v3 is now
part of Macrostrat's [core monorepo](https://github.com/UW-Macrostrat/macrostrat/tree/main/services/api-v3).
The history of this repository was transferred up to commit [`f4fcd6bc`](https://github.com/UW-Macrostrat/api-v3/commit/f4fcd6bc888e6880eabd46aaca61045b261ce9cc). This API has tight coupling with the editing
functionality of the Macrostrat core, so keeping it together will minimize the need for coordinated code changes.

## Overview

This is a Fastapi application interfacing with a postgres database. It is designed to be deployed behind
Nginx on a kubernetes cluster.

## Development

.env

```shell
uri=postgresql://...

REDIRECT_URI=http://localhost:8000/security/callback

OAUTH_AUTHORIZATION_URL=https://cilogon.org/authorize
OAUTH_TOKEN_URL=https://cilogon.org/oauth2/token
OAUTH_USERINFO_URL=https://cilogon.org/oauth2/userinfo

OAUTH_CLIENT_ID=
OAUTH_CLIENT_SECRET=

SECRET_KEY=<AnyRandomHash>
JWT_ENCRYPTION_ALGORITHM=HS256

access_key=<S3_ACCESS_KEY>
secret_key=<S3_SECRET_KEY>

ENVIRONMENT=development # This turns off authentication when running locally
```

## Creating a token

Assuming you are running locally on localhost:8000

1. Login in to the api via [http://localhost:8000/security/login](http://localhost:8000/security/login)

2. Grab a security token via
   POST [http://localhost:8000/docs#/security/create_group_token_security_token_post](http://localhost:8000/docs#/security/create_group_token_security_token_post)

   Set the group_id to 1 ( admin group ) and the expiration to the future ( 1832530128 = 2028-01-26 )
