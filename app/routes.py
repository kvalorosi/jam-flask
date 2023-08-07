from app import app

from flask import flash, redirect, render_template, request, url_for
import requests
from app.auth.forms import FoodForm
# from app.models import Products

@app.route('/')
def land():

    return render_template('opening.html')

