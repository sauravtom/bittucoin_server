# yomamabot/fb_yomamabot/views.py
import json, requests, random, re
from pprint import pprint

from django.views import generic
from django.http.response import HttpResponse

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from core.post_message import FacebookMessage

#  ------------------------ Fill this with your page access token! -------------------------------
PAGE_ACCESS_TOKEN = "EAAYQPinTkhEBANlu6CSVS22WcPEEEmHYFmriZBRpc8GbvT24A4dD0gD4twrZAmPTsjqlCmK5tZCZCaK4q79xBxZBZAdpGrzjHShgMshJ8RL9Og5dbJwZApy6lGvVFVESMZCNlCzwyFqZAhTkj3JFNRkq5GxA7Lj1EZCJJya2dGr7AcOgZDZD"
VERIFY_TOKEN = "hello_bot"


# Create your views here.
class MessengerBotView(generic.View):
    def get(self, request, *args, **kwargs):
        if self.request.GET['hub.verify_token'] == VERIFY_TOKEN:
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('Error, invalid token')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)

    # Post function to handle Facebook messages
    def post(self, request, *args, **kwargs):
        # Converts the text payload into a python dictionary
        incoming_message = json.loads(self.request.body.decode('utf-8'))
        # Facebook recommends going through every entry since they might send
        # multiple messages in a single call during high load
        for entry in incoming_message['entry']:
            for message in entry['messaging']:
                # Check to make sure the received call is a message call
                # This might be delivery, optin, postback for other events
                if 'message' in message:
                    # Print the message to the terminal
                    pprint(message)

                    post_message = FacebookMessage(message['sender']['id'], message['message']['text'])
                    # Assuming the sender only sends text. Non-text messages like stickers, audio, pictures
                    # are sent as attachments and must be handled accordingly.
                    post_message.post_facebook_message()
        return HttpResponse()