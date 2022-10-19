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