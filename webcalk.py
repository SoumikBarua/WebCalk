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

if __name__ == "__main__":
	app.run()