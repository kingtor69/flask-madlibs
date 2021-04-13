"""Madlibs Stories."""


class Story:
    """Madlibs story.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        title = self.title
        text = self.template

        for (key, val) in answers.items():
            title = title.replace("{" + key + "}", val)
            text = text.replace("{" + key + "}", val)

        return [title, text]

# Here's a story to get you started
once_upon_a_time = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a large {adjective} {noun}. It loved to {verb} {plural_noun}."""
    )

# subsequent stories and storylist written by Tor

the_lonliest = Story(
    ['proper_name', 'noun', 'adjective', 'day_of_week', 'place', 'game', 'adverb', 'past_tense_verb', 'plural_noun', 'beverage'], 
    """{proper_name} was a {noun} and they was very, very sad because they didn't have any friends. Or not any they could think of right now. On one particularly {adjective} {day_of_week}, {proper_name} decided it was past time to make a friend, so of {pronoun} went to the {place} for a game of {game}. Everyone had said that was the best way to make new friends. It was a very {adverb} round of {game} and everyone {verb}ed a lot. {pronoun.capitalize()} did meet a lot of interesting {plural_noun}, but at the end of the game, no one wanted to go to the {place} with {proper_name} for a {beverage}. And so the lonely {noun} went home, even lonlier than before."""
    )

day_in_the_life = Story(
    ['adverb', 'adjective', 'day_of_week', 'adjective__', 'proper_noun', 'verb', 'place', 'adjective_', 'animal', 'verb', 'noun', 'noun_'], 
    """On a {adverb} {adjective} {day_of_week}, {proper_noun} was {verb}ing their way to the {place}. When they got there, they were very {adjective_} to find a {animal} there, and even more surprised when the {animal} {verb}ed a {noun} right off the {noun_}. """
    )


storylist = [
    {"Once Upon a Time": once_upon_a_time},
    {"The Lonliest": the_lonliest},
    {"Day in the Life": day_in_the_life}
]