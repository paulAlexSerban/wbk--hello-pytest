# PBAnF Template - Nginx Reverse-proxy & Httpd Web-server

## Tech-stack

[![NodeJS](https://img.shields.io/badge/NodeJS-14.18.1-green)](https://nodejs.org/docs/latest-v14.x/api/)
[![Docker](https://img.shields.io/badge/Docker-20-blue)](https://docs.docker.com/release-notes/)
[![Nginx](https://img.shields.io/badge/Nginx-1.21.6-green)](https://www.nginx.com/)
[![Apache Httpd2](https://img.shields.io/badge/Apache%20Httpd-2.4.53-green)](https://httpd.apache.org/download.cgi#apache24)
[![Commitizen Friendly](https://img.shields.io/badge/commitizen-friendly-brightgreen.svg)](http://commitizen.github.io/cz-cli/)
[![Semantic Versioning](https://img.shields.io/badge/Semantic%20Versioning-2.0.0-green)](https://semver.org/spec/v2.0.0.html)

## How to use

- RUN - `npm run install:dependencies:dev` - to install NPM dependencies
- RUN - `npm run build:all:dev` - to build projects ./assets and ./frontend
- RUN - `npm run deploy` - deploy ./dist to ./docs
- RUN - `npm run watch:frontend` - to start watchers for ./frontend development
- RUN - `npm run build:compose` - to start docker-compose instance
- RUN - `npm run stop:compose` - to stop docker-compose instances
