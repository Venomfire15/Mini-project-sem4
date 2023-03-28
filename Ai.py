import os
import openai
import pyttsx3

#input 
a = input(print("Enter title to create article"))

#open api key 
os.environ["OPENAI_API_KEY"] = "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"
openai.api_key = os.getenv("OPENAI_API_KEY")

#Writing file
#AI Writer function (Don't change any values)
def call():
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt= a,
      temperature=0.7,
      max_tokens=256,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
    if 'choices' in response:
        if (len(response['choices']) > 0):
            answer = response['choices'][0]['text']
            print(answer)
            text = open("Summary.txt", '+w')
            text.write(answer)

a = call()

#Reading file
tts = pyttsx3.init()
file = open("Summary.txt", 'r')
r = file.read()
tts.say(r)
tts.runAndWait()