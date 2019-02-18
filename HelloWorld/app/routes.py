from app import app

@app.route('/')			# '@app.route' is a Decorator. It modifies the function that follows it.
@app.route('/index') 	# Here, they associate the URLs / and /index to this function.

# This means that when a web browser requests either of these two URLs, Flask is going to invoke this function 
# and pass the return value of the function back to the browser as a response.

def index():
	return 'Hello World'

