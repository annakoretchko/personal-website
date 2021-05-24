from flask import Blueprint, Flask, g, jsonify, render_template, request, Response, redirect, url_for, send_from_directory, flash

import os
import helper
import pandas as pd
from flask_mail import Mail, Message
import secrets


# Configure application
app = Flask(__name__)
mail= Mail(app)


app.config['SECRET_KEY'] = secrets.SECRET_KEY

@app.route('/index', methods=['POST', 'GET'])
@app.route('/', methods=['POST', 'GET'])
def index():

    title_text = 'Welcome to my site!'

    skills = helper.get_skill_content()

    title = "Hello! I am currently a Data Scientist and I created this site as a way to host my projects, share ideas and explore development tools."
    return render_template('index.html',
                                title_text=title,
                                title=title_text,
                                skills = skills,
                                id="index")


@app.route('/portfolio', methods=['POST', 'GET'])
def portfolio():

    # default language if just portfolio is entered in url

        # get the title content for the portfolio page
    title_text = "Here are some of my best, newest, or just intersting projects I have done. Enjoy the demo's and exploring the source code on my GitHub."

    # get all projects from the database
    zipped = helper.get_portfolio_content()
    return render_template('/portfolio.html',
                            title_text=title_text,
                            title="Portfolio",
                            id="portfolio",
                            projects=zipped)

@app.route('/about', methods=['POST', 'GET'])
def about():

    # get the title content for the portfolio page
    title_text = "I am extremely passionate about data, as it allows to cross over into any field and is integral to every thing we do today. I love fitness and finance, thus a lot of my personal pet projects are around my own fitness or financial data. I have my Master's from Georgia Teach and am intersted in FinTech and Financial Engineering."

    skills = helper.get_skill_content()

    return render_template('/about.html',
                            title_text=title_text,
                            skills = skills,
                            title="About Me",
                            id="about")


@app.route('/graph', methods=['POST', 'GET'])
def graph():

    # path to demo data
    
    data_path = "/static/demo_data/board_games.csv"
    #d3_path = "/templates/lib/d3.v5.min.js"
    return render_template('/graph.html',
                            data_path =data_path)



@app.route('/interactive', methods=['POST', 'GET'])
def interactive():

    # path to demo data
    
    data_path = "/static/demo_data/board_games.csv"
    #d3_path = "/templates/lib/d3.v5.min.js"
    return render_template('/interactive.html',
                            data_path =data_path)



@app.route('/choropleth', methods=['POST', 'GET'])
def choropleth():

    # path to demo data
    
    data_path = "/static/demo_data/average-ratingcsv"
    #d3_path = "/templates/lib/d3.v5.min.js"
    return render_template('/choropleth.html',
                            data_path =data_path)



@app.route('/garmin', methods=['POST', 'GET'])
def garmin():

    helper.get_network_graph_data()


    # get the title content for the portfolio page
    title_text = "Analyzing this data allows me to gain insights into my running techniques. For example, I know I have the best cadence and run the fastest when running 3 miles in contrast to 2 or 4).\nAdditionally, I can see my heart rate is decreasing over the past 8 years, meaning I am getting more fit and optimizing my anaerobic threshold."
    demo_data = helper.get_garmin_demo_data()
    

    return render_template('/garmin.html',
                            title_text=title_text,
                            demo_data = demo_data,
                            title="Garmin Data Exploration",
                            id="about")

@app.route('/contact', methods=["GET","POST"])
def contact():
    title_text = "TITLE HERE"
    
    form = helper.ContactForm()
    
    if request.method == 'POST':
        name =  request.form["name"]
        email = request.form["email"]
        subject = request.form["subject"]
        message = request.form["message"]
        #res = pd.DataFrame({'name':name, 'email':email, 'subject':subject ,'message':message}, index=[0])
        #res.to_csv('./contactusMessage.csv')
       
        thanks_response =helper.send_me_email(app,name,email,subject,message)
        helper.send_user_email(app,name,email,subject,message)

        confirmation_text = "A confirmation e-mail has been sent to you"
        return render_template('/contact.html', 
                                form=form,
                                title_text=confirmation_text,
                                title = thanks_response,
                                id = "contact")
    else:
        
        return render_template('/contact.html', 
                                form=form,
                                title_text=title_text,
                                title = "CONTACT TILEEEEE",
                                id = "contact")






@app.route("/robots.txt")
def robots():
    '''
    Add robots.txt file to avoid google indexing
    '''

    return send_from_directory(app.static_folder, request.path[1:])


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)


