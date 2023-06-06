[](https://flask.palletsprojects.com/en/2.3.x/cli/)

 * Tip: There are .env or .flaskenv files present. Do "pip install python-dotenv" to use them.

'''
    $env:FLASK_APP = "app"
'''


[](https://flask.palletsprojects.com/en/2.3.x/appcontext/)

RuntimeError: Working outside of application context.

This typically means that you attempted to use functionality that needed
the current application. To solve this, set up an application context
with app.app_context(). See the documentation for more information.

