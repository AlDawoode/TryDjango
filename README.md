

$ 
 ## **You can ignore SSL errors by setting pypi.org and files.pythonhosted.org as trusted hosts. 
 for Win7:**
``` 
 --------------------------
 pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org <package_name>
--------------------------
 
## **Create Django project after you have local env :**
```
pip install django
django-admin startproject sampleapp
```
 
--------------------------
--------------------------
  
## **Create local env + Add a requirements file that include Necessary Dependency for django project  :**
```
Create a virtual environment $ python3 -m venv /path/to/new/virtual/env
Install packages using $pip install <package> command
Save all the packages in the file with $pip freeze > requirements.txt. Keep in mind that in this case, requirements.txt file will list all packages that have been installed in virtual environment, regardless of where they came from

Install project dependencies
When if you’re going to share the project with the rest of the world you will need to install dependencies by running $pip install -r requirements.txt
```
--------------------------
--------------------------
 
## **Create local env :**
```
virtualenv -p python3 .
```
--------------------------
--------------------------

## **Run the local env :**

```
source bin/activate
```
--------------------------
--------------------------
## **Run django migrate :**

```
python manage.py migrate
```
--------------------------
--------------------------
## **Run django server :**
```
python manage.py runserver
```
--------------------------
--------------------------
## **Create User for Admin dashboard :**
```
python manage.py createsuperuser
```
--------------------------
--------------------------
## **Create app inside django project :**
```
python manage.py startapp AppName
```
--------------------------
--------------------------
## **made some changes {example : when create new model class }**
```
 python manage.py makemigrations
 python manage.py migrate 
```
--------------------------
--------------------------
## **python shell :**
```
 python manage.py shell
```
## **We can for example import models from shell:**
```
# from products.models import Product
# Product.objects.all()
```
## **If you want to create new products objects you can write:**
```
Product.objects.create(title="new product" , descirption = "another one " ...... )
```
--------------------------
--------------------------
