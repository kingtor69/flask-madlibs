from flask import Flask, request, render_template
from Flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = 'not-so-secret'


debug = DebugToolbarExtension(app)
