[](https://flask.palletsprojects.com/en/2.3.x/cli/)

 * Tip: There are .env or .flaskenv files present. Do "pip install python-dotenv" to use them.

'''
    $env:FLASK_APP = "app"
'''


[](https://flask.palletsprojects.com/en/2.3.x/appcontext/)


  File "C:\Users\thom520a\GitHub\JournalMyLife\2023\app.py", line 15, in <module>
    db.create_all()

RuntimeError: Working outside of application context.

This typically means that you attempted to use functionality that needed
the current application. To solve this, set up an application context
with app.app_context(). See the documentation for more information.

[](https://stackoverflow.com/questions/73961938/flask-sqlalchemy-db-create-all-raises-runtimeerror-working-outside-of-applicat)

    raise TypeError("Use the 'route' decorator to use the 'methods' argument.")
TypeError: Use the 'route' decorator to use the 'methods' argument.
