# TODO or bugs 2 fiz ;-) #


ERROR: Could not find a version that satisfies the requirement pkg-resources==0.0.0 (from versions: none)
ERROR: No matching distribution found for pkg-resources==0.0.0
WARNING: You are using pip version 22.0.3; however, version 23.1.2 is available.
You should consider upgrading via the 'C:\Users\Tsk\AppData\Local\Programs\Python\Python310\python.exe -m pip install --upgrade pip' command.

[]()
[](https://stackoverflow.com/questions/40670602/could-not-find-a-version-that-satisfies-the-requirement-pkg-resources-0-0-0)
[](https://code-specialist.com/python/pkg-resources)

removed pkg-resources==0.0.0 from requirements.txt

INFO: pip is looking at multiple versions of flask to determine which version is compatible with other requirements. This could take a while.
ERROR: Cannot install -r requirements.txt (line 10) and Werkzeug==2.2.3 because these package versions have conflicting dependencies.

The conflict is caused by:
    The user requested Werkzeug==2.2.3
    flask 2.3.2 depends on Werkzeug>=2.3.3

To fix this you could try to:
1. loosen the range of package versions you've specified
2. remove package versions to allow pip attempt to solve the dependency conflict

ERROR: ResolutionImpossible: for help visit https://pip.pypa.io/en/latest/topics/dependency-resolution/#dealing-with-dependency-conflicts

ERROR: Cannot install -r requirements.txt (line 10) and Jinja2==2.11.3 because these package versions have conflicting dependencies.

The conflict is caused by:
    The user requested Jinja2==2.11.3
    flask 2.3.2 depends on Jinja2>=3.1.2

ERROR: Cannot install -r requirements.txt (line 10) and itsdangerous==1.1.0 because these package versions have conflicting dependencies.

The conflict is caused by:
    The user requested itsdangerous==1.1.0
    flask 2.3.2 depends on itsdangerous>=2.1.2

ERROR: Cannot install -r requirements.txt (line 10) and Click==7.0 because these package versions have conflicting dependencies.

The conflict is caused by:
    The user requested Click==7.0
    flask 2.3.2 depends on click>=8.1.3

The conflict is caused by:
    The user requested MarkupSafe==1.1.1
    jinja2 3.1.2 depends on MarkupSafe>=2.0

The conflict is caused by:
    The user requested MarkupSafe==2.0
    jinja2 3.1.2 depends on MarkupSafe>=2.0
    mako 1.2.2 depends on MarkupSafe>=0.9.2
    werkzeug 2.3.3 depends on MarkupSafe>=2.1.1

    The user requested MarkupSafe==2.0
    jinja2 3.1.2 depends on MarkupSafe>=2.0
    mako 1.2.4 depends on MarkupSafe>=0.9.2
    werkzeug 2.3.3 depends on MarkupSafe>=2.1.1


removedd Mako==1.2.4

