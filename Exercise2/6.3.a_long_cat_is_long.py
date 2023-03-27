import re


# Accepts text as a parameter, and returns a dictionary of the word lengths in it.
# The key is the word and the value is its length.
def count_words(text1):
    # To clear the text of non-letter characters
    new_text = [re.compile('[^a-zA-Z]').sub('', word.lower()) for word in re.split('[,. \n?:!@#$%^&*()_+<>"=-]', text1)]
    list(dict.fromkeys(new_text))
    count = {word: len(word) for word in new_text if len(word) > 0}
    return count


text = """
You see, wire telegraph is a kind of a very, very long cat.
You pull his tail in New York and his head is meowing in Los Angeles.
Do you understand this?
And radio operates exactly the same way: you send signals here, they receive them there.
The only difference is that there is no cat.
"""

text2 = """
k8s for l1ife, for mone$$y and 4 style&life
"""
print(count_words(text))
