# Nginx & Httpd Template

## How to use
- RUN "npm run install:dependencies" - to install NPM dependencies
- RUN "npm run build:all" - to build projects assets and FE
- RUN "npm run watch:frontend" - to start watchers for FE developemnt
- RUN "npm run build:compose" - to start docker-compose instance
- RUN "npm run stop:compose" - to stop docker-compose instances

## How to bump
- PATCH - `npm version patch` - `2.0.${patch}`
- MINOR - `npm version minor` - `2.${minor}.0`
- MAJOR - `npm version major` - `${major}.0.0`

## Architecture Diagram
<img src="./wiki/architecture/architecture.png" width="100%"></img>

## Branching Strategy
<img src="./wiki/branching-strategy/branching-strategy.png" width="100%"></img>
