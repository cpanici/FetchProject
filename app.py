from flask import Flask, render_template
from forms import PyramidForm
import os

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/', methods=['GET', 'POST'])
def index():
	form = PyramidForm()
	if form.validate_on_submit():
		word = form.word.data
		result = pyramid(word)
		return render_template('home.html', form=form, result=result)
	return render_template('home.html', form=form)


def pyramid(word):
	chars = set(word)
	counts = [word.count(c) for c in list(chars)]
	counts.sort()
	if counts[0] != 1: 
		return f'{word} is not a pyramid word.'
	else:
		for i in range(1, len(counts)):
			if counts[i] - 1 != counts[i-1]:
				return f'{word} is not a pyramid word.'
		return f'{word} is a pyramid word!'
