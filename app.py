from flask import Flask, render_template, request, redirect, jsonify, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/event')
def event():
    return render_template('timeline.html')


# if __name__ == '__main__':
#     app.run(debug=True)
