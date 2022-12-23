## Annotations Service
This service simply provides all the annotation-related APIs for our application. 

## Commands
1) You can use ```python manage.py shell``` to connect to the ORM and insert objects into database.
2) You can run the ```test.py``` using `python manage.py test .` from within the `annotations` folder.

## Dockerization
1) `Dockerfile` and `docker-compose.yml` files are already provided for you. You don't need to run the `Dockerfile` as `docker-compose.yml` already does it for you. Just run the following command:
```cmd
   docker-compose up -d --build
```