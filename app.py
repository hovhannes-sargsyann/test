from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

# Define the 'route' (the URL path) and the function to handle it
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
