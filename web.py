from flask import Flask, render_template, flash, redirect, url_for, request, jsonify
import os, string, random, time
from scripts.checks import get_users, get_num, print_log, get_log_files, get_log_file
from bot import ad_send
import json
import asyncio

app = Flask(__name__)
app.config['SECRET_KEY'] = 'KEY'

@app.route("/", methods=['GET', 'POST'])
def index():
	users = get_num()
	print_log(f"Page: \"/\" | {request.remote_addr}", 'INFO', 'WEB')
	return render_template('index.html', users=users)

@app.route("/users", methods=['GET', 'POST'])
def index1():
	u = get_users()
	print_log(f"Page: \"/users\" | {request.remote_addr}", 'INFO', 'WEB')
	return render_template('users.html', users=u)

@app.route("/user/<id>", methods=['GET', 'POST'])
def index2(id):
	print_log(f"Page: \"/user/{id}\" | {request.remote_addr}", 'INFO', 'WEB')
	return render_template('user.html', id=id)

@app.route("/ad", methods=['GET', 'POST'])
def index3():
	print_log(f"Page: \"/ad\" | {request.remote_addr}", 'INFO', 'WEB')
	return render_template('ad.html')

@app.route("/send", methods=['GET', 'POST'])
def index4():
	text = ''
	if request.method == 'GET':
		text = request.values.get('text')
	elif request.method == 'POST':
		text = request.form.get('text')
	print_log(f"Page: \"/send\" | {request.remote_addr}", 'INFO', 'WEB')
	ioloop = asyncio.new_event_loop()
	ioloop.run_until_complete(ad_send(text))
	ioloop.close()
	return jsonify({'Кол-во получателей смотрите в логах': ''})

@app.route("/logs", methods=['GET', 'POST'])
def index5():
	files = get_log_files()
	print_log(f"Page: \"/logs\" | {request.remote_addr}", 'INFO', 'WEB')
	return render_template('logs.html', files=files)

@app.route("/log/<file>", methods=['GET', 'POST'])
def index6(file):
	text = get_log_file(file)
	print_log(f"Page: \"/logs\" | {request.remote_addr}", 'INFO', 'WEB')
	return render_template('log.html', file=text)

@app.errorhandler(404)
def not_found_error(error):
	print_log(f"404", 'WARNING', 'WEB')
	return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(error):
	print_log(f"500", 'ERROR', 'WEB')
	return render_template('500.html'), 500

if __name__ != '__main__':
	print_log(f"Web starting in 0.0.0.0:5000", 'INFO', 'WEB')
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)
	print_log(f"Web stoping", 'INFO', 'WEB')