# Sports Catalog - Project \#5

## What is this?
This is the Item Category project from the [Udacity's Full Stack Nanodgree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004). A user can register and login with their Google and Facebook account. Registered users can create new catalogs and items.

## Virtual box and vagrant
You will need to have virtual box and vagrant to run the necessary commands to view the contents of this repository. Luckily, the Udacity team has a guide [right here for you](https://www.udacity.com/wiki/ud197/install-vagrant). You do not need an account to view that page.

## Getting started
If you have virual box and vagrant installed, installation is as simple as cloning the repository, then doing the following commands in your favorite terminal:
```
vagrant up
```
The `vagrant up` command will setup your vagrant environment. Check out pg_config.sh to see what will be installed for you. Next:

```
vagrant ssh
```
`vagrant ssh` will log you in to your virtual machine within your terminal.

When you're logged in, type `cd /vagrant` to get into the main directory where you can then do `python main.py` to start the server. 
From there, go to localhost:8080 in your browser to view the content. 

## Database Seed
The first time you start the server, a file called itemcatalog.db will be generated to put a few catalogs in the database so you have something to look at from the very start.

You can see in detail what is put into the database by taking a look at the project/db/database_seed.py file.

## JSON Endpoints
This project includes a few JSON Endpoints. You can take a look at them by visiting the urls present in the project/handlers/json_endpoints.py module. Note that the category id and item id must be valid in order to view the JSON data.

## Cross-site Request Forgery
To read about Cross-Site Request Forgery, CSRF for short, please take a look [here](https://www.owasp.org/index.php/Cross-Site_Request_Forgery_(CSRF)).

This application uses [Flask-SeaSurf](https://flask-seasurf.readthedocs.io/en/latest/), which is automatically installed for you when you run `vagrant up`.

## File Structure
Instead of putting all view files into one module, I separated them all into the handlers directory.
Below is a brief description of the files and modules. I did not include a description for the individual modules in each project directory.
```
├── client_secrets.json   #Put your Google secrets here
├── fb_client_secrets.json   #Put your FB secrets here
├── itemcatalog.db   #Auto generated on initial run of python main.py
├── main.py  #The main module that starts everything up
├── pg_config.sh   #Needed to configure your VM
├── project
│   ├── db #Database-related modules here
│   ├── handlers   #View modules here, including a separate module for decorators
│   ├── static   #CSS, Javascript, images
│   ├── templates   #HTML files
│   └── utils   #Helper files here
├── README.md
└── Vagrantfile   #Needed to get your VM up and running
```
