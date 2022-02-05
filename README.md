[![Build Status](https://travis-ci.org/misraX/glucose.svg?branch=main)](https://app.travis-ci.com/github/misraX/glucose)
[![codecov](https://codecov.io/gh/misraX/glucose/branch/master/graph/badge.svg)](https://codecov.io/gh/misraX/glucose)

Analyze user's levels from glucose devices.

### Key points

- API for listing, retrieving, creating user's glucose level.
- Pagination with limit offset pagination.
- Filtering and ordering.
- Docker and docker-compose for Nginx, uwsgi, MySQL.
- Code formatting with flake8 and pre-commit setup with black. 
- bash scripts to initiate the project, local development, and docker start.sh script with uwsgi to run behind Nginx as a reverse proxy.
- .travis build for testing.
- Swagger for API documentation.

### Prerequisite 

1. docker and docker-compose
2. virtualenv
3. python 3.8
6. Bash

### Installation

```
bash ./init.sh
docker-compose build
docker-compose up -d
```
The project is served on port 80, localhost.

### API

Levels API

- api/levels/        apps.level.api.views.UserGlucoseLevelModelViewSet       level-list

- api/levels/<pk>/   apps.level.api.views.UserGlucoseLevelModelViewSet       level-detail

API docs using drf_yasg

- api/swagger/       drf_yasg.views.view     schema-swagger-ui

Filters and ordering

- start, stop ex: http://localhost/levels/?user=1&start=2022-02-01&stop=2022-02-17
- Ordering is set to any field on the levels API

### Frontend

- /levels/
