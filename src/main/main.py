import openai
import NewYorkTimes
import mysql.connector
from ApiKeys import ApiKeys
openai.organization = ApiKeys.openAiOrg
openai.api_key = ApiKeys.openAiApiKey
import time

"""
1) Get the articles from the ny times
2) Tell chatGPT that it is an expert in social media and especially instagram and twitter.
3) Feed them all in chatGPT and ask it to select the 4 most suceptible to work on social media (don't tell me why)
4) Tell chatGPT that it is a journalist on social media that loves provocating and writing about the news in an ironic way.
It should also always finish its articles with a joke. The articles should be around 45 words long.
5) With the output from the previous request, filter and give chatGPT the pair title/content and ask it to rewrite them
6) Send it to the database.

arts, automobiles, books, business, fashion, food, health, home, insider, magazine, movies, national, nyregion, 
obituaries, opinion, politics, realestate, science, sports, sundayreview, 
technology, theater, tmagazine, travel, upshot, and world
"""


# 1) Get the articles from the ny times
# We will start by getting the latest articles for technology, health, opinion, politics, sports and world.

print("Creating the NewYorkTimes objects...")
# technology_articles = NewYorkTimes.NewYorkTimes(type="latestArticles", section="technology")
# health_articles = NewYorkTimes.NewYorkTimes(type="latestArticles", section="health")
# opinion_articles = NewYorkTimes.NewYorkTimes(type="latestArticles", section="opinion")
# politics_articles = NewYorkTimes.NewYorkTimes(type="latestArticles", section="politics")
# sports_articles = NewYorkTimes.NewYorkTimes(type="latestArticles", section="sports")
# world_articles = NewYorkTimes.NewYorkTimes(type="latestArticles", section="world")
print("Creatin done!")

# 2) Tell chatGPT that it is an expert in social media and especially instagram and twitter.
# 3) Feed them all in chatGPT and ask it to select the 4 most suceptible to work on social media (don't tell me why)

print("Getting Relevant indices...")
# technology_articles.getRelevant()
# health_articles.getRelevant()
# opinion_articles.getRelevant()
# politics_articles.getRelevant()
# sports_articles.getRelevant()
# world_articles.getRelevant()
print("We got the indices!")

# 4) Tell chatGPT that it is a journalist on social media that loves provocating and writing about the news in an ironic way.
# It should also always finish its articles with a joke. The articles should be around 45 words long.
# 5) With the output from the previous request, filter and give chatGPT the pair title/content and ask it to rewrite them

print("Writing Titles...")
# technology_articles.writeTitles()
# health_articles.writeTitles()
# opinion_articles.writeTitles()
# politics_articles.writeTitles()
# sports_articles.writeTitles()
# world_articles.writeTitles()
print("Titles written!")

print("Writting the content...")
# technology_articles.writeContents()
# health_articles.writeContents()
# opinion_articles.writeContents()
# politics_articles.writeContents()
# sports_articles.writeContents()
# world_articles.writeContents()
print("Content written!")


#6) Send it to the database
mydb = mysql.connector.connect(
  host="www.db4free.net",
  user="topsecret",
  password=ApiKeys.databasePassword,
  database="topsecret"
)

mycursor = mydb.cursor()

print("Database now...")

def formatString(text):
   text = text.replace("'", "''")
   return text

def sendToDatabase(articles):
    for i in range(len(articles.newTitles)):
        sql = "INSERT INTO posts (`newTitle`, `newContent`, `oldTitle`, `oldContent`, `url`, `image`) VALUES ('{newTitle}', '{newContent}', '{oldTitle}', '{oldContent}', '{url}', 'n/a')".format(
            newTitle = formatString(articles.newTitles[i]), newContent = formatString(articles.newContents[i]), oldTitle = formatString(articles.oldTitles[i]), oldContent = formatString(articles.oldContents[i]), url = formatString(articles.urls[i])
            )
        mycursor.execute(sql)
    mydb.commit()

# sendToDatabase(technology_articles)
# sendToDatabase(health_articles)
# sendToDatabase(opinion_articles)
# sendToDatabase(politics_articles)
# sendToDatabase(sports_articles)
# sendToDatabase(world_articles)


test_main = NewYorkTimes.NewYorkTimes(type="mostViewed", days=7)

def main(nytArticles):
    print("Hey1")
    nytArticles.getRelevant()
    print("Hey2")
    nytArticles.writeTitles()
    print("Hey3")
    nytArticles.writeContents()
    print("Hey4")
    sendToDatabase(nytArticles)
    print("DONE")

main(test_main)