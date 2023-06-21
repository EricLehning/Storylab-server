import openai
import os
from django.http import JsonResponse
from openai import ChatCompletion
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

class ChatbotView(ViewSet):
    def create(self, request):
        user_input = request.data.get('user_input')

        completion = ChatCompletion.create(
            api_key=openai_api_key,
            model="gpt-3.5-turbo", temperature= 0.7,
            messages=[
                {
                    "role": "system",
                    "content":                                      
                                "You are a professional fiction writer who creates unique story outlines based on the story sentence, or 'logline' provided by the user. " 
                                "You write in the present tense."
                                "The only text you return is the body of the short story based on the story logline provided by the user. " 
                                "All the major elements of the story are included in the logline, but you may also invent others in order to make those provided work together in the most entertaining way possible. " 
                                "You avoid cliches and discover unconventional ways to develop the central theme of every story." 
                                "Your main character changes according to what they want, what they're afraid of, and what they learn about themselves through all that they are able to overcome, or fail to overcome." 
                                "You bring the story to a dynamic climax which sees the unification of character and theme through to a surprising conclusion."
                },
                {
                    "role": "user",
                    "content": user_input
                }
            ]

        )

        response = completion.choices[0].message.content

        return Response({'response': response})