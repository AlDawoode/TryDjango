
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
