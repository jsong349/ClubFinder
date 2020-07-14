import sys
sys.path.insert(0, '../data_matcher')
import match_data
import json
# insert at 1, 0 is the script path (or '' in REPL)
from flask import Flask, render_template, redirect, url_for, request, session, flash, g, make_response, send_file, send_from_directory, jsonify

app = Flask(__name__)


with open('../data/org_data_full_western.json', 'r') as j:
	contents = json.loads(j.read())


@app.route('/')
def interactive():
	return render_template('form.html')

@app.route('/background_process')
def background_process():
	print('starting')
	try:
		lang = request.args.get('interests', 0, type=str)
		lst = lang.split(" ")
		res = get_results(lst)
		print(res)
		to_send = []
		for club in res:
			to_send.append(contents[club[0]])
		print(to_send)
		return jsonify(result=to_send)
	except Exception as e:
		print(str(e))

def get_results(data):
    western_finder = match_data.ClubFinder("western")
    return western_finder.suggest_club(data)


if __name__ == "__main__":
	app.run()
