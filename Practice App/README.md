### To run the program: 

You can run the program on command line by following the steps provided below.

* Clone this directory into your local workspace and open ```Practice App``` folder.  
* Create a virtual environment named as ```env```.
```cmd
python -m venv env  
```
* Activate your virtual environment:
```cmd
env\Scripts\activate
```
* Install the necessary python packages listed in the ```requirements.txt```:
```cmd
pip install -r requirements.txt
```
* Run the Django application:
```cmd
python manage.py runserver
```
* You can test the application by using the website running on ```http://${host}:8000/```.


## Dockerization
* In order to dockerize our application one should perform the following steps:
   1) Download Docker. (You can download it from [here](https://www.docker.com/).) It may require you to download WSL 2, so just follow the instructions. If asked, download Ubuntu as linux distributor.
   2) Create a file named **Dockerfile** under the project folder and paste the code snippet below into the file:
    ```javascript
    FROM python:3.8-slim-buster

    WORKDIR /app

    COPY requirements.txt requirements.txt
    RUN pip3 install -r requirements.txt
    RUN apt-get update && apt-get -y install tk-dev

    COPY . .
    CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"] 
     ``` 
     * This file contains the code that is necessary to create our docker image. You can choose your python version as you wish. It better be at least 3.8 to avoid compatibility problems.
    
    3) Create a file named **.dockerignore** as we do not want our environment related files to be included. Add ``` */env ``` into the file. (Assuming that your virtual environment name is _env_. If not add that name in the format mentioned above. )
    4) Now we are going to build our docker image. Enter the following command in the terminal:
    ```javascript
    docker build --tag python-django .
    ```
    * python-django is the name of the image so you can name it however you want. 
    * Don't forget that images are immutable so in order to change it, you need to recreate it. I know that it is a quite large file but don't worry about recreating as necessary files are backed up in the cache.
    5) It is time to create our container. Enter the following command in the terminal to run your image inside a container. 
    ```javascript
    docker run --publish 8000:8000 python-django
    ```
    6) Open the Docker app you downloaded at first, click containers, move the cursor over the container you just created and click _open in browser_. Our application now works on linux as well.
    
### URL of the Application: http://54.209.217.195:8000/
