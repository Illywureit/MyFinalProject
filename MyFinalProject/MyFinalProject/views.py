"""
Routes and views for the flask application.
"""
import sys
from datetime import datetime
from flask import render_template
from MyFinalProject import app

import matplotlib.pyplot as plt
import os
from collections import Counter
import pandas as pd
from flask_bootstrap import Bootstrap
bootstrap = Bootstrap(app)


from MyFinalProject.models.Forms import ExpandForm
from MyFinalProject.models.Forms import CollapseForm

import io
import base64
    
from datetime import datetime
from flask import render_template

from flask import render_template, redirect, request
    
    
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
    
import numpy as np
import matplotlib.pyplot as plt
    
    
import json 
import requests
from os import path   
    
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
    
    
import os
    
    
from flask   import Flask, render_template, flash, request
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from wtforms import TextField, TextAreaField, SubmitField, SelectField, DateField
from wtforms import ValidationError
    

app.config['SECRET_KEY'] = 'IM ILI AND IM BITCH'

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/data')
def data():
    """Renders the about page."""
    return render_template(
        'data.html',
        title='Data',
        year=datetime.now().year,
        message='My data page.'
    )

@app.route('/olimpic_medals' , methods = ['GET' , 'POST'])
def olimpic_medals():

    print("medals")

    """Renders the about page."""
    form1 = ExpandForm()
    form2 = CollapseForm()
    s = path.join(path.dirname(__file__), 'static\\data\\olimbic-medal.csv')
    print(s)
    df = pd.read_csv(path.join(path.dirname(__file__), 'static\\data\\olimbic-medal.csv'), encoding = "utf-8")
    raw_data_table = ''
    #df = pd.read_csv("data/olimpic medal.csv", encoding = "ISO-8859-1")

    if request.method == 'POST':
        if request.form['action'] == 'Expand' and form1.validate_on_submit():
            raw_data_table = df.to_html(classes = 'table table-hover')
        if request.form['action'] == 'Collapse' and form2.validate_on_submit():
            raw_data_table = ''

    

    return render_template(
        'medal.html',
        title='Olimpic medals',
        year=datetime.now().year,   
        message='Olimpic medals dataset page.',
     
        raw_data_table = raw_data_table,
        form1 = form1,
        form2 = form2
    )