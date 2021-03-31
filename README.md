# IOT Project REST API
## Steps
1. Clone the repository.
2. Change directory to where the Dockerfile is.
3. Build the image using ```docker build -t web:latest .```.
4. Run the container using ```docker run -d --name django-heroku -e "PORT=8765" -e "DEBUG=1" -p 8007:8765 web:latest```.
5. Now Go to *localhost:8007*. You should be able to see the project up and runnig.
6. Stop the container using ```docker stop django-heroku```.
7. Remove the container using ```docker rm django-heroku```.

## Deploy to Heroku
1. Create a Heroku app using ```heroku create```.
2. Login to heroku CLI using ```sudo heroku login -i```.
3. Login to heroku container using ```sudo heroku container:login```.
4. Rebuild the docker image with the special tag for heroku registry using ```sudo docker build -t registry.heroku.com/<heroku-app-name>/web .```.
5. Push the image to the registry using ```docker push registry.heroku.com/<heroku-app-name>/web```.
6. Release the image ```heroku container:release -a <heroku-app-name> web```.
7. You will be able to see the app using ```heroku open -a <heroku-app-name>```.
8. Create a postgres addon on heroku using ```heroku addons:create heroku-postgresql:hobby-dev -a <heroku-app-name>```.
9. Once the database is up, run the migrations using
```heroku run python manage.py makemigrations -a <heroku-app-name>```

```heroku run python manage.py migrate -a <heroku-app-name>```.

10. You can check it using
```heroku pg:psql -a evening-tundra-50688```

In this way you will get an up and running RESTful API using django-rest-framework and Docker and it will be hosted on Heroku.

