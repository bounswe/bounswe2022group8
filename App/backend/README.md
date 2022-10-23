## To run the backend: 

Our project layout is as follows. `backend` is the entire Django folder, while `backend/backend` stores the essential information such as `settings` for the Django app.
```
CmpE 451
│   .github
|   .gitignore
|   Project3-ACP.pdf
|   README.md
|   Deliverables
|   Practice App
└───App
|    │  mobile
|    |  frontend
|    └───backend
|    |    |
|    |    └─ api
|    |       backend
|    |       tests
|    |    env (create your own virtual environment)
|    |    requirements.txt
|    |    manage.py
|    |    README.md
|    |______________
|___________________
```
      

### Initials

* Clone this directory into your local workspace and open _App_ folder.
* Navigate to the `backend` folder within the _App_. 
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
* This way, you'll install everything necessary to run the application including `Django` and related `Rest Framework` modules.

### Run the Application

* Run the Django application:
   ```cmd
   python manage.py runserver
   ```
* You can test the application by using the website running on ```http://${host}:8000/```.

### Run tests
* Our tests will be located in the `tests` folder. Please keep in mind that the name of the files must comply with this format: `test*.py` for Django to locate it.
   ```cmd
   python manage.py test tests/
   ```
### Migrations
Migrations are Django’s way of propagating changes you make to your models (adding a field, deleting a model, etc.) into your database schema.

* When you new models to the project, first you have to create corresponding migrations:
   ```cmd
   python manage.py makemigrations
   ```
* This will create the necessary migrations. Then you have to apply these migrations with the following code.
   ```cmd
   python manage.py migrate
   ```

### Formatting
* It's a good practice format our code using a Python formatter to keep it more clean.
* We'll be using `autopep8` as formatter which complies with the [PEP 8](https://peps.python.org/pep-0008/) style guide. If you don't have this formatter already present in your working environment, you can install it using `pip`:
   ```cmd
   pip install --upgrade autopep8
   ```
* If you are working on Windows, you can format your code using `Ctrl` + `Shift` + `F`. If this combination doesn't work for you, it's either you don't have the formatter or it's not the correct shortcut for you. You can look at the shortcode from the search bar using `Ctrl` + `Shift` + `P`. Write "_Formatter_" in that search bar and look for the shortcut associated with "_Format Document_" 

### Django Superuser
* The Django admin application can use your models to automatically build a site area that you can use to create, view, update, and delete records. This can save you a lot of time during development, making it very easy to test your models and get a feel for whether you have the right data.
* To use the Django in admin mode, first you have to create a super user with the following command:
   ```cmd
   python manage.py createsuperuser
   ```
* After creating a super user, run the Django application.
* To login to the admin panel, open the /admin URL (e.g. http://127.0.0.1:8000/admin).


### Docker
`Dockerfile` and `docker-compose.yml` files are alread provided for you. Dockerizing our project is important for the deployment stage where we want our database to be stable and consistent between different runs for each use. To dockerize the application, use the following commands:
* First of all, you must install the Docker Desktop from [here](https://www.docker.com/). It may require you to download WSL 2, so just follow the instructions. If asked, download Ubuntu as linux distributor.
* I strongly suggest you to install the Docker extension for VS Code. It makes visualizing what's going on with the containers much more easier.
* Firstly, build the `Dockerfile`. Let's give it a name with the `--tag` flag:
   ```cmd
   docker build --tag python-django .
   ```
   If you don't give it a name, its name will be some random gibberish. As a result of the build, a container will be created. A container simply corresponds to a Linux environment where a copy of our application resides.
* Now, we should proceed with running our `docker-compose.yml` file. `docker-compose.yml` file helps us to define the services we want to run in our container. We have two services in our application: `web` and `db`. We also use `volume` to persist data even if service is interrupted (which is extremely important for production). You can both **build** and **run** the `docker-compose.yml` with the following command:
   ```cmd
   docker-compose up -d --build
   ```
   `-d` flag runs the services in detach mode so that they don't block the terminal. You can open their own terminal from the VS Code Docker extension. `--build` flag builds the project from scratch. It's important to use this flag if you make any changes on the code and want them to be reflected on your dockerized application.
* Open the shell of the web service and apply migrations:
   ```cmd
   python manage.py makemigrations --settings=backend.settings.production
   python manage.py migrate --settings=backend.settings.production
   ```
* When you are done with the container, run the following command to stop the services:
   ```cmd
   docker-compose stop
   ```
---
* Sometimes we may change the structure of our models (rather than just updating them) during the development. In such scenarios, we may end up having to re-create our database from scratch. It's easy to do in your local, but you have to follow several steps to do it for your Docker container.:
> Attention: Notice that this procedure will delete everything in your database. 
   * Firstly, make sure that your container is not working:
      ```cmd
      docker-compose down
      ```
   * List the volumes and make sure that Postgres database is there:
      ```cmd
      docker volume ls
      ```
   * Remove that specific volume. In my case, name of the volume is `backend_postgres_data`. If it's different for you, please adjust the following command accordingly.:
      ```cmd
      docker volume rm backend_postgres_data
      ```
   * Build the container:
      ```cmd
      docker-compose up -d --build
      ```
   * Go to the `web` container, attach a shell and run the following commands:
      ```
      python manage.py makemigrations --settings=backend.settings.production
      python manage.py migrate --settings=backend.settings.production
      ``` 
   * Now, your database should be up-to-date.
