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
    title_text = "Here are some of my best, newest, or just interesting projects I have done. Enjoy the demo's and exploring the source code on my GitHub."

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
    title_text = "I am extremely passionate about data, as it allows to cross over into any field and is integral to everything we do today. I love fitness and finance, thus a lot of my personal pet projects are around my own fitness or financial data. I have my Master's from Georgia Tech and am intersted in FinTech and Financial Engineering."

    skills = helper.get_skill_content()

    return render_template('/about.html',
                            title_text=title_text,
                            skills = skills,
                            title="About Me",
                            id="about")


@app.route('/strava', methods=['POST', 'GET'])
def strava():

    # get the title content for the portfolio page
    title_text = "I have been using Strava since 2014, and for those of you unfamiliar with what Strava is, it's essentially a social media for runners, bikers and swimmers alike. A platform where equally obsessed athletes can gather and ogle over their exercise data. \n\
                I have been collecting running, swimming, lifting, and social media data surrounding my exercise efforts for the past 7 years, so I figured it was time to start doing some analytics ont he data. And sharing my methods and approach with you! \n\
                This project I will be going through the following: \n\
                    1. Provide a method to gather your most recent Strava data automatically, using python, via Strava's API \n\
                    2. Gather your historic Strava data through their site \n\
                    3. Clean and join the new and historic data \n\
                Start exploring my data and asking serious questions, like, can we predict the number of kudos I will receive on my next run by how many pictures I post? \n\
                But seriously, doing some cool Machine Learning, simple stats and other fun math to interpret our data!"

    skills = helper.get_skill_content()

    return render_template('/strava.html',
                            title_text=title_text,
                            skills = skills,
                            title="Strava Analysis",
                            id="strava")


@app.route('/graph', methods=['POST', 'GET'])
def graph():

    # path to demo data
    
    data_path = "/static/demo_data/board_games.csv"
    #d3_path = "/templates/lib/d3.v5.min.js"

    title_text = "Nodes, edges and weights are commonly used in data science today as the world increasingly places more value on network graphs. This graph allows the user to explore relationships between board games that are commonly played amongst the same user."
    title = "Board Game Analysis Network Graph"
    return render_template('/graph.html',
                            data_path =data_path,
                            title_text = title_text,
                            title = title, 
                            id = "graph")



@app.route('/interactive', methods=['POST', 'GET'])
def interactive():

    # path to demo data
    
    data_path = "/static/demo_data/board_games.csv"
    #d3_path = "/templates/lib/d3.v5.min.js"
    title_text = "My family is extremely competitive and loves to play board games. I wanted to work on some of my interactive data visualization skills and decided to use board game data as inspiration. The graph analyzes board game rankings by user over time and helps explore which games are popular today!"
    title = "Board Game Analysis Line Graph"
    return render_template('/interactive.html',
                            data_path =data_path,
                            title_text = title_text,
                            title = title,
                            id = "interactive")



@app.route('/choropleth', methods=['POST', 'GET'])
def choropleth():

    # path to demo data
    
    data_path = "/static/demo_data/average-ratingcsv"
    #d3_path = "/templates/lib/d3.v5.min.js"
    title = "Board Game Analysis Choropleth Map"
    title_text = "This geographical illustration lets the user interact and see where games are popular across the world! You'd be surprised by the amount of board game data available for data science!"
    return render_template('/choropleth.html',
                            data_path =data_path,
                            title = title,
                            title_text = title_text,
                            id = "choropleth")



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
                            id="choropleth")





@app.route('/contact', methods=["GET","POST"])
def contact():
    title_text = "Please shoot me an e-mail with any suggestions, comments, or concerns."
    
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
                                title = "Let's Connect!",
                                id = "contact")






@app.route("/robots.txt")
def robots():
    '''
    Add robots.txt file to avoid google indexing
    '''

    return send_from_directory(app.static_folder, request.path[1:])


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)


