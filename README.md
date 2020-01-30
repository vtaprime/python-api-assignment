# python-api-assignment
This project have CRUD API example was build base on Django and Postgresql

# Deployment guildline
## Setup enviroment
OS: Ubuntu 18.04
### Install Postgresql
```shell
$ sudo apt update
$ sudo apt install postgresql postgresql-contrib
```
After that, you can set sup a new user role to access to your db(optional)

See full tutorial [here](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04)
### Install Python enviroment
Install Pyenv:
- Build dependencies
```shell
$ sudo apt-get install -y make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl
```
- Using the pyenv-installer, This will install pyenv along with a few plugins that are useful
```shell
$ curl https://pyenv.run | bash
```
At the end of the run, you should see something like this:
```shell
WARNING: seems you still have not added 'pyenv' to the load path.

# Load pyenv automatically by adding
# the following to ~/.bashrc:

export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```
- Install:
I choose python version is 3.6.8
```shell
$ pyenv install 3.6.8
```
- Create virtual enviroment
```shell
pyenv virtualenv <python_version> <environment_name>
```
Example: 
```shell
pyenv virtualenv 3.6.8 customer_manage_venv
```
- Finally, active it!
```shell
pyenv local customer_manage_env
```

### Install cache service
I choose memcached, because it has high performance and easy to setup!
- System setup:
```shell
sudo apt-get install memcached
```
- Start memcached, I use default setting
```shell
sudo service memcached start
```

### Run project
Easy to deploy project to Digital Ocean droplet, If you want to know more details, [here](https://www.digitalocean.com/docs/droplets/how-to/create/) is tutorial.

After python virtual enviroment is activated, access to project path
- Source tree:
```
python-api-assignment
    ├── README.md
    ├── customer_manage
    │   ├── customer_manage_api
    │   │   ├── __init__.py
    │   │   ├── settings.py
    │   │   ├── urls.py
    │   │   ├── views
    │   │   │   ├── __init__.py
    │   │   │   ├── customer_api.py
    │   │   │   └── form_schema.py
    │   │   └── wsgi.py
    │   ├── customer_manage_lib
    │   │   ├── __init__.py
    │   │   ├── config.py
    │   │   ├── constants.py
    │   │   ├── logger.py
    │   │   ├── manager
    │   │   │   ├── __init__.py
    │   │   │   ├── cache_manager.py
    │   │   │   ├── customer_manager.py
    │   │   │   └── models.py
    │   │   └── utils
    │   │       ├── __init__.py
    │   │       ├── process_request_utils.py
    │   │       └── utils.py
    │   └── manage.py
    ├── init_db.sh
    ├── query_youngest.sql
    └── requirements.txt
```

- Install python packages:
```shell 
pip install -r requirements.txt
```
- Create database, run file init_db.sh. For any reasons, it's not working, i will fixed later!
```shell
sh init_db.sh
```

- Run Django server:
Access to customer_manage dir, run this command.
```shell
python manage.py runserver 0.0.0.0:5001
```
The server will running on Port 5001 of OS

Now, everything almost done!

#### Noted:
- You need to update user info in file settings.py of django project to connect PostgreSQL like you create above.
- You can create user_token to call API by using JWT, in python:
```python
access_token = jwt.encode({'expiry_time': 1579686439}, 'customer_secret', algorithm='HS256')
```
with expiry_time value is UTC timestamp, see more about Python JWT [here](https://pyjwt.readthedocs.io/en/latest/)
#### Something need to do in the future
- Install Proxy server, uwsgi server to improve security and performance,.. 
- Using Falcon framework to create Rest API to improve performance. I use django for perform this task because for now I have not enough time to research about it.

#### Finally
- This [link](https://www.getpostman.com/collections/7bc18ba8475e0dcbf046) is postman collection to test project.
- Clone this project: (https://github.com/vtaprime/python-api-assignment.git)
