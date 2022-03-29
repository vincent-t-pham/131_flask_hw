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
        <a href="/www.google.com/">not google</a>
        {% for list in lists %}
                <ul><li>{{ list }}</li></ul>
        {% endfor %}
        </body>
</html>
'''

#myobj.run()

