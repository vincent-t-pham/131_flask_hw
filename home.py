from flask import Flask, render_template

myobj = Flask(__name__)
name = "Lisa"
city_names = ['Paris', 'London', 'Rome', 'Tahiti']

@myobj.route("/")
def home():
	return render_template('htmlf.html', name = name, lists = city_names)

#myobj.run()

