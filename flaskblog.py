# server to run our api
from flask import Flask, request, jsonify, render_template


#jsonify is used to create a json reponse

# GET -- Request data from a specified source
# POST -- Create a resource
# PUT -- update a resource
# DELETE -- delete data from resource

app = Flask(__name__) # Flask application

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    },

]

@app.route("/")
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/home/about')
@app.route('/about')
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)