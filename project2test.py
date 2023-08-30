with open("story.txt","r") as f :
    story = f.read()



start_index = -1

start_anb = "<"
end_anb   = ">"
words = set()

for i  ,char in enumerate(story):

  if char == start_anb:
     start_index = i
  if char == end_anb and start_index != -1 :
     word = story[start_index: i+1]
     words.add(word)

answers = {}

for word in words:
   answer = input("enter a word for " +word+ " :")
   answers[word] = answer  

for word in words:
 story = story.replace(word,answers[word])


print(story)
