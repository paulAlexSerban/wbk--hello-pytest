# Reverse-proxy Web-server

[![Commitizen friendly](https://img.shields.io/badge/commitizen-friendly-brightgreen.svg)](http://commitizen.github.io/cz-cli/)
[![NodeJS](https://img.shields.io/badge/NodeJS-14.18.1-green.svg)](https://img.shields.io/badge/NodeJS-14.18.1-green)

## How to use

- RUN `npm run install:dependencies:dev` - to install NPM dependencies
- RUN `npm run build:all:dev` - to build projects assets and FE
- RUN `npm run watch:frontend` - to start watchers for FE developemnt
- RUN `npm run build:compose` - to start docker-compose instance
- RUN `npm run stop:compose` - to stop docker-compose instances

## Architecture Diagram

<img src="./wiki/architecture/architecture.png" width="50%"></img>

## Branching Strategy

<img src="./wiki/branching-strategy/branching-strategy.png" width="50%"></img>

## Tech-stack

- NodeJS
  - 14.18.1 (defined in .nvmrc and used in CI)
  - **WARNING** - if updated, both configs need to be changed
- Nginx
- Apache Httpd
- Docker & Docker-compose
