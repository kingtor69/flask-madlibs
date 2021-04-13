from flask import Flask, request, render_template
from random import randint, choice, sample
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story, storylist, make_story_from_class
# import stories

app = Flask(__name__)
app.config['SECRET_KEY'] = "thecheddarthebetter1969"

debug = DebugToolbarExtension(app)

@app.route('/')
def pick_story():
	titles = []
	for story in storylist:
	# for story in stories.storylist:
		for key in story:
			titles.append(key)

	return render_template("pick-story.html", titles = titles)

@app.route('/get-words')
def get_words():
	"""prepare prompts and return homepage"""
	chosen_title = request.args["story"]
	# chosen_story = stories.make_story_from_class(chosen_title)
	chosen_story = make_story_from_class(chosen_title)
	prompts = []
	for prompt in chosen_story.prompts:
		prompts.append(prompt.replace('_', ' '))

	return render_template("get-words.html", story = chosen_story, prompts = prompts, key_prompts = chosen_story.prompts, num_of_prompts = len(prompts))

@app.route('/story')
def write_story():
	"""takes input from querystring and 'writes' the story by inserting the user-entered words into the story"""
	# from stories import chosen_story
	# getattr(wtf_object, request.args['key'])
	finished_story = chosen_story.generate(answers)

	return render_template("story.html", finished_story = finished_story)


