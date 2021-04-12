from flask import Flask, request, render_template
from random import randint, choice, sample
from flask_debugtoolbar import DebugToolbarExtension
from stories import *

app = Flask(__name__)
app.config['SECRET_KEY'] = "thecheddarthebetter1969"

debug = DebugToolbarExtension(app)

@app.route('/')
def get_words():
	"""prepare prompts and return homepage"""
	prompts = []
	for prompt in story.prompts:
		prompts.append(prompt.replace('_', ' '))

	return render_template("get-words.html", prompts = prompts, key_prompts = story.prompts, num_of_prompts = len(prompts))

@app.route('/story')
def write_story():
	"""takes input from querystring and 'writes' the story by inserting the user-entered words into the story"""
	key = ""
	finished_story = ""
	in_curlies = False
	for char in story.template:
		if in_curlies == True:
			if char == "}":
				finished_story += request.args[key]
				key = ""
				in_curlies = False
			else:
				key += char
		elif char == "{":
			in_curlies = True
		else:
			finished_story += char


	return render_template("story.html", finished_story = finished_story)


# story = Story(
#     ["place", "noun", "verb", "adjective", "plural_noun"],
#     """Once upon a time in a long-ago {place}, there lived a
#        large {adjective} {noun}. It loved to {verb} {plural_noun}."""
# )