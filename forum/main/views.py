from . import main

@main.route('/')
def index():
	return '''this is a test'''

