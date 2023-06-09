#  #

python -m venv venv
.\venv\Scripts\activate.bat
pip install Flask Flask-SQLAlchemy

python.exe -m pip install --upgrade pip

* Tip: There are .env or .flaskenv files present.   pip install python-dotenv

## Linux ##
export FLASK_APP="app.py"
export FLASK_ENV="development"
## Windows/Powershell ##
$env:FLASK_APP = "app"
$env:FLASK_ENV = "development"

flask run

[I built the same app 3 times | Which Python Framework is best? Django vs Flask vs FastAPI](https://youtu.be/3vfum74ggHE?t=192)


### ###

[Stop Using ‘Pip Freezel’ For Your Python Projects | Built In](https://builtin.com/software-engineering-perspectives/pip-freeze)

pipreqs
UnicodeDecodeError: 'charmap' codec can't decode byte 0x8d in position 685: character maps to <undefined>

https://github.com/bndr/pipreqs/issues/371
pipreqs ./ --encoding=utf-8

