from flask import Flask, render_template

myobj = Flask(__name__)
name = "Lisa"
city_names = ['Paris', 'London', 'Rome', 'Tahiti']

@myobj.route("/")
def home():
	return '''
<html>
        <body>
        <h1> Welcome '''+  name +'''!</h1>
        <ahref="www.google.com">notgoogle</a>
	{% for list in lists %}
                \n<ul><li>+list+</li></ul>\n
        {% endfor %}
        </body>
</html>
'''

#myobj.run()

