#Code to interact with Azure  OpenAI


import os
import openai


openai.api_key = "AZURE_OPENAI_KEY"
openai.api_base = "AZURE_OPENAI_ENDPOINT"
deployment_name= "AZURE_OPENAI_DEPLOYMENT" #This will correspond to the custom name you chose for your deployment when you deployed a model.


# your endpoint should look like the following https://YOUR_RESOURCE_NAME.openai.azure.com/
openai.api_type = 'azure'
openai.api_version = '2023-05-15' #this might change in the future



response = openai.ChatCompletion.create(
    engine= deployment_name, # The deployment name you chose when you deployed the GPT-35-Turbo or GPT-4 model.
    messages=[
        {"role": "system", "content": "Assistant is a large language model trained by OpenAI."},
        {"role": "user", "content": "Who were the founders of Microsoft?"}
    ]
)


print(response)


print(response['choices'][0]['message']['content'])
