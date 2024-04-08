from flask import Flask, render_template, request
from flask_restx import Api, Resource
import pymongo  # Import PyMongo

app = Flask(__name__)
api = Api(app)

# Your MongoDB connection string
CONNECTION_STRING = "mongodb://your_username:your_password@your_host:your_port/your_database_name"

client = pymongo.MongoClient(CONNECTION_STRING)
db = client['your_database_name']  # Select the database 
collection = db['user_info']        # Select the collection

@api.route('/')  # Change the route for the homepage 
class UserInfo(Resource):
    def get(self):
        return render_template('userinfo.html')  # Render the HTML form

def post(self):
    city_of_birth = request.form['city_of_birth']
    name = request.form['name']

    # Create a dictionary with the form data
    user_info = {"name": name, "city_of_birth": city_of_birth}

    # Insert the dictionary into the MongoDB collection
    collection.insert_one(user_info)

    # Do something with the collected information (e.g., display it)
    return f"Hello {name} from {city_of_birth}!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
