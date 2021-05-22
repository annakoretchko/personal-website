from flask import request
import os
from flask_wtf import FlaskForm
from wtforms import TextField, BooleanField, TextAreaField, SubmitField
import pandas as pd
from flask_mail import Mail, Message
import secrets
from utils import get_data_utils as get_data_utils
from utils import visualize_data_utils as visualize_data_utils
import json

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
        "Python": [["Science Stack",5,'NumPy, pandas, SciPy, scikit learn, cvxpy, sklearn'],
                                  ["Data Visualization",4,'D3, Plotly, flask, bootstrap'],
                                  ["Deployment",4,'PyInstaller, Docker, GCP, Bash'],
                                  ["OOP and Procedural",3,'Modeling, Inheritance, Class, jupyter notebooks'],
                                  ["Other Languages",4,'R, MATLAB, javascript, html, Spark, Hadoop']],


        "ETL": [["Data Wrangling",5,'PCA, Standardization, Normalization'],
                                ["Pipeline Structure",5,'Source, Target, Organization, Optimization'],
                                ["SQL",4,'sqlite , NoSQL, PostgresSQL'],
                                ["API",4,'REST, request, HTTP'],
                                ["FTP",5,'bulk transport']],

        "Analytics": [["Probability Distributions",4,'Bernoulli, Binomial, Exponential, Geometric, Memoryless, Normal, Poisson, Weibull'],
                                ['Design of Experiment',5,'A/B testing, ANOVA, Factorial, Multi-armed bandit, Blocking, Balanced'],
                                ["Data",4,'Attribute, Categorical, Feature, PCA, Predictor, Quantitative, Scaling, Strucuted/Unstructured, Time Series'],
                                ["Variable Selection",4,'Backward Eliminiation, Forward Selection, Elastic Net, Overfitting, Ridge Regression, Stepwise Regression, Lasso Regression'],
                                ["Model Quality",4,'AIC, BIC, Confusion Matrices, k-fold cross-validation, MLE']],   
  

        "Data Science": [["Unsupervised Machine Learning",4,'Clustering (kmeans), Deep Learning, Neral Netowrk'],
                                ["Supervised Machine Learning",4,'Classification (KNN,SVM),Regression'],
                                ["Regression",4,'AUC, ROC, R-Sqaured, Bayesian, Box-Cox, CART, Classification Tree, Linear, Logistic, KNN regression, Spline Regression'],
                                ["Time Series Models",4,'ARIMA, Seasonality, Exponential Smoothing, GARCH, Holt-Winters, Moving Average, Trend, Cycles'],
                                ["Deterministic Optimization",4,'Convex/Concave, Greedy algorithm,Integer program,NP hard,Louvain algorithm']],
                                                            
                                  
                                  }
    

    return skill_dict
                            
                            
                            
                            

def send_me_email(app,name,email,subject,message):

    app.config['MAIL_SERVER']='smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = secrets.MAIL_USERNAME
    app.config['MAIL_PASSWORD'] = secrets.MAIL_PASSWORD
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    mail = Mail(app)
    msg = Message(subject, sender = email, recipients = ['annakoretchko@gmail.com'])
    msg.body = message + "\nSender's Name: " + name + "\nSender's e-mail: " + email 
    mail.send(msg)
    thanks_response = "Thanks for connecting "+str(name)+"!"
    return thanks_response


def send_user_email(app,name,email,subject,message):

    app.config['MAIL_SERVER']='smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = secrets.MAIL_USERNAME
    app.config['MAIL_PASSWORD'] = secrets.MAIL_PASSWORD
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    mail = Mail(app)
    msg = Message(subject, sender = email, recipients = [email])
    msg.body = "Thanks for connecting, " + name +"!"
    mail.send(msg)
   

def get_portfolio_content():
    '''
    Function to get the portfolio projects from the database
    Args: lang = str; specifies language selected by user
    Returns: zipped
    '''

    #db_row = check_language('portfolio', lang)
    db_row = []
    # instantiate a list to save all projects in
    project_list = []
    # iterate through all the projects in the database
    for project in db_row:
        one_project = []
        # add the title, description, skills and image name
        one_project.extend(project[1:5])
        # instantiate list for links
        links = []
        if project[6] != 'NaN':
            links.append(["Blog Post", project[6]])
        if project[5] != 'NaN':
            links.append(["Code", project[5]])
        one_project.append(links)

        # assign single project to entire project_list
        project_list.append(one_project)

    # create list of lists that contains pairs of projects
    if len(project_list) % 2 == 0:
        pass
    else:
        project_list.append(['placeholder'])
    iterator = iter(project_list)
    zipped = zip(iterator, iterator)

    return zipped


  
def get_garmin_demo_data():
    
    data_path = 'static/demo_data/Month.csv'
    # reads in data path of csv to dataframe 
    df = pd.read_csv(data_path)

    # subset and rename cols
    df = get_data_utils.rename_cols(df)

    # remove units from df
    df = get_data_utils.remove_units(df)

    # convert astype for each column to appropriate type
    df = get_data_utils.convert_type(df)

    df = df.drop(columns = ['Time_Period'])

    # combo data
    #df_combo = visualize_data_utils.create_combo_chart(df)

    #df_HR_cadence = visualize_data_utils.create_combo_HR_cadence(df)

    #df_speed_distance = visualize_data_utils.create_combo_speed_distance(df)

    df_combo_avg_distance = visualize_data_utils.create_combo_chart_Avgerage_Distance(df)
    return df
   

def get_network_graph_data():

    data_path = 'static/demo_data/board_games.csv'
    df = pd.read_csv(data_path)
    print(df)
    ls = df.values.tolist()
    print(ls)
    for i in ls:
        print(i,',')


    df_json = df.to_json()
    print(df_json)

    return df