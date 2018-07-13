import json

f = open("twitterData.json", "r")
tweetData = json.load(f)
f.close()

# print( tweetData[0]["id"])
# print(tweetData[0]["text"])

for i in tweetData:
    print(i["id"])
    print(i["text"])
