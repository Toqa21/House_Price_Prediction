# Import necessary modules
from flask import Flask, render_template, request
import pickle

# Create a Flask web application instance
app = Flask(__name__)

# Load your machine learning model from a saved file
model = pickle.load(open("trained_model.sav", "rb"))

# Define a route for the root URL ("/") that handles both GET and POST requests
@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None  # Initialize the prediction variable

    # Check if the incoming request is a POST request (form submission)
    if request.method == "POST":
        input_values = []  # Initialize a list to store input values
        for i in range(1, 42):  # Loop through input fields (assuming 41 fields)
            field_name = f"input{i}"  # Generate the input field name dynamically
            if field_name in request.form:
                input_values.append(float(request.form[field_name]))  # Extract and convert input value to float
            else:
                input_values.append(0.0)  # If the field is missing, default to 0.0

        # Make a prediction using the loaded machine learning model
        prediction = model.predict([input_values])[0]

    # Render the HTML template "index.html" and pass the prediction as a variable
    return render_template("index.html", prediction=prediction)

# Start the Flask application if this script is executed directly
if __name__ == "__main__":
    app.run(debug=True)  # Run the app in debug mode for development