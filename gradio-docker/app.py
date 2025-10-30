import gradio as gr
import os
import requests
import urllib3
urllib3.disable_warnings()

appurl = os.environ["APP_URL"]

def give_response(query, history):

    payload = {"query": query}
    response = requests.post(appurl, json=payload)

    return response.json()["response"]

demo = gr.ChatInterface(
              give_response,  #You can also use the syntax fn=give_response
              type = "messages",
              title="My first Chatbot",
              description="Ask me a question, don't be shy",
            )

demo.launch(server_name="0.0.0.0")

