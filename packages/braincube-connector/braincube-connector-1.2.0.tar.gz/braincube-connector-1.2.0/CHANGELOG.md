# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.2.0]

It is now possible to specify in the config.json that you want to verify certificates or not when
speaking to the Braincube API.
Setting the `verify` config to `False` will ask python to accept any SSL certificate.

You can also pass a personalized certificate chain by setting `verify` to a path to a PEM file that contains 
the certificate chain:
`'verify':'/etc/ssl/certchain.pem'`
See the [Python Requests documentation](https://requests-fr.readthedocs.io/en/latest/user/advanced.html?highlight=verify#verifications-certificats-ssl) for details.


## [1.1.0] - 2019-08-08
### Added
- Changelog file
- The ability to specify a sub-domain to connect to 

## [1.0.4] - 2019-08-07
### Changed
- Improve performance when converting raw data to pandas dataframe
- Use logging to log properly

## [1.0.3] - 2019-08-06
### Fixed
- Fix Error in documentation

## [1.0.2] - 2019-08-05
- Fix static pages not installed by the package

## [1.0.1] - 2019-08-05

### Fixed
- Fix static pages not included in the package

## [1.0.0] - 2019-03-21

### Added
- First release