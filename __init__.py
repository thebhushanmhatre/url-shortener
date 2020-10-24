from flask import Flask

def create_app(test_config=None):
	app = Flask(__name__)
	app.secret_key = 'l32ig5l3i43jb6kj54kj7' # Randomly typed

	from . import urlshort
	app.register_blueprint(urlshort.bp)

	return app