import sys
sys.path.insert(0, '../data_matcher')
import match_data
# insert at 1, 0 is the script path (or '' in REPL)
from flask import Flask, render_template, redirect, url_for, request, session, flash, g, make_response, send_file, send_from_directory, jsonify

app = Flask(__name__)

@app.route('/')
def interactive():
	return render_template('form.html')

@app.route('/background_process')
def background_process():
	try:
		lang = request.args.get('interests', 0, type=str)
		lst = lang.split(" ")
		return jsonify(result=get_results(lst))
	except Exception as e:
		return str(e)

def get_results(data):
    western_finder = match_data.ClubFinder("western")
    return western_finder.suggest_club(data)


if __name__ == "__main__":
	app.run()
