from flask import request
import psycopg2
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

    #db_row = check_language('skills', lang)
    db_row= {"read": '1', "write": '4', "run": '5'}
    # instantiate a dict to save all projects in
    skill_dict = {}

    # iterate through all the skills in the database
    for skill in db_row:
        if skill[1] in skill_dict.keys():
            skill_dict[skill[1]].append(list(skill[2:5]))
        else:
            skill_dict[skill[1]] = [list(skill[2:5])]

    skill_dict= {'Programming Languages': ['read',4], 'Machine Learning': 'run', 'Software Engineering': 'code', 'Data Analysis':10}

    return skill_dict