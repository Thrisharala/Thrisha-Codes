#madlibs generator.

with open("story.txt","r") as f: #story file
    story = f.read()           #open the text file

words = set()                  #set for unique words
start_of_word = -1

target_start = "<"             
target_end = ">"

for i ,char in enumerate(story):             #enumerator - to iterate over a sequence while keeping track of the index
    if char == target_start:
        start_of_word = i

    if char == target_end and start_of_word != -1:
        word = story[start_of_word: i + 1]
        words.add(word)
        start_of_word = -1                   #locates all of the different words inside our story

answers = {}

for word in words:
    answer = input("Enter a word for " + word + ":")
    answers[word] = answer

for word in words:
    story = story.replace(word,answers[word])

print(story)