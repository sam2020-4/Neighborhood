## Neighborhood

### Description
##### This is an application where users can display log in to the system and see what is happening in your Neighborhood for others to see and know what ids happening to their area and therefore can contact healthcare and police contacts.
**** View [Live-Link](https://neighborhood001.herokuapp.com/)

### Author
matata samuel

### Requirements
##### These are the requirements you need to get the project running locally on your machine:
  - Text Editor e.g vscode or atom
  - Install python3+
  - Install and activate virtual
  - Setup Database
  - Install Django

### Installation Process
##### Download any text editor of your choice, either Sublime, Visual-Studio-Code or Atom.
##### Install your preferred version of python
  - ```sudo apt-get install python3.8```.
  - ```python --version``` to confirm that python has been installed.
##### Open the command-line and run the following command to open a directory:
  - ```cd your preferred directory``` => ```cd Desktop```
##### Git clone the project on your current directory by:
  - ```git clone https://github.com/sam2020-4/Neighborhood``.
##### Open the project on your terminal:
  - ```atom . or code .``` , according to the type of your text editor.
##### Move to your project directory:
  - ```cd Awwards```.
##### Install virtual environment using python:
  - ```python3.8 -m venv virtual```, check your project to confirm you have a folder called virtual,
  - then activate it by running ```source virtual/bin/activate```
##### To install the packages in the ```requirements.txt file```,
  - ```pip install -r requirements.txt```  That will install all packages including Django.
##### To open python shell:
  - ```python3.8``` ,
  - ```import django```
  - And lastly ```django.get_version()``` to see and confirm the version of django installed.
  - You can then ```ctrl z``` to get out of the shell,
##### After confirming you have all this
  - ```python3 manage.py runserver``` to run the project.
  - Then click the local host link given to open the project on a browser ```http://127.0.0.1:8000/```.


#### For more information read the following django and python documentation:
  - [DjangoDocumentation](https://docs.djangoproject.com/en/1.11/intro/install/)
  - [PythonDocumentation](https://www.python.org/doc/)


### User Stories
- As a user, I would like Sign in with the application to start using.
- As a user I would like to Set up a profile about me and a general location and my neighborhood name.
- As a user I would like to Find a list of different businesses in my neighborhood
- As a user I would like to Find Contact Information for the health department and Police authorities near my neighborhood.
- As a user I would like to Create Posts that will be visible to everyone in my neighborhood.
- As a user I would like to Change My neighborhood when I decide to move out.
- As a user I would like to Only view details of a single neighborhood.

### Technologies Used
- Python3
- Django rest-Framework
- PostgreSQL
- HTML5
- Bootstrap4

## Dependencies
- Postgresql

### Licence
[MIT](LICENSE)

### Contact
##### mattasamuel3@gmail.com
