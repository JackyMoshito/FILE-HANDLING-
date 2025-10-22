with open("text1.txt", "r") as file:
    lines = file.readlines()
    line_count = len(lines)
    content = "".join(lines)

word_count = len(content.split())
print("Lines:", line_count)
print("Words:", word_count)
print("Characters:", len(content))