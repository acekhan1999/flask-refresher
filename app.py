# main py file that is responsible for running the web application

# import libraries

# render_template - to look into the templates folder for the specified HTML page and display the page.
from flask import Flask, render_template, request, redirect, url_for, session

import json, uuid

# app variable - this var. is responsible to run the web application
app = Flask(__name__)

# secret key for using session variables
app.secret_key = str(uuid.uuid4())

def sessions_init():
    session['customer_data'] = None

# route - responsible to redirect the user to the specified HTML page. Take data from the HTML page using POST and GET methods
@app.route('/')
def index():
    sessions_init()
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

with open('static/data/customer_data.json', 'r') as file:
    main_customer_data = json.load(file)

# form registration
@app.route("/register", methods=["POST", "GET"])
def register():

    if request.method == "POST":
        customer_name = request.form['customer_name']
        customer_email = request.form['customer_email']
        customer_password = request.form['customer_password']

        print(f"Customer Name: {customer_name} \nCustomer Email: {customer_email}")


        customer_data = {
            "id" : str(uuid.uuid4()),
            "data" : {
                    "customer_name": customer_name,
                    "customer_email": customer_email,
                    "customer_password": customer_password
            }
        }

        main_customer_data.append(customer_data)

        with open('static\data\customer_data.json', 'w') as file:
            json.dump(main_customer_data, file, indent=2)

        return redirect("dashboard")

    return render_template("registration.html")

# creating a login
@app.route('/login', methods=["POST", "GET"])
def login():

    if request.method == "POST":
        customer_email = request.form['customer_email']
        customer_password = request.form['customer_password']

        print(f"Customer Email: {customer_email} \nCustomer Password: {customer_password}")

        customer_data_index = None

        for index in range(len(main_customer_data)):
            # print(index)
            # print(main_customer_data[index]['data'])

            if main_customer_data[index]['data']['customer_email'] == customer_email and main_customer_data[index]['data']['customer_password'] == customer_password:
                print('found')
                customer_data_index = index
            
        print(customer_data_index)
        
        if customer_data_index != None:
            session['customer_data'] = main_customer_data[int(customer_data_index)]['data']
            return redirect('dashboard')
        else:
            return render_template("login.html", error="Invalid Login Credentials")
            

    return render_template("login.html", error=None)

@app.route('/dashboard')
def dashboard():

    if session['customer_data'] != None:
        return render_template("dashboard.html")
    else:
        return redirect("login")

@app.route('/logout')
def logout():
    sessions_init()
    return redirect("/login")

# NOTE: this always has to be at the end of the script!
# this is responsible to run your app and also start your debugger to check any errors in the code.

if __name__ == '__main__':
    app.run(debug=True)
