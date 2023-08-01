from pynytimes import NYTAPI
import openai
from ApiKeys import ApiKeys
nyt = NYTAPI(ApiKeys.nytApiKey, parse_dates=True)
openai.organization = ApiKeys.openAiOrg
openai.api_key = ApiKeys.openAiApiKey

def arrayToString(array):
    res = ""
    for el in array:
        res += el
    return res

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
         self.parsed = nyt.latest_articles(source, section)
      else:
         raise Exception("type can only be: topStories, mostViewed, mostShared or latestArticles.")
         
      self.titles = []
      self.contents = []
      self.relevant_indices = []

      self.topic = source

      self.newTitles = []
      self.newContents = []
      self.oldTitles = []
      self.oldContents = []
      self.urls = []

      self.system_msg = "You are an expert in social media running a newspaper. Your goal is to generate as much interactions as possible. You like to be controversial and have a strong sense of humor."

      for article in self.parsed:
         if (article['abstract'] != ''):
            self.titles.append(article['title'])
            self.contents.append(article['abstract'])

   def getRelevant(self):
      titles_list = []
      index = 0
      for title in self.titles:
         titles_list.append(str(index)+ ": " + title)
         index += 1
      length = str(len(titles_list))
      user_msg = "Your team of journalists came up with the following ideas of titles for the {topic} rubric. Each title has an index from 0 to {length}. Give me the indices of the 4 titles most suceptible to generate a lot of reactions on social media and try to diversify within the topic. Don't give me a reason why, ONLY answer with the 4 numbers in the following format: w,x,y,z. {test}".format(topic=self.topic, length=length, test=arrayToString(titles_list))
      response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                          messages=[{"role": "system", "content": self.system_msg},
                                          {"role": "user", "content": user_msg}])
   

      response_content = response.choices[0].message.content
      relevant_indices_string = response_content.split(",")
      self.relevant_indices = []
      for i in relevant_indices_string:
         self.relevant_indices.append(int(i))
      return self.relevant_indices        #This needs to be of the form: [1,2,4,8,13]

   def writeTitles(self):
      user_msg = "Rewrite the following title in an ironic way that will catch people off guard. Act as a comedian and don't be afraid to be controversial"
      index = 0
      for title in self.titles:
         if index in self.relevant_indices:
            response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                          messages=[{"role": "system", "content": self.system_msg},
                                          {"role": "user", "content": user_msg+title}])
            self.oldTitles.append(title)
            response_content = response.choices[0].message.content
            self.newTitles.append(response_content)
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
            response_content = response.choices[0].message.content
            self.newContents.append(response_content)
         index += 1

      
            





