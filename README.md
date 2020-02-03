## django-rest-framework-library-management-system
Simple boilerplate for django & django rest framework

 
#### Jwt token endpoint
Method | Endpoint | Functionanlity
--- | --- | ---
POST | `/api-token-auth` | Request jwt token

#### User Endpoints

Method | Endpoint | Functionality
--- | --- | ---
GET | `/api/user` | List users
POST | `/api/user/create` | Creates a user
GET | `/api/user/profile/{pk}` | Retrieve a user
PUT | `/api/user/update/{pk}` | Edit a user
DELETE | `/api/user/delete/{pk}` | Delete a user
PUT | `/api/user/profile/{pk}/upload` | Upload Profile Image
POST | `/api/user/registration` | Register as Member
PUT | `/api/user/profile/update/{pk}` | Update Own Profile

#### Author Endpoints

Method | Endpoint | Functionality
--- | --- | ---
GET | `/api/author` | List Authors
POST | `/api/author/create` | Creates a author
GET | `/api/author/detail/{pk}` | Retrieve a author
PUT | `/api/author/update/{pk}` | Edit a author
DELETE | `/api/author/delete/{pk}` | Delete a author

#### Book Endpoints

Method | Endpoint | Functionality
--- | --- | ---
GET | `/api/book` | List Books
POST | `/api/book/create` | Creates a book
GET | `/api/book/detail/{pk}` | Retrieve a book
PUT | `/api/book/update/{pk}` | Edit a book
DELETE | `/api/book/delete/{pk}` | Delete a book
GET | `/api/book/filter/author/{pk}` | Retrieve books by author
GET | `/api/book/export/excel` | Export all author as excel file

#### Loan Endpoints

Method | Endpoint | Functionality
--- | --- | ---
GET | `/api/loan` | List Loans
POST | `/api/loan/create` | Creates a loan
GET | `/api/loan/detail/{pk}` | Retrieve a loan
PUT | `/api/loan/update/{pk}` | Edit a loan
DELETE | `/api/loan/delete/{pk}` | Delete a loan
PUT | `/api/loan/request_status/update/{pk}` | Update loan rquest status to either accepted or rejected
PUT | `/api/loan/status/{pk}` | Update loan status either to taken or returned
GET | `/api/loan/request` | Retrieve all loan requests of autheticated user

### Installation 
If you wish to run your own build, you two options
 1. User Docker compose.
    If you are running this application from linux remove `tty: true` from `docker-compose.yml` otherwise skip.
    
    `$ git clone https://github.com/pusku/rest_library_management_system`
    
    `$ cd django-rest-framework-boilerplate`    
    `$ docker-compose up`
    
     `$--ignore-installed switch`
 2. Without docker
 
First ensure you have python globally installed in your computer. If not, you can get python [here](python.org).

After doing this, confirm that you have installed virtualenv globally as well. If not, run this:

    $ pip install virtualenv
Then, Git clone this repo to your PC

    $ git clone https://github.com/pusku/rest_library_management_system
    $ cd django-rest-framework-boilerplate
Create a virtual environment

    $ virtualenv .venv && source .venv/bin/activate
Install dependancies

    $ pip install -r requirements.txt
Make migrations & migrate

    $ python manage.py makemigrations && python manage.py migrate
Create Super user
    
    $ python manage.py createsuperuser

### Launching the app
    $ python manage.py runserver

### Run Tests
    $ python manage.py test

