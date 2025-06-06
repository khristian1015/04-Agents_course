# 2025APR27:
# Lap HP Pavilion 14 /dev/sda3 env: nlp (ollama: gemma3:1b, llama3.2, phi4-mini)
# 2025APR29:
# Lap Latitude 7300 C:\ env: nlp (ollama: gemma3:12b, llama3.2)

# CONNECTING REMOTELY TO HUGGING FACE MODELS (NON-FREE)
# https://huggingface.co/docs/smolagents/v1.14.0/en/reference/models#smolagents.LiteLLMModel

from smolagents import LiteLLMModel

messages = [
  {"role": "user", "content": [{"type": "text", "text": "Hello, how are you?"}]}
]

# WARNING: This is NON-FREE; uses credits & money from the Huggingface account.
model = LiteLLMModel(model_id="google/gemma-3-1b-it", temperature=0.2, max_tokens=10)
print(model(messages))

'''
completion(model, messages, timeout, temperature, top_p, n, stream, stream_options, stop, 
           max_completion_tokens, max_tokens, modalities, prediction, audio, presence_penalty, 
           frequency_penalty, logit_bias, user, reasoning_effort, response_format, seed, tools, 
           tool_choice, logprobs, top_logprobs, parallel_tool_calls, deployment_id, extra_headers, 
           functions, function_call, base_url, api_version, api_key, model_list, thinking, **kwargs)
'''
# Out[]:
BadRequestError: litellm.BadRequestError: LLM Provider NOT provided. Pass in the LLM provider you 
are trying to call. You passed model=google/gemma-3-1b-it
Pass model as E.g. For 'Huggingface' inference endpoints pass in 
`completion(model='huggingface/starcoder',..)` Learn more: https://docs.litellm.ai/docs/providers

# See file 03-smol_remote.py for usage with litellm: https://docs.litellm.ai/docs/providers

# FIXING error by adding full provider name
model = LiteLLMModel(model_id="huggingface/together/deepseek-ai/DeepSeek-R1", 
    temperature=0.2, 
    max_tokens=10)
print(model(messages))
# Out[]:
ChatMessage(role=<MessageRole.ASSISTANT: 'assistant'>, content='\n\nHi there! I suggest getting', 
tool_calls=None, raw=ModelResponse(id='ns1xp1B-zqrih-937ddcfd7cfe829e', created=1745919892, 
model='deepseek-ai/DeepSeek-R1', object='chat.completion', system_fingerprint=None, 
choices=[Choices(finish_reason='length', index=0, 
message=Message(content='\n\nHi there! I suggest getting', 
role='assistant', 
tool_calls=None, 
function_call=None, 
reasoning_content='\n\n', 
provider_specific_fields={'reasoning_content': '\n\n'}))], 
usage=Usage(completion_tokens=10, prompt_tokens=12, total_tokens=22, 
completion_tokens_details=None, prompt_tokens_details=None), prompt=[]))


# ---------------------------------------


# CONNECTING LOCALLY TO OLLAMA MODELS (FREE)
https://huggingface.co/docs/smolagents/guided_tour?Pick+a+LLM=Ollama

from smolagents import LiteLLMModel

messages = [
  {"role": "user", "content": [{"type": "text", "text": "Hello, how are you?"}]}
]

# This is FREE; runs in your machine
model = LiteLLMModel(
    model_id="ollama_chat/llama3.2", # This model is a bit weak for agentic behaviours though
    api_base="http://localhost:11434", # replace with 127.0.0.1:11434 or remote open-ai compatible server if necessary
    api_key="YOUR_API_KEY", # replace with API key if necessary
    num_ctx=8192, # ollama default is 2048 which will fail horribly. 8192 works for easy tasks, more is better. Check https://huggingface.co/spaces/NyxKrage/LLM-Model-VRAM-Calculator to calculate how much VRAM this will need for the selected model.
    temperature=0.2, 
    max_tokens=50)
print(model(messages))
#Out [23]: LapLatitude7300
ChatMessage(role=<MessageRole.ASSISTANT: 'assistant'>, content="I'm just a language model, so I 
don't have feelings or emotions like humans do. However, I'm functioning properly and ready to 
assist you with any questions or tasks you may have! How can I help you today?", tool_calls=None, 
raw=ModelResponse(id='chatcmpl-27a61ef3-d4c3-4035-8254-2d44f3f73f4a', created=1745996573, 
model='ollama_chat/llama3.2', object='chat.completion', system_fingerprint=None, 
choices=[Choices(finish_reason='stop', index=0, 
message=Message(content="I'm just a language model, so I don't have feelings or emotions like 
humans do. However, I'm functioning properly and ready to assist you with any questions or tasks 
you may have! How can I help you today?", 
role='assistant', 
tool_calls=None, 
function_call=None, 
provider_specific_fields=None))], usage=Usage(completion_tokens=47, prompt_tokens=31, 
total_tokens=78, completion_tokens_details=None, prompt_tokens_details=None)))