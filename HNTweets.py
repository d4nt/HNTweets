import urllib
import sqlite3
import datetime
import tweepy
from xml.dom.minidom import parseString
from settings import *

class Item:
	title = ""
	link = ""

class CustomUrlOpener(urllib.FancyURLopener):
	version = "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/25.0"

def getFeedData():
	urllib._urlopener = CustomUrlOpener()
	feedRequest = urllib.urlopen(HACKER_NEWS_RSS_URL)
	feedString = feedRequest.read()
	feedRequest.close()
	return parseString(feedString)

def iterateItems(feedData):
	results = []
	for element in feedData.getElementsByTagName("item"):
		item = Item()
		item.title = element.getElementsByTagName("title")[0].childNodes[0].data
		item.link = element.getElementsByTagName("link")[0].childNodes[0].data
		item.commentLink = element.getElementsByTagName("comments")[0].childNodes[0].data
		results.append(item)
	return results

def isSchemaThere(conn):
	cur = conn.cursor()
	cur.execute("SELECT name FROM sqlite_master WHERE name='links'")
	if len(cur.fetchall()) > 0:
		return True
	return False

def createSchema(conn):
	cur = conn.cursor()
	cur.execute("CREATE TABLE links (title text, url text, first_seen datetime)")
	
def isNewLink(item):
	conn = sqlite3.connect(LOCAL_LINK_DB)
	if isSchemaThere(conn) == False:
		createSchema(conn)
	cur = conn.cursor()
	cur.execute("SELECT url FROM links WHERE url=?", (item.link,))
	isNew = len(cur.fetchall()) == 0
	conn.commit()
	conn.close()
	return isNew

def insertLink(item):	
	conn = sqlite3.connect(LOCAL_LINK_DB)
	cur = conn.cursor()
	cur.execute("INSERT INTO links VALUES (?, ?, datetime('now'))", (item.title, item.link,))
	conn.commit()
	conn.close()

def fixCommentLink(link):
    protocolEnd = 0
    if "//" in link:
        protocolEnd = link.index("//") + len("//")
        return "https://" + link[protocolEnd:]
    else:
        return "https://" + link.lstrip("/")

def getTweetText(item):
	maxTitleTextLength = TWITTER_MAX - (TCO_SHORT_URL_LENGTH + len(DIVIDER_TEXT))
	if item.link <> item.commentLink:
		maxTitleTextLength -= (len(COMMENT_TEXT) + TCO_SHORT_URL_LENGTH)
	tweetText = item.title.strip(" .,:;!?")[:maxTitleTextLength] + DIVIDER_TEXT + item.link
	if item.link <> item.commentLink:
		tweetText += COMMENT_TEXT + fixCommentLink(item.commentLink)
	return tweetText

def submitTweet(tweetText):
	if DEBUG_MODE == False:
		auth = tweepy.OAuthHandler(TWITTER_CUSTOMER_KEY, TWITTER_CUSTOMER_SECRET)
		auth.set_access_token(TWITTER_OAUTH_KEY, TWITTER_OAUTH_SECRET)
		api = tweepy.API(auth)
		api.update_status(tweetText)
	else:
		print tweetText

for item in iterateItems(getFeedData()):
	if isNewLink(item):
		insertLink(item)
		tweetText = getTweetText(item)
		submitTweet(tweetText)
