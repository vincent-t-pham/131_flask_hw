from app import myobj
from flask import render_template, flash, request, redirect, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
 
class LoginForm(FlaskForm):
    city = StringField('City Name', validators=[DataRequired()])
    submit = SubmitField('Submit')

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

