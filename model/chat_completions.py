from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)


def chatbot(prompt):
    bot = "You are children math teacher called Joseph, you are loving and caring. You will do whatever it takes to make sure the success of all of your student."

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "assistant", "content": bot},
            {"role": "user", "content": prompt}
        ]

    )

    role = response.choices[0].message.role
    message = response.choices[0].message.content.strip()

    return {role: message}
