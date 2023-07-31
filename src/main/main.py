import openai
import NewYorkTimes
import mysql.connector
from ApiKeys import ApiKeys
openai.organization = ApiKeys.openAiOrg
openai.api_key = ApiKeys.openAiApiKey

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

technology_articles = NewYorkTimes.NewYorkTimes(type="latestArticles", section="technology")
health_articles = NewYorkTimes.NewYorkTimes(type="latestArticles", section="health")
opinion_articles = NewYorkTimes.NewYorkTimes(type="latestArticles", section="opinion")
politics_articles = NewYorkTimes.NewYorkTimes(type="latestArticles", section="politics")
sports_articles = NewYorkTimes.NewYorkTimes(type="latestArticles", section="sports")
world_articles = NewYorkTimes.NewYorkTimes(type="latestArticles", section="technology")

# 2) Tell chatGPT that it is an expert in social media and especially instagram and twitter.
# 3) Feed them all in chatGPT and ask it to select the 4 most suceptible to work on social media (don't tell me why)

technology_articles.getRelevant
health_articles.getRelevant
opinion_articles.getRelevant
politics_articles.getRelevant
sports_articles.getRelevant
world_articles.getRelevant

# 4) Tell chatGPT that it is a journalist on social media that loves provocating and writing about the news in an ironic way.
# It should also always finish its articles with a joke. The articles should be around 45 words long.
# 5) With the output from the previous request, filter and give chatGPT the pair title/content and ask it to rewrite them

technology_articles.writeTitles
health_articles.writeTitles
opinion_articles.writeTitles
politics_articles.writeTitles
sports_articles.writeTitles
world_articles.writeTitles

technology_articles.writeContents
health_articles.writeContents
opinion_articles.writeContents
politics_articles.writeContents
sports_articles.writeContents
world_articles.writeContents

#6) Send it to the database
mydb = mysql.connector.connect(
  host="www.db4free.net",
  user="topsecret",
  password=ApiKeys.databasePassword,
  database="topsecret"
)

mycursor = mydb.cursor()

def sendToDatabase(articles):
    for i in range(len(articles.newTitle)):
        sql = "INSERT INTO posts (newTitle, newContent, oldTitle, oldContent, url, image)" 
        + "VALUES ('{newTitle}', '{newContent}', '{oldTitle}', '{oldContent}', '{url}', 'n/a')".format(
            articles.newTitles[i], articles.newContents[i], articles.oldTitles[i], articles.oldContents[i], articles.url[i]
            )
        mycursor.execute(sql)

mydb.commit()
print(mycursor.rowcount, "record inserted.")
