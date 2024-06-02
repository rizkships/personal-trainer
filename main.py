import os
from openai import OpenAI
from dotenv import load_dotenv
from typing_extensions import override
from openai import AssistantEventHandler

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




# First, we create a EventHandler class to define
# how we want to handle the events in the response stream.
 
class EventHandler(AssistantEventHandler):    
  @override
  def on_text_created(self, text) -> None:
    print(f"\nassistant > ", end="", flush=True)
      
  @override
  def on_text_delta(self, delta, snapshot):
    print(delta.value, end="", flush=True)
      
  def on_tool_call_created(self, tool_call):
    print(f"\nassistant > {tool_call.type}\n", flush=True)
  
  def on_tool_call_delta(self, delta, snapshot):
    if delta.type == 'code_interpreter':
      if delta.code_interpreter.input:
        print(delta.code_interpreter.input, end="", flush=True)
      if delta.code_interpreter.outputs:
        print(f"\n\noutput >", flush=True)
        for output in delta.code_interpreter.outputs:
          if output.type == "logs":
            print(f"\n{output.logs}", flush=True)
 
# Then, we use the `stream` SDK helper 
# with the `EventHandler` class to create the Run 
# and stream the response.
 
with client.beta.threads.runs.stream(
  thread_id=thread.id,
  assistant_id=personal_trainer.id,
  instructions="Please address the user as Rizk.",
  event_handler=EventHandler(),
) as stream:
  stream.until_done()






















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
