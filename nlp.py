from transformers.utils import logging
logging.set_verbosity_error()

from transformers import pipeline

chatbot = pipeline(task="conversational",
                   model="models/facebook/blenderbot-400M-distill")

user_message = """
What are some fun activities I can do in the winter?
"""
# user_message = """
# I'm feeling really down today. What can I do to feel better?
# """

from transformers import Conversation

conversation = Conversation(user_message)
print(conversation)
conversation = chatbot(conversation)
print(conversation)