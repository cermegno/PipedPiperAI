# Small Python application to demonstrate the simplicity of Gradio

# First we need to import the necessary libraries
# - If not installed already you can install Gradio with PIP (pip install gradio)
# - We need to extract information from a JSON payload. The json library is included in the core Python install 

import gradio as gr
from openai import OpenAI
import os

apikey = os.environ["NVIDIA_API_KEY"]
llmurl = os.environ["LLM_URL"]

# As before we create a client object that points to the NVIDIA API. Use your own key.
#   base_url = "https://integrate.api.nvidia.com/v1",
client = OpenAI(
  base_url =llmurl,
  api_key = apikey
)

# This is the function that will be called by the Gradio interface
# It includes the call to the NVIDIA API
# Since it uses the stateful chat function we need the message and the history as parameters
# The history parameter is a list of openai-style dictionaries "role/content"
def give_response(message, history):

    completion = client.chat.completions.create(
      model="meta/llama-3.2-3b-instruct",
      messages=[{"role": "user", "content": message}],
      temperature=0.2,
      top_p=0.7,
      max_tokens=1024,
    )

    return completion.choices[0].message.content

# This creates the actual interface.
# You can check for more options in the Gradio documentation: https://www.gradio.app/docs/gradio/chatinterface
demo = gr.ChatInterface(
              give_response,  #You can also use the syntax fn=give_response
              type = "messages",
              title="My first Chatbot",
              description="Ask me a question, don't be shy",
            )

# The final step is run the Gradio app
# This will display a message with the actual URL you can use to open the app in your browser
demo.launch(server_name="0.0.0.0")

# You can use the following options to change the port the server listens to and to ignore self-signed certs
#demo.launch(server_name="0.0.0.0", ssl_verify=False, server_port=7860)
