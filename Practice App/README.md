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

* Other commands that will be useful in the future:
   * ```python manage.py test api/tests```: Run the tests within the ```api/tests``` folder.
   * ```python manage.py makemigrations```: Create new migrations based on the changes you have made to your models.
   * ```python manage.py sqlmigrate <app-name> <migration-number>```: Displays the SQL statements for a migration and executes them.
   * ```python manage.py migrate```: Apply the migrations.
   * ```python manage.py shell```: Open the Python shell that gives you access to the database API included with Django.
