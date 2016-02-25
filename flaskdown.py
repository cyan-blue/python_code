# Browse the /download route to see it in action

from flask import Flask, make_response

# Initialize the Flask application
app = Flask(__name__)

# This route will just print some csv lines
@app.route('/')
def index():
    csv = """dsafsdfasdfsdaf"""
    return csv

# This route will prompt a file download with the csv lines
@app.route('/download')
def download():
    csv = """fsadfasdfdasfdsafdasfsdafdfasfdfdasdf"""
    # We need to modify the response, so the first thing we 
    # need to do is create a response out of the CSV string
    response = make_response(csv)
    # This is the key: Set the right header for the response
    # to be downloaded, instead of just printed on the browser
    response.headers["Content-Disposition"] = "attachment; filename=upgrade.lua"
    return response

if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=int("9000"),
        debug=True
    )
