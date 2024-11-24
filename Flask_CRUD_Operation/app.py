from flask import Flask 

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World!"

# for single file and single module 
# import Route_Controller.userRouteController as userRouteController
# from Route_Controller import userRouteController


# for all pakage of RouteController
# from Route_Controller import *
try:
    from Route_Controller import *
except Exception as e:
    print(e)


