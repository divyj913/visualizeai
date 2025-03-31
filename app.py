from flask import Flask, render_template, request, redirect, url_for, session, flash
from google import genai
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")
@app.route("/about")
def about():
    return render_template("about.py")
# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
def gfg():
	if request.method == "POST":
		# getting input with query from  HTML form
		query = request.form.get("text")
		client = genai.Client(api_key="AIzaSyCNh3EOg-j1awvkPHBD5oNl9J0nRjfeDEY")
		response = client.models.generate_content(
		    model="gemini-2.0-flash", contents="Can you help me visualise"+query+"dont use any bold or italic text and keep it under 60 words", 
		)
		response_text = response.text
		#print(response.text)
	return render_template("index.html", response_text=response.text)

if __name__ == "__main__":
    app.run(debug=True)
    
