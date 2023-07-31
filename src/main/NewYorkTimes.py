from pynytimes import NYTAPI
import openai
from ApiKeys import ApiKeys
nyt = NYTAPI(ApiKeys.nytApiKey, parse_dates=True)
openai.organization = ApiKeys.openAiOrg
openai.api_key = ApiKeys.openAiApiKey

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
   self.relevant_indices = []

   self.newTitles = []
   self.newContents = []
   self.oldTitles = []
   self.oldContents = []
   self.urls = []

   self.system_msg = "You are an expert in social media running a newspaper. Your goal is to generate as much interactions as possible." 
   + "You like to be controversial and have a strong sense of humor."

   for article in self.parsed:
      self.titles.append(article['title'])
      self.contents.append(article['abstract'])

   def getRelevant(self):
      titles_list = []
      index = 0
      for title in self.titles:
         titles_list.append(str(index)+ ": " + title)
         index += 1
      user_msg = "Your team of journalists came up with the following ideas of titles. Each title as an index from 0 to " + len(titles_list) 
      + ". Give me the indices of the 4 titles most suceptible to generate a lot of reactions on social media. Don't give me a reason why," 
      + "simply answer with the 4 indexes in the following format: w,x,y,z." + titles_list

      response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                          messages=[{"role": "system", "content": self.system_msg},
                                          {"role": "user", "content": user_msg}])
      
      self.relevant_indices = response.split(",")
      for i in self.relevant_indices:
         i = int(i)
      return self.relevant_indices        #This needs to be of the form: [1,2,4,8,13]
   
   def writeTitles(self):
      user_msg = "Rewrite the following title in an ironic way that will catch people off guard."
      index = 0
      for title in self.titles:
         if index in self.relevant_indices:
            response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                          messages=[{"role": "system", "content": self.system_msg},
                                          {"role": "user", "content": user_msg+title}])
            self.oldTitles.append(title)
            self.newTitles.append(response)
            self.urls.append(self.parsed[index]['url'])
         index += 1
      
   def writeContents(self):
      user_msg = "Rewrite the following text in an ironic way. The paragraph should be around 45 words long and you should finish it with a joke or a question"
      index = 0
      for content in self.contents:
         if index in self.relevant_indices:
            response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                          messages=[{"role": "system", "content": self.system_msg},
                                          {"role": "user", "content": user_msg+content}])
            self.oldContents.append(content)
            self.newContents.append(response)
         index += 1

   
      
            





