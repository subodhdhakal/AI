from haystack.components.generators.chat import OpenAIChatGenerator
from haystack.dataclasses import ChatMessage
from haystack.utils import Secret
from helper import load_groq_env

load_groq_env()
generator = OpenAIChatGenerator(
    api_key=Secret.from_env_var("GROQ_API_KEY"),
    api_base_url="https://api.groq.com/openai/v1",
    model="llama3-8b-8192",
    generation_kwargs = {"max_tokens": 512}
)

messages = []

while True:
    msg = input("Enter your message or Q to exit\n🧑 ")
    if msg=="Q":
        break
    messages.append(ChatMessage.from_user(msg))
    response = generator.run(messages=messages)
    assistant_resp = response['replies'][0]
    print("🤖 "+assistant_resp.content)
    messages.append(assistant_resp)
