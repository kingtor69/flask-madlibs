from random import choice
from stories import storylist, Story

def pick_random_story():
	return Story(choice(storylist))