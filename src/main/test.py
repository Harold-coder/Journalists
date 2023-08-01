import os
import openai
from ApiKeys import ApiKeys
openai.organization = ApiKeys.openAiOrg
openai.api_key = ApiKeys.openAiApiKey
# openai.Model.list()
# models = openai.Model.list()
# print(models)

def arrayToString(array):
    res = ""
    for el in array:
        res += el
    return res

test = ['A Climate Warning from the Cradle of Civilization', 'The Secret History of Gun Rights: How Lawmakers Armed the N.R.A.', 'Amid the Counterattack’s Deadly Slog, a Glimmer of Success for Ukraine', 'Russia Says 2 Drones Hit Buildings in Moscow in Latest Wave of Attacks', 'Russia Takes Its Ukraine Information War Into Video Games', 'Inside the Party Switch that Blew Up North Carolina Politics', 'At Least 43 Killed in Blast at Political Rally in Pakistan', 'What Is It About Montecito?', 'New York City Had a Migrant Crisis. It Hired a Covid Expert to Help.', 'The Legacy Dilemma: What to Do About Privileges for the Privileged?', '$60 Million Refund Request Shows Financial Pressure on Trump From Legal Fees', 'Trump Threatens Republicans Who Don’t Help Him Exact Vengeance', 'Megan Rapinoe Is Not Going Quietly', 'The Weekender', 'The New York Times News Quiz, July 28, 2023', 'He Created the Katamari Games, but They’re Rolling On Without Him', 'How Trump Could Wreck Things for Republicans in 2024', 'What ‘Oppenheimer’ Doesn’t Tell You About the Trinity Test', 'The Research Scandal at Stanford Is More Common Than You Think', 'It Was Never Just About the Butterflies', 'A New Recipe for a Very Old Hummus', 'Why Is It So Darn Hot?', 'In Israel, High Stakes for High Court: Democracy’s Fate', 'A Federal Food Safety Case Reveals Latest New York City Rat Horror Story', 'West African Nations Threaten Military Action Unless Niger Coup Is Undone', 'Terence Crawford Stands Alone at the Top of Boxing', 'A Recipe for Love? Add ‘Water and Sunlight.’']

# length = str(len(test))
# system_msg = "You are an expert in social media running a newspaper. Your goal is to generate as much interactions as possible.You like to be controversial and have a strong sense of humor."

# user_msg = "Your team of journalists came up with the following ideas of titles. Each title as an index from 0 to {length}. Give me the indices of the 4 titles most suceptible to generate a lot of reactions on social media. Don't give me a reason why,simply answer with the 4 indexes in the following format: w,x,y,z. {test}".format(length=length, test=arrayToString(test))

# response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
#                                           messages=[{"role": "system", "content": system_msg},
#                                           {"role": "user", "content": user_msg}])


# response_content = response.choices[0].message.content
# relevant_indices = response_content.split(",")
# for i in relevant_indices:
#     i = int(i)
# print(relevant_indices)



testStr = "Hello Boss I wouldn''t test you out"
def formatString(text):
   text = text.replace("'", "''")
   return text

print(formatString(testStr))

