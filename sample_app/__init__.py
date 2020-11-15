from flask import Flask, render_template
from flask_buefy import Buefy

app = Flask(__name__)
Buefy(app)

# Define some routes
@app.route('/')
def index():
    return render_template('index.html')

app.run()
