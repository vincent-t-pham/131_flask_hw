from flask import Flask, render_template

myapp = Flask(__name__)
name = "Lisa"
city_names = ['Paris', 'London', 'Rome', 'Tahiti']

@myapp.route("")
def home():
	return render_template('htmlf.html', name = name, lists = city_names)

#myapp.run()

