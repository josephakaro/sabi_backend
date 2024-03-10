# python Module imports:
from model.chat_completions import chatbot
from flask import Flask
from flask_restful import Api, Resource
from openai import OpenAI

from dotenv import load_dotenv
import os


# Environment Variables
PORT = os.environ.get('PORT')


# OpenAI Prep:

# Initialization:
app = Flask(__name__)
api = Api(app)

"""
# TODO: DAY ONE
# TODO: User Authentications
	# Search for Existing credentials in the database
		- if user exist login
		- if doesn't exist prompt user to enter correct credentials
		- Use Oauth for other login methods
		- Provide password reset options on five incorrect entry
		- Allow Access if no error found!.
"""

"""
# TODO: User Authorization
	# Create New user
		- Check for correct format entry
		- if the provided details exist in the database, prompt user to enter new.
		- Allow user to access their dashbord.
		- User must verify their email.
"""

"""
# TODO: DAY TWO
# TODO: SABI-GPT Logics
"""


class Response(Resource):
    def get(self, message):
        prompt = chatbot(message)
        return prompt, 201


api.add_resource(Response, '/chat/<string:message>')

# Server Status
if __name__ == "__main__":
    app.run(debug=True, port=PORT)
