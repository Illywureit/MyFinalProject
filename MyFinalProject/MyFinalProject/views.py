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
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

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
from MyFinalProject.models.Forms import OlympicMedals  
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

from MyFinalProject.models.QueryFormStructure import LoginFormStructure
from MyFinalProject.models.QueryFormStructure import UserRegistrationFormStructure
from MyFinalProject.models.LocalDatabaseRoutines import create_LocalDatabaseServiceRoutines
  
db_Functions = create_LocalDatabaseServiceRoutines() 
app.config['SECRET_KEY'] = 'h'

#this is the route for the Home page:
@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )
#this is the route for the Contact page:
@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )
#this is the route for the About page:
@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
#this is the route for the Data page:
@app.route('/data')
def data():
    """Renders the about page."""
    return render_template(
        'data.html',
        title='Data',
        year=datetime.now().year,
        message='My data page.'
    )
#this is the route for the first data: 
@app.route('/olimpic_medals' , methods = ['GET' , 'POST'])
def olimpic_medals():

    print("medals")

    """Renders the about page."""
    #creats the expand and collapse buttons:
    form1 = ExpandForm()
    form2 = CollapseForm()
    #reads the csv:
    s = path.join(path.dirname(__file__), 'static\\data\\olimpic-medal.csv')
    
    df = pd.read_csv(path.join(path.dirname(__file__), 'static\\data\\olimpic-medal.csv'), encoding = "utf-8")
    raw_data_table = ''
     
    # if the user click on the button:
    if request.method == 'POST':
        if request.form['action'] == 'Expand' and form1.validate_on_submit():
            raw_data_table = df.to_html(classes = 'table table-hover')
        if request.form['action'] == 'Collapse' and form2.validate_on_submit():
            raw_data_table = ''

    
 # returns the HTML page with the table and the parameters:
    return render_template(
        'medal.html',
        title='Olimpic medals',
        year=datetime.now().year,   
        message='Olimpic medals dataset page.',
     
        raw_data_table = raw_data_table,
        form1 = form1,
        form2 = form2
    )
#this is the route for the second data: 
@app.route('/top_runners' , methods = ['GET' , 'POST'])
def top_runners():

    print("runners")

    """Renders the about page."""
     #creats the expand and collapse buttons:
    form1 = ExpandForm()
    form2 = CollapseForm()
    #reads the csv:
    s = path.join(path.dirname(__file__), 'static\\data\top-runners.csv')
    print(s)
    df = pd.read_csv(path.join(path.dirname(__file__), 'static\\data\\top-runners.csv'), encoding = "utf-8")
    raw_data_table = ''
   
    # if the user click on the button:
    if request.method == 'POST':
        if request.form['action'] == 'Expand' and form1.validate_on_submit():
            raw_data_table = df.to_html(classes = 'table table-hover')
        if request.form['action'] == 'Collapse' and form2.validate_on_submit():
            raw_data_table = ''

    
# returns the HTML page with the table and the parameters:
    return render_template(
        'runners.html',
        title='Top runners',
        year=datetime.now().year,   
        message='top runners dataset page.',
     
        raw_data_table = raw_data_table,
        form1 = form1,
        form2 = form2
    )
#this is the route for the register page:
@app.route('/register', methods=['GET', 'POST'])
def Register():
    form = UserRegistrationFormStructure(request.form)
    #if you click submit:
    if (request.method == 'POST' and form.validate()):
        if (not db_Functions.IsUserExist(form.username.data)):
            db_Functions.AddNewUser(form)
            db_table = ""

            flash('Thanks for registering new user - '+ form.FirstName.data + " " + form.LastName.data )
            # Here you should put what to do (or were to go) if registration was good
        else:
            flash('Error: User with this Username already exist ! - '+ form.username.data)
            form = UserRegistrationFormStructure(request.form)
        # returns the HTML page with the parameters:
    return render_template(
        'register.html', 
        form=form, 
        title='Register New User',
        year=datetime.now().year,
        repository_name='Pandas',
        )

# -------------------------------------------------------
# Login page
# This page is the filter before the data analysis
# -------------------------------------------------------

@app.route('/login', methods=['GET', 'POST'])
def Login():
    form = LoginFormStructure(request.form)

    #if you press submit

    if (request.method == 'POST' and form.validate()):
        #checks if the input matches the information in the system
        if (db_Functions.IsLoginGood(form.username.data, form.password.data)):
          return redirect('olympic-medals')
           #if it does, it approves the log-in and redirects the user to the 'Query' page.
        else:
            flash('Error in - Username and/or password')
   
    return render_template(
        'login.html', 
        form=form, 
        title='Login to data analysis',
        year=datetime.now().year,
        repository_name='Pandas',
        )
@app.route('/olympic-medals' , methods = ['GET' , 'POST'])
def olympic_medals():

    print("Olympic Medals")

    form1 = OlympicMedals()
    chart = '/static/imgs/1200px-Olympic_rings_without_rims.svg.png'

   #reads the data file.

    df = pd.read_csv(path.join(path.dirname(__file__), 'static/data/olimpic-medal.csv'))

   #Creates a list of the countries that appear in the data.

    country_choices = list(set(df['Country']))

   #Cleans the first line in the list (wich is a NaN).

    clean_country_choices = [x for x in country_choices if x == x]

    #creates list of tuples as the form requires.
   
    m = list(zip(clean_country_choices , clean_country_choices))
    form1.country.choices = m 


    if request.method == 'POST':
        #pull the country from the form
        country = form1.country.data

        #filter the data with the chosen country.
        df1 = df.loc[df['Country'] == country]
        
        #Creates seires that includes all types of discipline, sizing them and puts them in decending order.
        s = df1.groupby('Discipline').size().sort_values(ascending=False)


        #-------- Creates the graph acording the seiries and makes it a pic
        fig = plt.figure()
        ax = fig.add_subplot(111)
        fig.subplots_adjust(bottom=0.4)
        s.plot(ax = ax , kind = 'bar', figsize = (24, 8) , fontsize = 22 , grid = True)
        chart = plot_to_img(fig)
        #--------

    
    return render_template(
        'olympic.html',
        form1 = form1,
        chart = chart
    )
def plot_to_img(fig):
    pngImage = io.BytesIO()
    FigureCanvas(fig).print_png(pngImage)
    pngImageB64String = "data:image/png;base64,"
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')
    return pngImageB64String