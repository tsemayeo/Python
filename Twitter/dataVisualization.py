'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt

#Get the JSON data
tweetFile = open("twitterData.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# Continue your program below!

polar = []

subject = []

polarTotal = 0

subjectTotal = 0

for i in tweetData:
    tb = TextBlob(i["text"])

    polar.append(tb.polarity)
    polarTotal += tb.polarity

    subject.append(tb.subjectivity)
    subjectTotal += tb.subjectivity



plt.hist(polar, bins = [-0.5, 0, 0.5, 1])
plt.title("Polarity Histogram")
plt.xlabel("Polarity")
plt.ylabel("Frequency")
plt.BarWidth = 0.4
plt.gcf()
plt.show()

plt.hist(subject, bins = [ 0, 0.2, 0.4, 0.6, 0.8, 1])
plt.title("Subjectivity Histogram")
plt.xlabel("Subjectivity")
plt.ylabel("Frequency")
plt.BarWidth = 0.4
plt.gcf()
plt.show()

length = len(polar)
print("polarity: ", polarTotal/length)
print("subjectivity: ", subjectTotal/length)
