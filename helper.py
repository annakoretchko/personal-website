from flask import request
import os
from flask_wtf import FlaskForm
from wtforms import TextField, BooleanField, TextAreaField, SubmitField
import pandas as pd

class ContactForm(FlaskForm):
    name = TextField("Name")
    email = TextField("Email")
    subject = TextField("Subject")
    message = TextAreaField("Message")
    submit = SubmitField("Send")


def get_skill_content():
    '''
    Function to get the skills from the database
    Args: lang = str; specifies language selected by user
    Returns: skill_list
    '''

   
    skill_dict = {
        "Python": [["Science Stack",5,'NumPy,pandas,SciPy,seaborn, matplotlib, PyTables,scikit-learn,cvxpy,request'],
                                  ["Data Visualization",4,'D3, Plotly, flask, bootstrap'],
                                  ["Deployment",4,'PyInstaller, Docker, GCP, Bash'],
                                  ["OOP",4,'> 3 years'],
                                  ["Python",4,'> 3 years']],
        "ETL": [["Python",4,'> 3 years'],
                                ["Data Wrangling",5,'> 3 years'],
                                ["SQL",4,'> 3 years'],
                                ["Python",4,'> 3 years'],
                                ["Python",4,'> 3 years']],
                                  
        "Programming words ": [["Python",4,'> 3 years'],
                                ["Python",4,'> 3 years'],
                                ["Python",4,'> 3 years'],
                                ["Python",4,'> 3 years'],
                                ["Python",4,'> 3 years']],
                                                            
                                  
                                  }
    

    return skill_dict
                            
                            
                            
                            




  
