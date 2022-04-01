from app import myobj
from app.forms import LoginForm
from flask import render_template, flash, request, redirect, flash

name = "Lisa"
city_names = ['Paris', 'London', 'Rome', 'Tahiti']

@myobj.route('/', methods=['GET', 'POST'])
def home():
	form = LoginForm()
	if form.validate_on_submit():
		result = request.form
		flash('{}' .format(form.city.data))
		return redirect('/')
	return render_template('home.html', name=name, lists=city_names, form=form)


#myobj.run()

