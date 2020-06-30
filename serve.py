from flask import Flask, request
from flask import render_template
import os

# creates a Flask application, named app
app = Flask(__name__)

UPLOAD_FOLDER = "/tmp/"

# a route where we will display a welcome message via an HTML template
@app.route("/")
def hello():
    message = "Hello, World"
    return render_template('audio.html')

@app.route("/upload", methods= ['POST'])
def upload():
	print(request)
	print(request.files["audio"])
	file = request.files["audio"]
	file.save(os.path.join(UPLOAD_FOLDER, file.filename + ".wav"))
	return "<h1> okay </h1>"

# run the application
if __name__ == "__main__":
    app.run(debug=True)
