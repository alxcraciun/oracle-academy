import re

pattern = r"!\[Untitled\]\(.*?\)"

# Load the file into a string
with open("46_Questions.md", "r") as f:
    text = f.read()

# Remove all occurrences of the pattern
for i in range(67, 100):
    text = re.sub(pattern, fr"![Image-{i}](.\\assets\\Image-{i}.png)" + "\n\n<br>", text, count = 1)

# Write the modified text back to the file
with open("46_Questions.md", "w") as f:
    f.write(text)