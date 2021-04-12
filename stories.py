"""Madlibs Stories."""


class Story:
    """Madlibs story.

    # I didn't read this starter code very carefully and 
    # accidentally rewrote generate() in app.py write_story()
    # To  make a story, pass a list of prompts, and the text
    # of the template.

    #     >>> s = Story(["noun", "verb"],
    #     ...     "I love to {verb} a good {noun}.")

    # To generate text from a story, pass in a dictionary-like thing
    # of {prompt: answer, promp:answer):

    #     >>> ans = {"verb": "eat", "noun": "mango"}
    #     >>> s.generate(ans)
    #     'I love to eat a good mango.'
    """

    def __init__(self, words, text, title=""):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text
        self.title = title

    # def generate(self, answers):
    #     """Substitute answers into text."""

    #     text = self.template

    #     for (key, val) in answers.items():
    #         text = text.replace("{" + key + "}", val)

    #     return text


# Here's a story to get you started
# that refers to the first one, subsequent stories written by Tor
storylist = [
    (["place", "noun", "verb", "adjective", "plural_noun"], 
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}.""" 
    ), 
    (['proper_name', 'noun', 'adjective', 'day_of_week', 'place', 'game', 'adverb', 'past_tense_verb', 'plural_noun', 'beverage'], 
    """{proper_name} was a {noun} and they was very, very sad because they didn't have any friends. Or not any they could think of right now. On one particularly {adjective} {day_of_week}, {proper_name} decided it was past time to make a friend, so of {pronoun} went to the {place} for a game of {game}. Everyone had said that was the best way to make new friends. It was a very {adverb} round of {game} and everyone {verb}ed a lot. {pronoun.capitalize()} did meet a lot of interesting {plural_noun}, but at the end of the game, no one wanted to go to the {place} with {proper_name} for a {beverage}. And so the lonely {noun} went home, even lonlier than before.""", 
    "The Lonliest {noun.capitalize()}"
    ),
    (['adverb', 'adjective', 'day_of_week', 'proper_noun', 'verb', 'place', 'adjective_', 'animal', 'verb', 'noun', 'noun_'], 
    """On a {adverb} {adjective} {day_of_week}, {proper_noun} was {verb}ing their way to the {place}. When they got there, they were very {adjective_} to find a {animal} there, and even more surprised when the {animal} {verb}ed a {noun} right off the {noun_}. """, 
    "The {adjective__} Day"
    )]