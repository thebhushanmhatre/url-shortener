
# URL Shortener

App to share Urls and Files by uploading and saving them on this app.

### Technology Stack used:
1. HTML/CSS
1. Python

### Python Libraries Used:

**Framework used**: Flask

**For Testing**: pytest

**For Accessing Files**: os.path

**For working wih JSON**: json


### Steps to Run this app locally:
1. Fork the repo and Clone the app to your local machine.
1. Change directory to the app
```shell
cd url-shortener
```
1. Install `pipenv` to Setup Environment and Install the packages using following commands:
```shell
pip install pipenv
pipenv install
pipenv shell
```
Note: If you are creating a new app without forking an existing app then you need to install libraries using following commands 
```shell
pipenv install LIBRARY_NAME
```
1. To run the app in development environment (This helps in auto detecting the code changes)
```shell
export FLASK_ENV=development
```
1. If the name of the app is not app.py which is the case in our app.
```shell
export FLASK_APP=app_name
```
In our case, use:
```shell
export FLASK_APP=urlshort
```
1. Start the app using `flask run` command

Open [http://localhost:5000](http://localhost:5000) to view it in the browser.


### App Structure

* **urlshort.py** is the app that contains all the app logic.

* **urlshort** folder contains the satic and templates folder.
* **static** folder contains the static files such as the css/js and user_files folder
* **user_files** contains the images that we are going to upload.

* **templates** contains the HTML with python embedded which will be interpreted using Jinja.
Python code is written inside ```{{% # Python code %}}```
If code returns something remove the '%' from start and end i.e. ```{{ # Python code that returns/ needs to be displayed }}```

* **Pipfile** and **Pipfile.lock** contains the information on packages used in the app
These are auto created by pipenv.

* **conftest.py** and **test_main.py** are used for testing.

### Some Cool features

* **render_template:** Render HTML with Embedded Python Code.
* **request:** Contains request data.
* **redirect:** Redirects to given url.
* **url_for:** Finds logic based on method name instead of relying on url, Gives Flexibity in changing url when required without having to change inside logic.
* **flash:** Displays Alert messages.
* **abort:** Display Abort Error message.
* **session:** Helps store session data
* **jsonify:** Helps in converting data to JSON format.
* **Blueprint:** Helps in keeping the app structured.



## Contact me on [Linkedin](https://www.linkedin.com/in/thebhushanmhatre/).

