import os
import openai

openai.organization = "org-L22NNUMXPfemeE6PNC51tf1W"
openai.api_key = "API_KEY"

MODEL = "gpt-3.5-turbo"

line = ""


def talk(message) -> None:
    completion = openai.ChatCompletion.create(
        model=MODEL,
        messages=[
            {"role": "user", "content": message}
        ]
    )

    for choice in completion["choices"]:
        print("GPT3 > ", choice["message"]["content"], '\n')


print("GPyT 1.0\nby belicfr\n")

while line != "!stop":
    line = input("YOU > ")

    if line != "!stop":
        talk(line)