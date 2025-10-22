import os

if os.path.exists("diary.txt"):
    print("File exists")
else:
    print("File not found!")