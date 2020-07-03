from flask import Flask, request
from flask import render_template, redirect, url_for
import os

# creates a Flask application, named app
app = Flask(__name__)

UPLOAD_FOLDER = "/tmp/"


# a route where we will display a welcome message via an HTML template
@app.route("/home")
def hello():
    message = "Hello, World"
    return render_template('audio.html')

@app.route("/upload", methods= ['POST', 'GET'])
def upload():
	if request.method == "POST":
		print(request)
		print(request.files["audio"])
		file = request.files["audio"]
		file.save(os.path.join(UPLOAD_FOLDER, file.filename + ".wav"))
		return redirect('/textfromaudio')
	else:
		print("Something")
		message = getText()
		print(message)
		return render_template("transcript.html", message=message)
		

@app.route("/textfromaudio", methods = ['GET'])
def textfromaudio():
	# Run your function to get the text here
	print("Something")
	message = getText()
	print(message)
	return render_template("transcript.html", message=message)

@app.route("/sendtranscript", methods = ['POST'])
def sendtranscript():
	print(request.form)
	return formthing(request.form)

@app.route("/storefinal", methods = ['POST'])
def storefinal():
	print(request.form)

	# Whatever data storing ya wanna do, request.form gives you the form data as a dict
	f = open(UPLOAD_FOLDER+"result.txt", 'w')
	f.write("Hello there")
	f.write(request.form["first"])
	f.write(request.fomr["second"])
	f.close()

	return render_template('datastored.html')

@app.route("/formthingy", methods = ['GET'])
def formthing(dummy):
	# Function here to convert that transcript into whatever form details
	formData = getStuff(dummy)
	return render_template("formthingy.html", data=formData)

def getText():
	# This is the part that gets the text from the audio
	return "This is the transcript. That is the audio test."

def getStuff(dummy):
	return {'first':dummy["transcript"], 'second':dummy["transcript"].lower()}


# run the application
if __name__ == "__main__":
    app.run(debug=True)
