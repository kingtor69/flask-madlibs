from flask import Flask, request, render_template
from random import randint, choice, sample
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

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

	answers = {}
	for query in request.args:
		answers[query] = request.args[query]
	finished_story = story.generate(answers)

	return render_template("story.html", finished_story = finished_story)


# story = Story(
#     ["place", "noun", "verb", "adjective", "plural_noun"],
#     """Once upon a time in a long-ago {place}, there lived a
#        large {adjective} {noun}. It loved to {verb} {plural_noun}."""
# )