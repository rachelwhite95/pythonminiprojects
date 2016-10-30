import wikipedia 

wordList = open("stopwords.txt")
wordListContent = wordList.read()
wordListUnderstood = wordListContent.split("\n")

name = raw_input ("Oh hey there. What is your name?\n") 
response = raw_input ("Nice to meet you " + name + ". How are you today?\n")
userResponseList = response.split(" ")
filteredList = []

for eachWord in userResponseList: 
    if (eachWord not in wordListUnderstood):
        filteredList.append(eachWord)

goodMood = ["happy", "good", "great"]
badMood = ["sad", "bad"]

for anyWord in filteredList:
    if (anyWord in goodMood):
        print("That's good to hear, " + name + ".")
    elif (anyWord in badMood):
        print("Oh no. That's not good," + name + ".") 
        
response = raw_input("What do you want to talk about?\n")
wikiSearch = wikipedia.search(response, results = 10)

x = 0
for answers in range(len(wikiSearch)):
    yesNo = raw_input("Would you like me to tell you a little bit about " + wikiSearch[x] + "?\n" )
    if (yesNo == "yes"):
        info = wikipedia.summary(wikiSearch[x], sentences = 3)
        print (info)
        break
    x = x + 1
    if (yesNo == "no"):
        respone = raw_input("Oh okay. Did you mean " + wikiSearch[x] + "? ")        
        if (yesNo == "yes"):
            info = wikipedia.summary(wikiSearch[x], sentences = 3)
            print (info)
            break
        if (yesNo == "no"):
            response = raw_input("Well I don't know then! Do you want to change the subject? ")
            if (yesNo == "yes"):
                response = raw_input("What do you want to change the subject to? ")
                wikiSearch = wikipedia.search(response, results = 10)
                x = 1
            if (yesNo == "no"):
                print "Okay, sorry I dont know everything."