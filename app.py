import os
from flask import Flask, request, render_template # Retrieve Flask, our framework
import requests

app = Flask(__name__)   # create our flask app

# this is our main page
@app.route("/")
def index():

	# fetch Ideas JSON
	ideas = requests.get('http://itp-ideas-dwd.herokuapp.com/data/ideas')
	
	# get ideas from JSON
	itpIdeas = ideas.json().get('ideas')
	
	# log out the content of the request
	app.logger.debug(itpIdeas)
	
	# prepare template data
	templateData = {
		'ideas' : itpIdeas
	}
	
	return render_template("index.html", **templateData)


# start the webserver
if __name__ == "__main__":
	app.debug = True
	
	port = int(os.environ.get('PORT', 5000)) # locally PORT 5000, Heroku will assign its own port
	app.run(host='0.0.0.0', port=port)