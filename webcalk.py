# Third-party imports

from flask import Flask, render_template, request, redirect, url_for
from forms import SubmissionForm

# Declare the app
app = Flask(__name__)
# Set up variables
app.config['SECRET_KEY'] = 'somesecretkey'
first = None
second = None
operation = None
counter = -1

@app.route("/", methods=['GET', 'POST'])
def index():
    global first, second, operation, counter
    counter += 1
    """Set up index front page."""
    
    form = SubmissionForm()
    print(str(form.validate_on_submit()))
    if form.validate_on_submit():
        first = form.first.data
        second = form.second.data
        operation = form.operations.data
        counter = -1
        return redirect(url_for('calculate', operationname=operation))
    else:
        print(form.first.data)
        print(form.second.data)
        if counter >= 1:
            # If either the first number and/or the second number is not an integer/float
            if (form.first.data is None) or (form.second.data is None):
                counter = -1
                return redirect(url_for('error'))
    return render_template('index.html', form=form)

@app.route("/result/<operationname>")
def calculate(operationname):
    global first, second, operation
    """Perform calculations."""

    result = None
    page_title = None
    if operation == 'addition':
        result = first + second
        page_title = 'Addition Operation'
    elif operation == 'subtraction':
        result = first - second
        page_title = 'Subtraction Operation'
    elif operation == 'multiplication':
        result = first * second
        page_title = 'Multiplication Operation'
    else:
        result = first / second
        page_title = 'Division Operation'

    calculation = {'first': first, 'second': second, 'operation': operation, 'result' : result}
    return render_template('result.html', title=page_title, calculation=calculation)

@app.route("/result/error")
def error():
    """Handle error."""
    return render_template('error.html')

@app.errorhandler(404)
def not_found_error(error):
    global counter
    coun
    return render_template('404.html'), 400

@app.errorhandler(500)
def internal_error(error):
    global counter
    counter = -1
    return render_template('500.html'), 500

@app.errorhandler(403)
def internal_error(error):
    global counter
    counter = -1
    return render_template('403.html'), 403

if __name__ == "__main__":
	app.run()