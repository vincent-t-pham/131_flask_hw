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
        <a href="www.google.com">notgoogle</a>
	<ul>
		<li>Paris</li>
		<li>London</li>
		<li>Rome</li>
		<li>Tahiti</li>
	</ul>
        </body>
</html>
'''

#myobj.run()

