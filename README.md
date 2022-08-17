# sv-dental

As regards steps to running the project by other users , this should work.

clone the project

```python
git clone https://github.com/TADB0902/sv-dental.git
```

create and start a a virtual environment

```python
virtualenv env --no-site-packages

source env/bin/activate

pip install -r requirements.txt
```
https://docs.python.org/3/library/venv.html#:~:text=A%20virtual%20environment%20is%20a,part%20of%20your%20operating%20system.

create a db and add the credentials to settings.py

then run
```python
python manage.py migrate
```
create admin account

```python
python manage.py createsuperuser
```
then
```python
python manage.py makemigrations
```
to makemigrations for the app

then again run
```python
python manage.py migrate
```
