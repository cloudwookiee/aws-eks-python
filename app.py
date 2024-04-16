from flask import Flask, render_template, request
import pymongo

# ... (rest of your imports) 

# MongoDB Connection 
try:
    client = pymongo.MongoClient("mongodb://ec2-44-202-226-165.compute-1.amazonaws.com:27017/")  # Replace with your connection string 
    db = client["pythonappdb"] 
    collection = db["user_data"]
except pymongo.errors.ConnectionFailure as e:
    print("Could not connect to MongoDB: %s" % e)

# ... (your route definition)

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
    app.run(debug=True, host="0.0.0.0")
