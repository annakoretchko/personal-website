from flask import Blueprint, Flask, g, jsonify, render_template, request, Response, redirect, url_for, send_from_directory
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
import os
import helper

# Configure application
app = Flask(__name__)

@app.route('/index', methods=['POST', 'GET'])
@app.route('/', methods=['POST', 'GET'])
def index():

    title_text = 'Title of Page Goes Here'

    return render_template('index.html',
                                title_text=title_text,
                                title="SUBTITLE OF LANDING PAGE HERE",
                                id="index")


@app.route('/portfolio', methods=['POST', 'GET'])
def portfolio():

    # default language if just portfolio is entered in url

        # get the title content for the portfolio page
    title_text = "projects go here"

    return render_template('/portfolio.html',
                            title_text=title_text,
                            title="PROJECT PORTFOLIO",
                            id="portfolio")

# @app.route('/about', methods=['POST', 'GET'])
# def about():

#     # get the title content for the portfolio page
#     title_text = "about go here"
#     # skills1= {"read": '1', "write": '4', "run": '5'}
#     # skills2= {"code": '1', "bike": '4', "lift": '5'}
#     # #skills = [skills1,skills2]
#     # skills = {"code": 'test', "bike": '4', "lift": '5'}
#     skills = helper.get_skill_content()

#     return render_template('/about.html',
#                             title_text=title_text,
#                             skills = skills,
#                             title="ABOUT ME",
#                             id="about")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)