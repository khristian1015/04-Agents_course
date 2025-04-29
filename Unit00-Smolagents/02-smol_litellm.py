
# Lap HP Pavilion 14 /dev/sda3 env: nlp (ollama: gemma3:1b, llama3.2, phi4-mini)
# 2025APR27

# https://huggingface.co/docs/smolagents/v1.14.0/en/reference/models#smolagents.LiteLLMModel

from smolagents import LiteLLMModel

messages = [
  {"role": "user", "content": [{"type": "text", "text": "Hello, how are you?"}]}
]

model = LiteLLMModel(model_id="anthropic/claude-3-5-sonnet-latest", temperature=0.2, max_tokens=10)
print(model(messages))
