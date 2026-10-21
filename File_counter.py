from google.colab import files
uploaded = files.upload()

with open("counts.txt" , "r")as file:
  content = file.read()

lines = len(content.splitlines())
words = len(content.split())
characters = len(content)

print("lines : " , lines)
print("words : " , words)
print("characters : " , characters)
