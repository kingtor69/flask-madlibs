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


# Here's a story to get you started
# that refers to the first one, except I added the title
# subsequent stories written by Tor
storylist = [
    (["place", "noun", "verb", "adjective", "plural_noun"], 
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}.""", "Once Upon a Time" 
    ), 
    (['proper_name', 'noun', 'adjective', 'day_of_week', 'place', 'game', 'adverb', 'past_tense_verb', 'plural_noun', 'beverage'], 
    """{proper_name} was a {noun} and they was very, very sad because they didn't have any friends. Or not any they could think of right now. On one particularly {adjective} {day_of_week}, {proper_name} decided it was past time to make a friend, so of {pronoun} went to the {place} for a game of {game}. Everyone had said that was the best way to make new friends. It was a very {adverb} round of {game} and everyone {verb}ed a lot. {pronoun.capitalize()} did meet a lot of interesting {plural_noun}, but at the end of the game, no one wanted to go to the {place} with {proper_name} for a {beverage}. And so the lonely {noun} went home, even lonlier than before.""", 
    "The Lonliest {noun.capitalize()}"
    ),
    (['adverb', 'adjective', 'day_of_week', 'adjective__', 'proper_noun', 'verb', 'place', 'adjective_', 'animal', 'verb', 'noun', 'noun_'], 
    """On a {adverb} {adjective} {day_of_week}, {proper_noun} was {verb}ing their way to the {place}. When they got there, they were very {adjective_} to find a {animal} there, and even more surprised when the {animal} {verb}ed a {noun} right off the {noun_}. """, 
    "The {adjective__} Day"
    )]