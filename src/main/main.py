import openai
import NewYorkTimes
from ApiKeys import ApiKeys
openai.organization = ApiKeys.openAiOrg
openai.api_key = ApiKeys.openAiApiKey


topStories = NewYorkTimes.NewYorkTimes(type="topStories")

print(topStories.titles)

# system_msg = 'You are talking to a 10 year old asian girl'

# # Define the user message
# user_msg = 'Tell her a very short story that teaches her a lesson about life.'

# # Create a dataset using GPT
# response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
#                                         messages=[{"role": "system", "content": system_msg},
#                                          {"role": "user", "content": user_msg}])

# print(response)



