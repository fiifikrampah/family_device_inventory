# Changelog

All notable changes to this project will be documented in this file.

The version of the initial release was in the format: `Major.Minor.Patch.Build`.
Version info for future releases will follow the Semantic Versioning
Style: `Major.Minor.Patch`

## [v1.0.0.0] (Pre-Release) - 2021-08-30

### New features

- Simple CRUD Flask app to allow a family to keep track of devices they own
  - Users can be added to Postgres DB
  - Devices can be added to/removed from Postgres DB
  - Device entry can be edited
- Docker support to allow user to quickly spin up project architecture inside a container
- User authentication with md5 hashing mechanism for securing user password
- Unit tests to allow for simple developmental testing before deployment
- Continuous Integration tests via CircleCI
- Support for deploying the app directly to Heroku as either a Heroku app or Container stack

### Fixes

- N/A

### Improvements

- N/A
