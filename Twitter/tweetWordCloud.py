'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob
from wordcloud import WordCloud
import matplotlib.pyplot as plt

#Get the JSON data
tweetFile = open("twitterData.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# Continue your program below!

string = ""

for i in tweetData:
    string += i["text"]

stringBlob = TextBlob(string)


wordCount = {}
wordList = stringBlob.words


for i in wordList:
    wordCount[i] = stringBlob.word_counts[i]+1

wordcloud = WordCloud().generate(string)
plt.figure()
plt.imshow(wordcloud, interpolation = "bilinear")
plt.axis("off")
plt.show()
