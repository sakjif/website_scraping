# WEB-parsing(scraping)

Script that parse some data from website

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

This project uses Python 3.9, PostgreSQL, Docker(docker-compose), Peewee(ORM)

### Installing

1. Clone repository

```
git clone https://github.com/sakjif/website_scraping
```

2. Create virtual environment

```
python3 -m venv venv (on Linux)
python -m venv venv (on Windows)
```

If it is not activated, activate it by running

```
source venv/bin/activate (on Linux)
venv\Scripts\activate (on Windows)
```
3. #### Don't forget about config variables in ```.env``` file:(DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_TABLE = data)


4. We are using Docker to run this app. All build instructions are in docker-compose, 
so we just need to run it

```
sudo docker-compose up
```

   
## Note

There are two kind of SQL implementation:
- The 1st one is using Peewee ORM (set by default). The source code is in ```pewee.py```
- The 2nd one is using native SQL syntax. The source code is in ```sql.py```
If you want to use the 2nd one just update ```command:  bash -c 'python sql.py``` in ```docker-compose.yml```

