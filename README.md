# JournalMyLife

An personal journal app, made for keeping track of all your daily activities, planning and thoughts.

## Getting Started

git clone

### Prerequisites

Python 3 with the modules: Flask and...
```
Give examples
```

### Installing

```
1. (optional)Set up MySQL|Not needed, can use an locale sqlite3.db in working folder.
1a. python -m venv venv | For runing it in an virtual environment.
2. pip install -r requirements.txt  | OR use pipreqs
3. source venv/bin/activate OR source venv/Scripts/activate OR  .\venv\Scripts\Activate.ps1

python.exe -m pip install --upgrade pip

```
pip install flask-sqlalchemy
pip install --only-binary :all: mysqlclient
pip install flask-login
pip install flask-migrate
pip install Flask-WTF
pip install flask-bootstrap

pip install pipreqs
pipreqs ./ --encoding=utf-8

pip install coverage
pip install Flask-Script

### Broken ###

since flask 2.0.0 and Flask-Script kinda broke this project, DONT USE, not working atm, use flask 1.1.2, if trying to run this project!
manage.py <- y'll get ModuleNotFoundError: No module named 'flask._compat'
[](https://stackoverflow.com/questions/67538056/flask-script-from-flask-compat-import-text-type-modulenotfounderror-no-module)


## Running the tests

python test_journalmylife.py

## Deployment


## Built With

* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - The web framework used
* [pip](https://pypi.org/)  - Dependency Management

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/thomasskokholm/ inset link) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Thomas S. Kokholm** - *Initial work* - [ThomasSKokholm](https://github.com/ThomasSKokholm)

See also the list of [contributors](https://github.com/ThomasSKokholm/journalmylife/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* 1
* 2
* 3

