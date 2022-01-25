# leaves-tracker-app
A backend application for tracking leaves of Squad-Stack employees.

# Steps to set up for local development

## Ubuntu
1. Install python

    update system
    - `sudo apt-get update`
    - `sudo apt-get upgrade -y`

    install python tools
    - `sudo apt-get install python3.8`
    - `sudo apt-get install -y python3-pip`
    - `sudo apt-get install -y python3.8-dev`
    - `sudo apt-get install -y build-essential`
    - `pip3 install virtualenv`

2. Install PostgreSQL using the following commands.
    - `sudo apt update`
    - `wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -`
    - `echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" |sudo tee  /etc/apt/sources.list.d/pgdg.list`
    - `sudo apt install postgresql-12 postgresql-client-12`
    - `systemctl start postgresql.service`

    - Run the following commands to create new user and database using postgres user of the system created at the time of installation
        - `sudo -i -u postgres`
        - `createuser --interactive myuser` will prompt for the user name if none is specified on the command line
        - `createdb leavestracker`
        - `exit`

    - Other way to create user and database in postgres using postgres shell (psql)
        - `sudo -u postgres psql`
        - `postgres=# create database leavestracker;`
        - `postgres=# create user myuser with encrypted password 'mypass';`
        - `postgres=# grant all privileges on database mydb to myuser;`


    When setting up the PSQL for development or testing make sure to note the name and
    password of the user created by the createuser command.You need to use this username and password
    in the `local.py` in folder `leavestracker/settings/local.py`


3. Install Rabbit MQ using the following commands.

    - `echo 'deb http://www.rabbitmq.com/debian/ testing main' | sudo tee /etc/apt/sources.list.d/rabbitmq.list`
    - `wget -O- https://www.rabbitmq.com/rabbitmq-release-signing-key.asc | sudo apt-key add -`
    - `sudo apt-get update`
    - `sudo apt-get install -y rabbitmq-server`
    - `sudo systemctl enable rabbitmq-server`
    - `sudo systemctl start rabbitmq-server`
    - `sudo rabbitmqctl add_user admin password`
    - `sudo rabbitmqctl set_user_tags admin administrator`
    - `sudo rabbitmqctl set_permissions -p / admin ".*" ".*" ".*"`

    check the status of rabbit-mq server

    - `sudo rabbitmqctl status`

4. Install Redis

    - `sudo apt install redis-server`
    - `sudo systemctl start redis`
    - `sudo systemctl enable redis`
    - Run this `sudo systemctl enable redis-server.service` if facing error in above command


    check whether the redis server is running or not

    - `redis-cli ping` should return PONG if the server is running


5. clone the project.

    - `git clone https://github.com/squadrun/leaves-tracker.git`

6. Create local settings file based on `local_example.py`

    - `cd leavestracker/settings`
    - `vi local.py`
    - `from .local_example import *`
    - Define `DATABASES` and `CACHES` variables and save

7. Set up a virtual env using `virtualenvwrapper` [https://bit.ly/3084M2p]

8. Switch to the virtual env and install dependencies from `requirements.txt`.

    - `pip3 install -r requirements.txt`
    - Run this if facing `psycopg` error - `sudo apt-get install libpq-dev`
    - Run this if facing issue with `pyjq` - `sudo apt-get install autoconf libtool`

9. Run migrations - `python manage.py migrate`

10. Run app using the command `python manage.py runserver`

11. Run celery using the command `celery --app=leavestracker worker --beat -Q -l INFO --without-heartbeat --without-gossip`

## MacBook

1. Make sure [Homebrew](https://brew.sh/) is installed.

2. Install `python`, `rabbitmq` and `postgresql` using homebrew. Also install `virtualenv`

    - `brew install python rabbitmq postgresql@12`
    - `pip3 install virtualenv`

3. Set up RabbitMQ (run with sudo if getting permission issues)

    - `rabbitmqctl add_user admin password`
    - `rabbitmqctl set_user_tags admin administrator`
    - `rabbitmqctl set_permissions -p / admin ".*" ".*" ".*"`

3. Set up PostgreSQL

    - `createuser --interactive`
    - `createdb leavestracker`
    - `exit`

4. Set up redis

    - `brew install redis`
    - `brew services start redis`

5. Follow steps 5-11 of Ubuntu setup

## Windows with WSL

1. Install WSL from this [link](https://docs.microsoft.com/en-us/windows/wsl/install)

2. Download Linux Distro from Microsoft Store (Ubuntu Recommended) [Ubuntu Link](https://www.microsoft.com/store/productId/9NBLGGH4MSV6)

3. For any local Storage use /mnt/<Prefered Windows Drive>/

4. Follow all the steps mentioned in Ubuntu setup.

### Note:
- To Run the application/Installation you have to use the Ubuntu CLI.

## Miscellaneous
1. For testing, you need to create a new db user with username and password as "postgres" as mentioned in test_settings.py . Also you need to use test_settings as your settings while running test cases

## Install Black and Flake8 pre-commit hook
1. Run pip install black flake8 pre-commit
2. Run pre-commit install
3. You can also integrate black with your IDE using https://github.com/psf/black/blob/master/docs/editor_integration.md

## ClickUp prepare-commit msg hook
Pre-script :- If you had already installed globally then you just need to run "git init" for this repo.

Else -
1. We use ClickUp for task tracking and ClickUp provides integration with GitHub.
2. Why should we use it? (CU == ClickUp)
    - It gives us the ability to see which commit was made for which CU task and hence backtracking for future purposes.
    - Anyone will be able to see what all commits were made in which CU task in CU.
    - Example commit it creates - https://github.com/squadrun/squadrun/commit/d65d1a212febe2e49e7420eb24756b01dbb65e62
    - How it is visible in CU - https://app.clickup.com/t/2hn81j
3. Now, how to enable this? Go through - https://github.com/tarungarg546/clickup-git-hook
4. It is recommended to setup globally if you'll be working across multiple repos.
5. Start committing/pushing code like a ninja! :D ;)

**PS: Only commit code while working on leavestracker virtualenv!**
