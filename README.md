
# Event Management API

**Implementation of Event Management system using Django and DRF**

## 💪Built with
![Static Badge](https://img.shields.io/badge/Django-1?style=flat&logo=Django&labelColor=0c4b33&color=187f58&link=https%3A%2F%2Fwww.djangoproject.com%2F)
![Static Badge](https://img.shields.io/badge/Python-1?style=flat&logo=Python&labelColor=ffd847&color=3776ab&link=https%3A%2F%2Fwww.python.org%2F)
![Static Badge](https://img.shields.io/badge/PostgreSQL-1?style=flat&logo=PostgreSQL&labelColor=ffffff&color=336791&link=https%3A%2F%2Fwww.postgresql.org%2F)
![Static Badge](https://img.shields.io/badge/Docker-1?style=flat&logo=Docker&labelColor=ffffff&color=1d63ed&link=https%3A%2F%2Fwww.docker.com%2F)
![Static Badge](https://img.shields.io/badge/Redis-1?style=flat&logo=Redis&labelColor=ffffff&color=161f31&link=https%3A%2F%2Fredis.io%2F)

## ✨Give it a try

*Expected to use **Bash** or similar shell alternatives*

<br>

clone repo >> generate .env >> edit it

```bash
git clone https://github.com/Kimoi/EventManagement-API.git && \
cd EventManagement-API && \
cp env_example .env && \
nano .env
```

<br>

- Let's spin up the container

```commandline
docker-compose up -d --build
```

- 3 containers should be running: web, db, redis

```commandline
docker ps
```

- Apply migrations

```commandline
docker-compose exec web python manage.py migrate
```

- Create superuser

```commandline
docker-compose exec web python manage.py createsuperuser
```

## ⚡Example endpoints:

>>/api/token/
> 
>POST. Provide user credentials to get token

>>/api/token/refresh/
>
>POST. Provide refresh token to get access token 

>>/api/
> 
>GET. Api Root

>>/api/events/
>
>GET. List events and their participants (organizations)
> 
>POST. Create event. Fields: title, description, date, image

>>/api/events/1
> 
>GET. Retrieve detail event information (with employees)

>>/create/organization/
>
>POST. Create organization. Fields: title, description, address, postcode

## ⚠️Stop and Erase

`docker-compose down -v`

`deactivate && cd .. && rm -fr EventManagement-API`
