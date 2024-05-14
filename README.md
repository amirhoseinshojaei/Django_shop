# Django_Shop ✨

<img src="screenshots/django.gif" align="center">

* and E-commerce website using Python,Django,RestFramework,html,Css

# Features

* 🛒 Product Management : Ability to add, edit and delete products easily by store managers.
    Display full product details including pictures, prices and descriptions.


* 📦 Shopping cart system : Ability to add and remove & update quantity products from the shopping cart.
    Calculating the total purchase cost by considering the number and price of products.


* 💳 Secure Payment gateway : Connect to PayPal payment gateway for safe and secure transactions.
    Support online payments using credit cards and PayPal account.


* 📊 Sales Analytics: Gain valuable insights into your business's performance and make data-driven decisions.

----

# Getting Started

- Getting started with Django-Store is very easy. Follow the steps below to set up your e-commerce platform:

1. **Clone the Repository:** 

       git clone https://github.com/amirhoseinshojaei/Django_shop.git


2. **Navigate to the Project:**

        cd Django_shop


3. **Create and activate a VIRTUAL ENVIROMENT:**

        virtualenv venv

        source venv/bin/activate  

- on windows:

      venv\scripts\activate

4. **Install Required Dependencies:**

        pip install -r requirements.txt

5. **Apply Database Migrations:**

        python manage.py migrations

6. **Create a Super User:**

        python manage.py createsuperuser

7. **Start the Development System:**

       pyhton manage.py runserver

8. **Access the Admin Panle:**

* http://localhost:8000/admin

----

# API

**Get a list of products:**

- http://localhost:8000/rest_shop/products/

<img src="screenshots/Screenshot from 2024-05-14 02-54-36.png" align="center">
<img src="screenshots/Screenshot from 2024-05-14 02-54-46.png" align="center">


**Get a list of categories:**

- http://localhost:8000/rest_shop/category/


**Get a list of Cart:**

- http://localhost:8000/rest_cart/cart/

<img src="screenshots/Screenshot from 2024-05-14 02-55-06.png" align="center">

----

# Context Processors

        TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart', #add this 🖌️
            ],
        },
    },

----

# PayPal

<img src="screenshots/paypal.png" align="center">

----

# Panel Admin

<img src="screenshots/Screenshot from 2024-05-14 02-53-16.png" align="center">
<hr>
<img src="screenshots/Screenshot from 2024-05-14 02-53-27.png" align="center">
<hr>
<img src="screenshots/Screenshot from 2024-05-14 02-53-27.png" align="center">
<hr>

- Paypal IPns

<img src="screenshots/Screenshot from 2024-05-14 02-53-43.png" align="center">

----

# My Shop

- http://localhost8000/shop/products/

<img src="screenshots/Screenshot from 2024-05-14 02-25-30.png" align="center">

<hr>

- Detial Product

<img src="screenshots/Screenshot from 2024-05-14 02-25-48.png" align="center">

<hr>

- Book category 

<img src="screenshots/Screenshot from 2024-05-14 02-26-11.png" align="center">

<hr>

- http://localhost8000/cart/

<img src="screenshots/Screenshot from 2024-05-14 02-27-29.png" align="center">

<hr>

- http://localhost:8000/orders/create/

<img src="screenshots/Screenshot from 2024-05-14 02-27-48.png" align="center">

----

**Test Paypal:**

<img src="screenshots/testpaypal.png" align="center">

----

# HAPPY MOOD

**Be happy and Enjoy this project , And Always learning😎**

**You make me very happy by forking and committing to the project🤩**

----

# License

<a href="https://github.com/amirhoseinshojaei/Django_shop?tab=GPL-3.0-1-ov-file#GPL-3.0-1-ov-file">Click here</a>


