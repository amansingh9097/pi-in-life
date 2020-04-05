from flask import Flask
import json
from datetime import datetime

app = Flask(__name__)

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
	<meta http-equiv="refresh" content="1" >
	<head>
		<title>Every day is a Pi day</title>
	</head>
	<body>
		<center>
			<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Pi-symbol.svg/248px-Pi-symbol.svg.png" height="150" width="150">
		<h3> Every day is a Pi day</h3>
		<p> The current date time is <b>{} GMT+5:30</b>.</p>

		<p> When the current date is parsed as DDMMYY, it's just a number <b>{}</b><br>
		and this number occurs at <b>{}</b> decimal position of Pi</p>

		<p> When the current time is parsed as HHMMSS, it's the number <b>{}</b><br>
		that occurs at <b>{}</b> decimal position of Pi</p>

		<h5>Made with ❤ by <a href="https://aman-singh.com/">Aman Singh</a></h5>
		</center>
	</body>
	</html>
	""".format(datetime.strftime(current_datetime,"%d %B, %Y %X"), current_date, current_date_pos, current_time, current_time_pos)

if __name__ == "__main__":
	app.run(debug=True)