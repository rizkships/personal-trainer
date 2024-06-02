import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

print('Imports are working correctly')

# Initialize the OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
model = "gpt-3.5-turbo-16k"

personal_trainer = client.beta.assistants.create(
    name="Personal Trainer",
    instructions="You are the best personal trainer and nutritionist who knows how to get clients to lose fat and build lean muscles. You've trained high-caliber athletes and movie stars.",
    model=model,
)

thread = client.beta.threads.create()

message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="How do I get started working out to lose fat and build muscles?"
)

run = client.bete.threads.run.create_and_poll(
    thread_id=thread.id,
    assistant_id=personal_trainer.id,
    instructions = "Please address the user as Rizk."

)



















# Create a simple request to the OpenAI API
""" 
try:
    chat_completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Tell me a joke."}
        ]
    )
    # Print the response from the OpenAI API
    print(chat_completion.choices[0].message.content)
except Exception as e:
    print(f"An error occurred: {e}")

"""
