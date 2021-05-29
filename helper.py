from flask import request
import os
from flask_wtf import FlaskForm
from wtforms import TextField, BooleanField, TextAreaField, SubmitField
import pandas as pd
from flask_mail import Mail, Message
import secrets
import json
import pandas as pd
import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt
# from datetime import datetime as date
# import plotly
# import plotly.express as px
# import plotly.graph_objects as go
# from plotly.tools import FigureFactory as FF
# from sklearn.linear_model import LinearRegression
# import dash
# import dash_core_components as dcc
# import dash_html_components as html
# from dash.dependencies import Input, Output
# import numpy as np
# import plotly.graph_objects as go
# import plotly.express as px
# from sklearn.model_selection import train_test_split
# from sklearn import linear_model, tree, neighbors


from utils import get_data_utils as get_data_utils
from utils import visualize_data_utils as visualize_data_utils

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
                                ["Data",4,'Attribute, Categorical, Feature, PCA, Predictor, Quantitative, Scaling, Structured/Unstructured, Time Series'],
                                ["Variable Selection",4,'Backward Elimination, Forward Selection, Elastic Net, Overfitting, Ridge Regression, Stepwise Regression, Lasso Regression'],
                                ["Model Quality",4,'AIC, BIC, Confusion Matrices, k-fold cross-validation, MLE']],   
  

        "Data Science": [["Unsupervised Machine Learning",4,'Clustering (kmeans), Deep Learning, Neral Netowrk'],
                                ["Supervised Machine Learning",4,'Classification (KNN,SVM),Regression'],
                                ["Regression",4,'AUC, ROC, R-Squared, Bayesian, Box-Cox, CART, Classification Tree, Linear, Logistic, KNN regression, Spline Regression'],
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



# def compare_time_frames(model_selection = "knn"):
    
#     """[Takes two sets of times periods and compares results of the two time frames]

#     Args:
#         file_path ([str]): [path to csv]
#         start_1 ([type]): [beginning of time_frame_1]
#         end_1 ([type]): [end of time_frame_1]
#         start_2 ([type]): [beginning of time_frame_2]
#         end_2 ([type]): [end of time_frame_2]
#     """
#     # Run faster in NC or SoFlo?
#     file_path ='static/demo_data/combined_activities.csv'
#     start_1 = '2019-07-01'
#     end_1 = '2020-04-01'
#     start_2 = '2020-10-03'
#     end_2 = '2021-04-26'
#     # reads in activities df
#     df = pd.read_csv(file_path)


#     #Create new dataframe with only columns I care about
#     cols = ['name', 'upload_id', 'type', 'distance', 'moving_time',   
#             'average_speed', 'max_speed','total_elevation_gain',
#             'activity_date'
#         ]
#     df = df[cols]


#     # change avg speed
#     #df.loc[df["average_speed"] == 0,'average_speed'] = (df["distance"]  / df["moving_time"])*1000
#     run = df.loc[df['type'] == 'Run'] 
 
#     # convert time strings
#     start_1 = date.strptime(start_1, '%Y-%m-%d').date()
#     end_1 = date.strptime(end_1, '%Y-%m-%d').date()
#     start_2 = date.strptime(start_2, '%Y-%m-%d').date()
#     end_2 = date.strptime(end_2, '%Y-%m-%d').date()

#     run['activity_date'] = pd.to_datetime(run['activity_date']).dt.date

#     # chunk time frames

#     # create column that is T if in t1 and F all else
#     run['time_frame_1'] = np.where( (run['activity_date'] > start_1) & (run['activity_date'] < end_1), 'T', 'F')
#     # get rows that fall in t1 column 
#     time_frame_1 = run.loc[run['time_frame_1'] == 'T']


    
#     # create column that is F if in t2 and F all else
#     run['time_frame_2'] = np.where( (run['activity_date'] > start_2) & (run['activity_date'] < end_2), 'T', 'F')
#     # get rows that fall in t2 column
#     time_frame_2 = run.loc[run['time_frame_2'] == 'T']

#     # get speed for each time period and also converts (time is in seconds, distance is in meters.
#     #  m/s to mph 1 m/s to 2.237 mph)
#     t1_speed = round(time_frame_1['average_speed'].mean() * 2.237, 2)
#     t2_speed = round(time_frame_2['average_speed'].mean() * 2.237, 2)
#     t1_max_speed = round(time_frame_1['max_speed'].mean()* 2.237, 2)
#     t2_max_speed = round(time_frame_2['max_speed'].mean()* 2.237, 2)

#     print("Average T1 Speed: " + str(t1_speed) + " | Average T1 Max Speed: " + str(t1_max_speed) + '\n'
#         + "Average T2 Speed: " + str(t2_speed) + " | Average T2 Max Speed: " + str(t2_max_speed))

#     percent_increase_average = round((t2_speed - t1_speed) * 100 / t1_speed,2)
#     print("Percent increase average speed:",percent_increase_average)

#     percent_increase_average_max = round((t2_max_speed - t1_max_speed) * 100 / t1_max_speed,2)
#     print("Percent increase max speed:",percent_increase_average_max)

#     #sns.scatterplot(x='total_elevation_gain', y = 'average_speed', data = run).set_title("Speed vs Elevation Gain")
#     #sns.regplot(x='total_elevation_gain', y = 'average_speed', data = run).set_title("Speed vs Elevation Gain")
#     # saves image
#     #plt.show()
#     y1 = [t1_speed, t1_max_speed]
#     y2 = [t2_speed,t2_max_speed]
#     #df_compare = pd.DataFrame(list(zip(l1,l2)), columns = ['Average Speed','Max Speed'])

#     x_title=['Average Speed', 'Max Speed']

#     fig = go.Figure(data=[
#         go.Bar(name='Mountainous North Carolina', x=x_title, y=y1),
#         go.Bar(name='Hot & Humid Florida', x=x_title, y=y2)
#     ])
#     # Change the bar mode
#     fig.update_layout(barmode='group')
    
#     plot_json = json.dumps(fig, cls = plotly.utils.PlotlyJSONEncoder)

#     select_time = pd.concat([time_frame_2,time_frame_1])
   
#     # graph 2
#     #df = px.data.tips()
#     run = select_time[['total_elevation_gain','average_speed']]
   
#     X = run.total_elevation_gain.values.reshape(-1, 1)

#     model = LinearRegression()
#     model.fit(X, run.average_speed)

#     x_range = np.linspace(X.min(), X.max(), 100)
#     y_range = model.predict(x_range.reshape(-1, 1))

#     fig2 = px.scatter(run, x='total_elevation_gain', y='average_speed', opacity=0.65)
#     fig2.add_traces(go.Scatter(x=x_range, y=y_range, name='Regression Fit'))
    
#     plot_json2 = json.dumps(fig2, cls = plotly.utils.PlotlyJSONEncoder)



#     ## three model graph


#     # fig3 = train_and_display(run,model_selection)
#     # plot_json3 = json.dumps(fig3, cls = plotly.utils.PlotlyJSONEncoder)

#     return plot_json , plot_json2,run


# def train_and_display(run, name):
#     if name == None:
#         name = 'knn'
#     X = run.total_elevation_gain.values[:, None]
#     X_train, X_test, y_train, y_test = train_test_split(
#     X, run.average_speed, random_state=42)

#     models = {'Regression': linear_model.LinearRegression,
#         'DecisionTree': tree.DecisionTreeRegressor,
#         'knn': neighbors.KNeighborsRegressor}
 
#     model = models[name]()
#     model.fit(X_train, y_train)

#     x_range = np.linspace(X.min(), X.max(), 100)
#     y_range = model.predict(x_range.reshape(-1, 1))

#     fig = go.Figure([
#         go.Scatter(x=X_train.squeeze(), y=y_train, 
#                 name='train', mode='markers'),
#         go.Scatter(x=X_test.squeeze(), y=y_test, 
#                 name='test', mode='markers'),
#         go.Scatter(x=x_range, y=y_range, 
#                 name='prediction')
#         ])

#     plot_json3 = json.dumps(fig, cls = plotly.utils.PlotlyJSONEncoder)
   


#     return plot_json3