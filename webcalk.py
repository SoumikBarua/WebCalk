# Third-party imports

from flask import Flask, render_template

# Declare the app
app = Flask(__name__)

@app.route("/")
def hello():
	return render_template('webcalk.html')

if __name__ == "__main__":
	app.run()