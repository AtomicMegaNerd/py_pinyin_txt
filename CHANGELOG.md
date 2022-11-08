# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.2.0] - 2022-07-22

### Changed

- Updated to use Python 3.10.
- Use utf-8 encoding when calling open (fixes pylint warning).
- Update dependencies in Changelog.
- Remove setup.py and install inside Docker using pipenv.
- Use builder pattern for Docker to reduce image size.

## [1.1.4] - 2021-06-18

### Changed

- Use alpine based image to make it much smaller.

## [1.1.3] - 2020-06-18

### Changed

- Updated Dockerfile to no longer run as the program as root.

## [1.1.2] - 2020-05-20

### Changed

- Updated Dockerfile to use Python 3.9.5 based image.
- Updated the dev dependencies as well.

## [1.1.1] - 2020-05-09

### Changed

- Updated Dockerfile to use Python 3.9.1 based image.

## [1.1.0] - 2020-05-09

### Added

- Dockerfile in case you want to run this as a docker image.

## [1.0.1] - 2020-04-29

### Changed

- Updated pylint
- Fixed a few minor linting issues.

## [1.0.0] - 2020-04-26

### Added

- Initial release of PyPinyinTxt.
