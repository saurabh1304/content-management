# Content Management

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/saurabh1304/content-management.git
$ cd content-management
```

Using `env.example` create a `.env` file with the appropriate config values.

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv venv
$ source venv/bin/activate
```

Then install the dependencies:

```sh
(venv)$ pip install -r requirements.txt
```

```sh
(venv)$ python manage.py runserver
```
