from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/featured-projects")
def featured():
    return render_template('featured.html', featured_active=True)


@app.route("/project-directory")
def directory():
    return render_template('directory.html', directory_active=True)


@app.route('/about')
def about():
    return render_template('about.html', about_active=True)
