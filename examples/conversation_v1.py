import json
from watson_developer_cloud import ConversationV1

conversation = ConversationV1(
    username='d0e3189a-8084-4d74-adab-aedb11ac09ea',
    password='O0bjw1EztPqb',
    version='2016-09-20')

# replace with your own workspace_id
workspace_id = 'd148117e-a0a7-44f2-95b0-d92cc73d6818'

response = conversation.message(workspace_id=workspace_id, message_input={
    'text': 'I think I have diabetes'})
print(json.dumps(response, indent=2))

# When you send multiple requests for the same conversation, include the
# context object from the previous response.
# response = conversation.message(workspace_id=workspace_id, message_input={
# 'text': 'turn the wipers on'},
#                                context=response['context'])
# print(json.dumps(response, indent=2))


{
  "url": "https://gateway.watsonplatform.net/conversation/api",
  "username": "d0e3189a-8084-4d74-adab-aedb11ac09ea",
  "password": "O0bjw1EztPqb"
}
