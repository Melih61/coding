
text = 'YOOOOOO\nThis is some text'

# use 'a' if you want to add a text to a file or 'w' to overwrite everything in the file
with open('Write.txt','a') as file:
    file.write(text)