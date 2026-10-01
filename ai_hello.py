# c4b
from pathlib import Path

import anthropic
from dotenv import load_dotenv

folder = Path(__file__).parent
load_dotenv(folder / ".env")

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=200,
    messages=[{"role": "user", "content": "say hello to raff in a short sentence"}],
)

print(message.content[0].text)
