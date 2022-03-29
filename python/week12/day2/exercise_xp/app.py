from flask import Flask, render_template
import random
import string

app = Flask(__name__)

letters = string.ascii_lowercase
random_string = ''.join(random.choice(letters) for i in range(256)) 

app.config['SECRET_KEY']= random_string

import routes