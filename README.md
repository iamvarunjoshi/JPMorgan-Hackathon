# Urban Roots

## Team info

Find your .html file in the templates folder 

## Installation

#### Install required packages

Start by installing
```sh
sudo apt-get install libpq-dev python-dev
```

Then
```sh
pip install -r requirements.txt
```

#### Start the server (localhost:8080):
```sh
python main.py
```

### Update database:
```sh
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```

### Domain:
```sh
https://558e229b.ngrok.com
```