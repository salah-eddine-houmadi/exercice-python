import re
text = "The quick brown fox jumps over the lazy dog fox."

new_text = re.sub("fox", "cat", text)
print("New text:", new_text)