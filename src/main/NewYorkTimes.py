from pynytimes import NYTAPI
from ApiKeys import ApiKeys
nyt = NYTAPI(ApiKeys.nytApiKey, parse_dates=True)

class NewYorkTimes:
  def __init__(self, type, section=None, days=7, method="facebook", source="all"):
    if type == "topStories": 
      if section:
         self.parsed = nyt.top_stories(section)
      else:
         self.parsed = nyt.top_stories()
    elif type == "mostViewed":
       self.parsed = nyt.most_viewed(days)
    elif type == "mostShared":
       self.parsed = nyt.most_shared(days, method)          # method is facebook or email.
    elif type == "latestArticles":
       self.parsed == nyt.latest_articles(source, section)
    else:
       raise Exception("type can only be: topStories, mostViewed, mostShared or latestArticles.")
    
    self.titles = []
    self.contents = []

    for article in self.parsed:
        self.titles.append(article['title'])
        self.contents.append(article['abstract'])