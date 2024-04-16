from flask import Flask, render_template, request
import pymongo

app = Flask(__name__)

# Create a MongoDB client, connect to MongoDB server (replace the URI with your own)
client = pymongo.MongoClient("mongodb://myAdminUser:test123@ec2-44-202-226-165.compute-1.amazonaws.com:27017/")

# Connect to a specific database (replace 'mydatabase' with your database name)
db = client["pythonappdb"]

# Connect to a specific collection in the database (replace 'mycollection' with your collection name)
collection = db["user_info"]

@app.route("/", methods=['GET', 'POST'])
def where_are_you_from():
    if request.method == 'POST':
        name = request.form['name']
        hometown = request.form['hometown']

        try:
            user_info = {
                "name": name,
                "hometown": hometown
            }
            collection.insert_one(user_info)
            return render_template('index.html', name=name, hometown=hometown)

        except pymongo.errors.PyMongoError as e:
            print("Error saving data to MongoDB: %s" % e)
            return render_template('index.html', error="An error occurred while saving your data. Please try again.")

    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)  # Listen on port 80
