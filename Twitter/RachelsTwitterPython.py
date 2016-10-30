#sending to twitter account twitter.com/rachwhitepython

import twitter, datetime, urllib2

user = 792015373168246784 #my twitter ID
file = open("/Users/rwhite1/Desktop/Twitter/TwitterKeys.txt") #file with twitter api keys in
keys = file.read().split('\n') #reads twitter key file line by line

filename = open("/Users/rwhite1/Library/Application Support/Google/Chrome/Default/Current Session") #opens chrome history. P.S...... I haven't copied Georgia's.... I'm just using Georgia's old laptop!
websites = filename.read() #reads chrome history

timestamp = datetime.datetime.utcnow() #finds time

lastwebsite = websites.rfind("http") #searches the chrome history and finds the last entry after "http", this will be the last website visited

endIndex = websites.find(chr(0), lastwebsite) #looks for last string after binary 0, which will be the last URL visited
lastURL = websites[lastwebsite:endIndex]

response = urllib2.urlopen(lastURL)
html = response.read()
startIndex = html.find("<title>") #finds the title of the webpage 
endIndex = html.find("</title>")

htmlTitle = html[startIndex+7:endIndex]

lastwebsite2 = websites[lastwebsite:-50]
print(str(lastwebsite2)) #puts the last website viewed into a sting called lastwebsite2

api = twitter.Api(keys[0],keys[1],keys[2],keys[3]) #accesses twitter api keys

response = api.PostUpdate("I just visited " + str(htmlTitle) + ". Tweet sent at " + str(timestamp)) #sends a tweet to twitter with the text in orange and the last website visited and the time that the tweet is sent

print("Status updated to: " + response.text) #prints a message in terminal to confirm 