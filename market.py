from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Hello, !</h1>"

# @app.route('/about/<username>')
# def about_page(username):
#     return f"<h1>This is the about page of {username}</h1>"

@app.route('/home')
def home_page():
    return render_template("hello.html")

@app.route('/market')
def market_page():
    items = [
        {'name':'Laptop', 'price':1000},
        {'name':'Phone', 'price':500},
        {'name':'Tablet', 'price':750}
    ]
    return render_template("market.html" , items=items )
