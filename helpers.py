def make_story_from_class(chosen_key):
    for story in storylist:
        if story.get(chosen_key):
            chosen_story = story[chosen_key]
    return Story(chosen_story)