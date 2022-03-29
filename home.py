from flask import Flask, render_template

myapp_obj = Flask(__name__)

@myapp_obj.route("/")
def home():
	name = "Lisa"
	city_names = ['Paris', 'London', 'Rome', 'Tahiti']
	return render_template('htmlf.html', name = name, lists = city_names)

myapp_obj.run()

