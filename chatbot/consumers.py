import json
import os
import openai
import re
from channels.generic.websocket import WebsocketConsumer
# from chatbot.chat import get_chatbot_message
from dotenv import load_dotenv
load_dotenv()
openai.api_key = "Your Api Key Goes here!"
# def get_chatbot_message(message):
#     completion = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "system", "content": "As a compassionate mental health companion, my purpose is to provide guidance and solace to those experiencing emotional breakdowns. My responses are crafted to be succinct, yet filled with empathy, aiming to offer prompt support during challenging moments. i will keep responses short and simple"},
#             {"role": "user", "content": message}
#         ]
#     )

#     print(completion)
#     return completion.choices[0].message['content']


def find_doctor_mention(text):
    # Define the regex pattern
    keywords = ["dr", "doctor", "profession" , "nurse", "therapist"]
    if any(keyword in text.lower() for keyword in keywords):
        return True
    else:
      return False

def get_chatbot_message(message):
    contact_dr = find_doctor_mention(message)
    if contact_dr:
        return "contact nearby DR"
    else:
       return "Let's Chat"

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print(text_data_json)
        message = text_data_json["message"]

        needs_dr = find_doctor_mention(message)

        if not needs_dr:
            chat_response = get_chatbot_message(message)
        else:
            chat_response = f"""
            <p>I have found the following Dr nearest to your location</p>
                <div class="p-6">
                    <h5 class="mb-2 block font-sans text-xl font-semibold leading-snug tracking-normal text-blue-gray-900 antialiased">
                    Dr Makhubo Dental 
                    </h5>
                    <p class="block font-sans text-base font-light leading-relaxed text-inherit antialiased">
                    Services Saveways
                    </p>
                    <br>
                    <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d7179.536967302387!2d29.228733942246542!3d-25.877096159117986!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x1eeaeda785666601%3A0xb3f8c82d6e3e7519!2sDr%20Makhubo%20Dental%20Services%20Saveways!5e0!3m2!1sen!2sza!4v1698551112599!5m2!1sen!2sza" width="300" height="250" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
                </div>
                <div class="p-6 pt-0">
                    <button data-ripple-light="true" type="button" class="select-none rounded-lg bg-blue-500 py-3 px-6 text-center align-middle font-sans text-xs font-bold uppercase text-white shadow-md shadow-blue-500/20 transition-all hover:shadow-lg hover:shadow-blue-500/40 focus:opacity-[0.85] focus:shadow-none active:opacity-[0.85] active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none">
                    Request Help
                    </button>
                </div>
                <br></br>
                    <p>Do you need more assistance?</p>
                            """
        self.send(text_data=json.dumps({ "message": message, "response": chat_response}))

    # def chat_message(self, event):
    #     message = event['message']

    #     self.send(text_data=json.dumps({
    #         'type':'chat',
    #         'message':message
    #     }))