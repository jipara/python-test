from flask import Flask
from flask import render_template
import requests


# parameters = {
#     "name": "jipara"
# }
# response = requests.get(url="https://api.agify.io", params=parameters)
# response.raise_for_status()
# data = response.json()
# data1 = data["age"]
#
#
# response1 = requests.get(url="https://api.genderize.io", params=parameters)
# response1.raise_for_status()
# data2 = response1.json()
# gender = data2["gender"]
app = Flask(__name__)


# def make_h1(function):
#     def wrapper(*args, **kwargs):
#         return "<h1>" + function(args[0]) + "</h1>"
#
#     return wrapper


# @app.route("/guess/<name>/")
# def greet(name):
#     name1 = name.title()
#     return render_template("index.html", name=name1, data=data1, gender_v=gender)

@app.route("/guess/<name>/")
def greet(name):
    name1 = name.title()
    gender_url = f"https://api.agify.io?name={name}"
    response = requests.get(gender_url)
    gender_response = response.json()
    gender = gender_response["gender"]
    age_url = f"https://api.agify.io={name}"
    age_response = requests.get(age_url)
    age = age_response.json()
    data1 = age["age"]
    return render_template("index.html", name=name1, data=data1, gender_v=gender)


@app.route("/blog/<num>")
def get_blog(num):
    blog_url = "https://www.npoint.io/docs/646400778124cf1e97d3"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    # Run the app in debug mode to auto-reload
    app.run(debug=True)
