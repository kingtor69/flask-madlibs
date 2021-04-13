from flask import Flask, request, render_template
from random import randint, choice, sample
from flask_debugtoolbar import DebugToolbarExtension
from stories import storylist
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
	chosen_story = None
	chosen_title = request.args["story"]
	if chosen_title == "random":
		story_dic = choice(storylist)
		for key in story_dic:
			chosen_title = key
			chosen_story = story_dic[key]
	else:
		for story in storylist:
			if chosen_title in story:
				chosen_story = story[chosen_title]

	if not chosen_story:
		return render_template("error.html", error = "never chose a story in get_words.", chosen_story = chosen_story, chosen_title = chosen_title, kicker = "stupid snake language")				
			
	prompts = []
	for prompt in chosen_story.prompts:
		prompts.append(prompt.replace('_', ' '))

	return render_template("get-words.html", title = chosen_title, prompts = prompts, key_prompts = chosen_story.prompts, num_of_prompts = len(prompts))

@app.route('/story')
def write_story():
	"""takes input from querystring and 'writes' the story by inserting the user-entered words into the story"""
	
	
	chosen_story = None
	chosen_title = request.args["key"]
	for story in storylist:
		if chosen_title in story:
			chosen_story = story[chosen_title]
			answers = {}
			for query in request.args:
				answers[query] = request.args[query]
			title_story = chosen_story.generate(answers)
			return render_template("story.html", title = title_story[0], finished_story = title_story[1])
	
	return render_template("error.html", error = "couldn't find the story in write_story.", chosen_story = chosen_story, chosen_title = chosen_title, kicker = "dangit!")
		
	



