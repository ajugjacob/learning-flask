from flask import Flask, render_template, url_for
'''hello'''
app = Flask(__name__)

posts = [
    {
        'title' : 'Blog post 1',
        'name' : 'Aju Jacob',
        'date' : '2nd May',
        'content' : 'Hi there, this is my first post'
    },
    {
        'title' : 'Blog post 2',
        'name' : 'Jane Doe',
        'date' : '3nd May',
        'content' : 'Hello there, this is my second post'
    }
]

@app.route('/')
@app.route('/home')

def home():
    return render_template('home.html', posts=posts)

@app.route('/about')

def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
