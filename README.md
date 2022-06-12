## Awwards
This is an awwards clone

## Author
Pauline Wafula

## Description
Awwards is a web application that mimics a popular app , Awwards.This application allows a user to post a project they have created and get it reveiwed by the peers.

## User Stories
These are the behaviours/features that the application implements for use by a user.

As a user I would like to:

* View posted projects and their details
* Post a project to be rated/reviewed
* Rate/ review other users' projects
* Search for projects 
* View projects overall score
* View my profile page

## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display login form or sign up incase you dont have an account  | **On page load** | Displays the registration form on clicking sign up |
| Displays projects | **On clicking a 'search' button** | Displays project under the searched title |
| Displays a form to add a project | **Click add a project link** | add a new project with the image ,title,description,url,date and user |
| profile page | **On clicking profile** | takes you to the user profile|
|  logout | **On clicking logout** |logs out a user from the page|


## SetUp / Installation Requirements
### Prerequisites
* python3.8
* pip
* activate virtual environment
### Cloning
* In your terminal:


        $ git clone https://github.com/paulinenanzala19/Awwards.git
        $ cd awwards

## Running the Application
* Creating the virtual environment

        $ python3.8 -m venv --without-pip virtual
        $ source virtual/bin/activate
        $ curl https://bootstrap.pypa.io/get-pip.py | python

* Installing Django and other Modules

        $ python3.8  pip install django
        $ python3.8  pip install django-bootstrap3
        $ python3.8  pip install pillow
        $ python3.8  pip install django-registration
        $ python3.8  pip install django-crispy-forms

        

* To run the application, in your terminal:

        $ python3.8 manage.py runserver
       
   
## Testing the Application
To run the tests for the class files:

        $ python3.8 manage.py test theawwards
        

## Technologies Used
* Python3.8
* Django
* HTML
* CSS(Bootstrap)

## live link
['']

## known bugs
Not any that i am aware of but am open to suggestions
## License
MIT License

Copyright (c) 2022 Pauline Nanzala

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.