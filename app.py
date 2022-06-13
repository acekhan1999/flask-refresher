# main py file that is responsible for running the web application

# import libraries

# render_template - to look into the templates folder for the specified HTML page and display the page.
from flask import Flask, render_template

# app variable - this var. is responsible to run the web application
app = Flask(__name__)

# route - responsible to redirect the user to the specified HTML page. Take data from the HTML page using POST and GET methods
@app.route('/')
def index():
    return "Welcome Back! To Flask Web Application"

@app.route('/about')
def about():
    return "I'm an old flask developer upskilling myself to incoprate flask and react native!"

# route variables
# @app.route('/services/<str:service_id>')
@app.route('/services/<int:service_no>')
def services(service_no):

    print(type(service_no))
    return f"Service No. {(service_no)} is now available"

# adding html files
@app.route('/products')
def products():

    return render_template('products.html')

# NOTE: this always has to be at the end of the script!
# this is responsible to run your app and also start your debugger to check any errors in the code.

if __name__ == '__main__':
    app.run(debug=True)