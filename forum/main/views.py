from . import main
from flask import render_template

@main.route('/')
def index():
	return render_template('index.html')


@main.route('/test1')
def t1():
	return render_template('t1.html')

@main.route('/test2')
def t2():
	return render_template('t2.html')
