from flask import Flask
from flask_frozen import Freezer
import json
from datetime import datetime

app = Flask(__name__)
freezer = Freezer(app)

@app.route("/", methods=["GET"])
def home():
	with open('pi.json') as f:
  		data = json.load(f)
	current_datetime = datetime.now()
	current_date = datetime.strftime(current_datetime, "%d%m%y")
	current_time = datetime.strftime(current_datetime, "%H%M%S")
	current_date_pos = data['pi'].find(current_date)
	current_time_pos = data['pi'].find(current_time)

	return """
	
	<head>
		<title>A part of π is in our everyday life</title>
	</head>
	<body>
		<center>
			<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Pi-symbol.svg/248px-Pi-symbol.svg.png" height="150" width="150">
		<h3> A part of π is in our everyday life.</h3>
		<p> The current date time is <b>{} GMT+5:30</b>.</p>

		<p> When the current date is parsed as DDMMYY, it's just a number <b>{}</b><br>
		and this number occurs at <b>{}</b> decimal position in Pi</p>

		<p> When the current time is parsed as HHMMSS, it's the number <b>{}</b><br>
		that occurs at <b>{}</b> decimal position in Pi</p>

		<h5>Made with ❤ by <a href="https://aman-singh.com/">Aman Singh</a></h5>
		</center>
	</body>
	</html>
	""".format(datetime.strftime(current_datetime,"%d %B, %Y %X"), current_date, current_date_pos, current_time, current_time_pos)

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000, debug=True)
	freezer.freeze()
