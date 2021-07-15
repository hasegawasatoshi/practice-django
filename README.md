# practice-django

## Usage

Configure `.env` file.
```
cp sample.env .env
```

| Key | Description |
|:----|:-|
| IP  | IP address of docker container. e.g. 127.0.0.1 |
| DJANGO_SUPERUSER_USERNAME | Django superuser's name |
| DJANGO_SUPERUSER_PASSWORD | Django superuser's passowrd |
| DJANGO_SUPERUSER_EMAIL    | Django superuser's email |
| POSTGRES_HOST             | Hostname of PostgreSQL |
| POSTGRES_DB               | Database table name |
| POSTGRES_USER             | PostgreSQL username | 
| POSTGRES_PASSWORD         | PostgreSQL password |

Start PostgreSQL
```
docker-compose up -d postgres
```

Build Django container image
```
docker-compose build django
```

DB migration
```
docker-compose run django python manage.py migrate
```

Create superuser
```
docker-compose run django python manage.py createsuperuser --noinput
```

Start Django
```
docker-compose up -d django
```

Stop Django and PostgreSQL
```
docker-compose down
```

Remove volume container for PostgreSQL if you want to initialize DB
```
$ docker volume ls
DRIVER    VOLUME NAME
local     practice-django_postgres-lib

$ docker volume rm practice-django_postgres-lib
```
