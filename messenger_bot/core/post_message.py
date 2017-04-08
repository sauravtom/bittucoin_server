import re
import requests
import json
from pprint import pprint
from generate_node_message import GenerateMessage

#  ------------------------ Fill this with your page access token! -------------------------------
PAGE_ACCESS_TOKEN = "EAAYQPinTkhEBANlu6CSVS22WcPEEEmHYFmriZBRpc8GbvT24A4dD0gD4twrZAmPTsjqlCmK5tZCZCaK4q79xBxZBZAdpGrzjHShgMshJ8RL9Og5dbJwZApy6lGvVFVESMZCNlCzwyFqZAhTkj3JFNRkq5GxA7Lj1EZCJJya2dGr7AcOgZDZD"
VERIFY_TOKEN = "hello_bot"

class FacebookMessage:

    def __init__(self, sender_id, message):
        self.sender_id = sender_id
        self.message = message

    def post_facebook_message(self):
        # Remove all punctuations, lower case the text and split it based on space
        tokens = re.sub(r"[^a-zA-Z0-9\s]", ' ', self.message).lower().split()

        user_details_url = "https://graph.facebook.com/v2.6/%s" % self.sender_id
        user_details_params = {'fields': 'first_name,last_name,profile_pic', 'access_token': PAGE_ACCESS_TOKEN}
        user_details = requests.get(user_details_url, user_details_params).json()

        message = GenerateMessage('')

        post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=%s' % PAGE_ACCESS_TOKEN
        response_msg = json.dumps({"recipient": {"id": self.sender_id}, "message": message.generatee_welcome_node()})
        status = requests.post(post_message_url, headers={"Content-Type": "application/json"}, data=response_msg)
        pprint(status.json())