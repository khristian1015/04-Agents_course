
# Lap HP Pavilion 14 /dev/sda3 env: nlp (ollama: gemma3:1b, llama3.2, phi4-mini, qwen3:4b)
# 2025APR27
# PC Optiplex 9020 C:\ nlp1 (ollama: gemma3:12b, gemma3:27b)
# 2025APR28

# https://docs.litellm.ai/docs/providers/ollama

# Example usage:

from litellm import completion

response = completion(
    model="ollama/gemma3:1b", 
    messages=[{ "content": "respond in 20 words. who are you?","role": "user"}], 
    api_base="http://localhost:11434"
)
print(response)
#Out [5]: 
ModelResponse(id='chatcmpl-3a23afa6-fb57-4a5d-9ece-ad2c8323a6b8', created=1745740184, 
model='ollama/gemma3:1b', object='chat.completion', system_fingerprint=None, 
choices=[Choices(finish_reason='stop', index=0, 
message=Message(content='I am Gemma, a large language model created by Google DeepMind.',
role='assistant', 
tool_calls=None, 
function_call=None, 
provider_specific_fields=None))], usage=Usage(completion_tokens=15, prompt_tokens=25, 
total_tokens=40, completion_tokens_details=None, prompt_tokens_details=None))

print(response.choices[0])
#Out [5]: 
Choices(finish_reason='stop', index=0, message=Message(content='I am Gemma, a large language model created by Google DeepMind.', role='assistant', tool_calls=None, function_call=None, provider_specific_fields=None))

print(response.choices[0].message.content)
#Out [5]: 
I am Gemma, a large language model created by Google DeepMind.

#  model="ollama/gemma3:12b", 
In [4]: print(response)
ModelResponse(id='chatcmpl-e2bbc07a-e658-4904-af9a-5a34bd1a54a3', created=1745856325, 
model='ollama/gemma3:12b', object='chat.completion', system_fingerprint=None, 
choices=[Choices(finish_reason='stop', index=0, 
message=Message(content="I am Gemma, an open-weights AI assistant created by the Gemma team at 
Google DeepMind. I'm here to help!", 
role='assistant', 
tool_calls=None, 
function_call=None, 
provider_specific_fields=None))], usage=Usage(completion_tokens=28, prompt_tokens=25, 
total_tokens=53, completion_tokens_details=None, prompt_tokens_details=None))

#-----------------

# Example Usage - JSON Mode

from litellm import completion

response = completion(
  model="ollama/gemma3:1b",
  messages=[
      {
          "role": "user",
          "content": "respond in json, what's the weather"
      }
  ],
  max_tokens=10,
  format = "json",
  # api_base="http://localhost:11434", # CAUSES ERROR
  # api_key = "ollama" # CAUSES ERROR
)
# Out[]:
json.decoder.JSONDecodeError: Unterminated string starting at: line 1 column 33 (char 32)


response = completion(
  model="ollama/gemma3:1b",
  messages=[
      {
          "role": "user",
          "content": "respond in json, what's the weather"
      }
  ],
  max_tokens=200,
  format = "json",
  # api_base="http://localhost:11434", # CAUSES ERROR
  # api_key = "ollama" # CAUSES ERROR
)
...
File ~/bin/miniconda3/envs/nlp/lib/python3.11/site-packages/litellm/llms/ollama/completion/transformation.py:266, in OllamaConfig.transform_response(self, model, raw_response, model_response, logging_obj, request_data, messages, optional_params, litellm_params, encoding, api_key, json_mode)
    259 function_call = json.loads(response_json["response"])
    260 message = litellm.Message(
    261     content=None,
    262     tool_calls=[
    263         {
    264             "id": f"call_{str(uuid.uuid4())}",
    265             "function": {
--> 266                 "name": function_call["name"],
    267                 "arguments": json.dumps(function_call["arguments"]),
    268             },
    269             "type": "function",
    270         }
    271     ],
    272 )
    273 model_response.choices[0].message = message  # type: ignore

KeyError: 'name'


response = completion(
  model="ollama/gemma3:27b",
  messages=[
      {
          "role": "user",
          "content": "respond in json, what's the weather"
      }
  ],
  max_tokens=200,
  format = "json",
  # api_base="http://localhost:11434", # CAUSES ERROR
  # api_key = "ollama" # CAUSES ERROR
)
...
APIConnectionError: litellm.APIConnectionError: 'name'                                      
Traceback (most recent call last):                                                  
File "C:\Users\Dell\miniconda3\envs\nlp1\Lib\site-packages\litellm\main.py", 
line 2872, in completion                                                       
response = base_llm_http_handler.completion(                                   
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^                                              
File "C:\Users\Dell\miniconda3\envs\nlp1\Lib\site-packages\litellm\llms\custom_httpx\
llm_http_handler.py", line 415, in completion                                            
return provider_config.transform_response(                        
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^                             
File "C:\Users\Dell\miniconda3\envs\nlp1\Lib\site-packages\litellm\llms\ollama\completion\
transformation.py", line 266, in transform_response                                         
"name": function_call["name"],                                          
~~~~~~~~~~~~~^^^^^^^^      
                                             
KeyError: 'name'   
                    

response = completion(
  model="ollama/llama3.2",
  messages=[
      {
          "role": "user",
          "content": "respond in json, what's the weather"
      }
  ],
  max_tokens=10,
  format = "json",
  # api_base="http://localhost:11434", # CAUSES ERROR
  # api_key = "ollama" # CAUSES ERROR
)
  File "/home/clm/bin/miniconda3/envs/nlp/lib/python3.11/json/decoder.py", line 355, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 36 (char 35)


response = completion(
  model="ollama/llama3.2",
  messages=[
      {
          "role": "user",
          "content": "respond in json, what's the weather"
      }
  ],
  max_tokens=200,
  format = "json",
  # api_base="http://localhost:11434", # CAUSES ERROR
  # api_key = "ollama" # CAUSES ERROR
)
File ~/bin/miniconda3/envs/nlp/lib/python3.11/site-packages/litellm/llms/ollama/completion/transformation.py:266, in OllamaConfig.transform_response(self, model, raw_response, model_response, logging_obj, request_data, messages, optional_params, litellm_params, encoding, api_key, json_mode)
    259 function_call = json.loads(response_json["response"])
    260 message = litellm.Message(
    261     content=None,
    262     tool_calls=[
    263         {
    264             "id": f"call_{str(uuid.uuid4())}",
    265             "function": {
--> 266                 "name": function_call["name"],
    267                 "arguments": json.dumps(function_call["arguments"]),
    268             },
    269             "type": "function",
    270         }
    271     ],
    272 )
    273 model_response.choices[0].message = message  # type: ignore

KeyError: 'name'


#----------------------------------


# Example Usage - Tool Calling

from litellm import completion
import litellm 

## [OPTIONAL] REGISTER MODEL - not all ollama models support function calling, litellm defaults to json mode tool calls if native tool calling not supported.

# litellm.register_model(model_cost={
#                 "ollama_chat/llama3.1": { 
#                   "supports_function_calling": true
#                 },
#             })

tools = [
  {
    "type": "function",
    "function": {
      "name": "get_current_weather",
      "description": "Get the current weather in a given location",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {
            "type": "string",
            "description": "The city and state, e.g. San Francisco, CA",
          },
          "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
        },
        "required": ["location"],
      },
    }
  }
]

messages = [{"role": "user", "content": "What's the weather like in Boston today?"}]

response = completion(
  model="ollama_chat/llama3.2",
  messages=messages,
  tools=tools
)
In [14]: print(response)
ModelResponse(id='chatcmpl-4e320dc4-9e51-4a3c-bdf1-28e458bc47fe', created=1745740702, 
model='ollama_chat/llama3.2', object='chat.completion', system_fingerprint=None, 
choices=[Choices(finish_reason='stop', index=0, 
message=Message(content='', 
role='assistant', 
tool_calls=[ChatCompletionMessageToolCall(function=Function(
arguments='{"location": "Boston, MA", "unit": "fahrenheit"}', 
name='get_current_weather'), id='12288494-691e-4409-a470-45cea1b553e9', type='function')], 
function_call=None, 
provider_specific_fields=None))], usage=Usage(completion_tokens=27, prompt_tokens=193, total_tokens=220, completion_tokens_details=None, prompt_tokens_details=None))


# Changing the message to Mexico to see if Celsius is chosen
messages = [{"role": "user", "content": "What's the weather like in mexico today?"}]

response = completion(
  model="ollama_chat/llama3.2",
  messages=messages,
  tools=tools
)
In [6]: print(response)
ModelResponse(id='chatcmpl-bb0f30a4-2795-44fe-9d1c-b9ac92d9c266', created=1745766624, 
model='ollama_chat/llama3.2', object='chat.completion', system_fingerprint=None, 
choices=[Choices(finish_reason='stop', index=0, 
message=Message(content='', 
role='assistant', 
tool_calls=[ChatCompletionMessageToolCall(function=Function(arguments='{"location": "Mexico", 
"unit": "celsius"}', name='get_current_weather'), id='45520d48-3cc9-4c18-9e59-e37da11376bb', 
type='function')], 
function_call=None, 
provider_specific_fields=None))], usage=Usage(completion_tokens=25, prompt_tokens=193, 
total_tokens=218, completion_tokens_details=None, prompt_tokens_details=None))


response = completion(
  model="ollama/gemma3:1b",
  messages=messages,
  tools=tools
)
In [3]: print(response)
ModelResponse(id='chatcmpl-e76255a7-1b32-4d23-83d6-233200370641', created=1745749802, 
model='ollama_chat/gemma3:1b', object='chat.completion', system_fingerprint=None, 
choices=[Choices(finish_reason='tool_calls', index=0, 
message=Message(content=None, 
role='assistant', 
tool_calls=[ChatCompletionMessageToolCall(function=Function(arguments='{"location": "Boston, MA"}', 
name='get_current_weather'), id='call_3541ecbb-63f9-4d53-b605-d9201a1b53bc', type='function')], 
function_call=None, 
provider_specific_fields=None))], usage=Usage(completion_tokens=22, prompt_tokens=164, 
total_tokens=186, completion_tokens_details=None, prompt_tokens_details=None))

response = completion(
    model="ollama_chat/phi4-mini",
    messages=messages,
    tools=tools
)
In [5]: print(response)
ModelResponse(id='chatcmpl-38acc587-d7e2-437a-bfbb-08313a94e96e', created=1745750155, 
model='ollama_chat/phi4-mini', object='chat.completion', system_fingerprint=None, 
choices=[Choices(finish_reason='stop', index=0, 
message=Message(content='<|tool_call|>[{
"type":"function",
"function":{"name":"get_current_weather",
"arguments":{"location": "Boston, MA", "unit": "fahrenheit"}}}]
<|/tool_call|>', 
role='assistant', 
tool_calls=None, 
function_call=None, 
provider_specific_fields=None))], usage=Usage(completion_tokens=34, prompt_tokens=103, 
total_tokens=137, completion_tokens_details=None, prompt_tokens_details=None))

In [6]: print(response.choices[0].message.content)
<|tool_call|>[{"type":"function","function":{"name":"get_current_weather","arguments":{"location": "Boston, MA", "unit": "fahrenheit"}}}]<|/tool_call|>


# model="ollama/gemma3:12b",
model="ollama/gemma3:12b"

messages = [{"role": "user", "content": "What's the weather like in Mexico today?"}]

response = completion(
  model=model,
  messages=messages,
  tools=tools
)
In [16]: print(response)
ModelResponse(id='chatcmpl-b94bd37b-3ef2-4288-9359-15b9d7ffbe4a', created=1745857025, 
model='ollama/gemma3:12b', object='chat.completion', system_fingerprint=None, 
choices=[Choices(finish_reason='tool_calls', index=0, 
message=Message(content=None, role='assistant', 
tool_calls=[ChatCompletionMessageToolCall(function=Function(arguments='{"location": "Mexico"}', 
name='get_current_weather'), id='call_259ef81b-a6d6-49f5-baff-1b682efcb640', type='function')], 
function_call=None, provider_specific_fields=None))], 
usage=Usage(completion_tokens=19, prompt_tokens=167, total_tokens=186, 
completion_tokens_details=None, prompt_tokens_details=None))


# model="ollama/gemma3:27b",
model="ollama/gemma3:27b"

messages = [{"role": "user", "content": "What's the weather like in Mexico today?"}]

response = completion(
  model=model,
  messages=messages,
  tools=tools
)
In [13]: print(response)                                                                     
ModelResponse(id='chatcmpl-112145a4-2a92-4e92-9b75-0145a06b6caf', created=1745862107, 
model='ollama/gemma3:27b', object='chat.completion', system_fingerprint=None, 
choices=[Choices(finish_reason='tool_calls', index=0, 
message=Message(content=None, 
role='assistant', 
tool_calls=[ChatCompletionMessageToolCall(function=Function(arguments='{"location": "Mexico", 
"unit": "fahrenheit"}', name='get_current_weather'), id='call_11dc06f3-44ce-4264-805a-e62dcd19d5d0', 
type='function')], 
function_call=None, provider_specific_fields=None))], 
usage=Usage(completion_tokens=27, prompt_tokens=167, total_tokens=194, 
completion_tokens_details=None, prompt_tokens_details=None)) 


# model="ollama/mistral-small3.1"
model="ollama/mistral-small3.1"

messages = [{"role": "user", "content": "What's the weather like in Boston today?"}]

response = completion(
  model=model,
  messages=messages,
  tools=tools
)
In [5]: print(response)                                                       
ModelResponse(id='chatcmpl-986f6ef9-a683-4901-b6dd-9694be1fdce5', created=1745870751, 
model='ollama/mistral-small3.1', object='chat.completion', system_fingerprint=None, 
choices=[Choices(finish_reason='tool_calls', index=0, 
message=Message(content=None, 
role='assistant', 
tool_calls=[ChatCompletionMessageToolCall(function=Function(
arguments='{"location": "Boston, MA"}', name='get_current_weather'), 
id='call_3b8dac68-429d-43d5-a839-2f61cef7a8f6', type='function')], 
function_call=None, provider_specific_fields=None))], 
usage=Usage(completion_tokens=21, prompt_tokens=507, total_tokens=528, 
completion_tokens_details=None, prompt_tokens_details=None)) 


from litellm import completion
model="ollama/qwen3:4b"

messages = [{"role": "user", "content": "What's the weather like in Boston today?"}]

response = completion(
  model=model,
  messages=messages,
  tools=tools
)
In [9]: print(response)
ModelResponse(id='chatcmpl-89fa51e6-20d8-4355-bbab-588b98efa805', created=1745885661, 
model='ollama/qwen3:4b', object='chat.completion', system_fingerprint=None,
choices=[Choices(finish_reason='tool_calls', index=0, 
message=Message(content=None, 
role='assistant', 
tool_calls=[ChatCompletionMessageToolCall(function=Function(arguments='{"location": "Boston, MA", "unit": "fahrenheit"}', name='get_current_weather'), id='call_0fd8384d-1a89-4954-b105-4e2a786b299f', type='function')], 
function_call=None, 
provider_specific_fields=None))], 
usage=Usage(completion_tokens=36, prompt_tokens=156, total_tokens=192, 
completion_tokens_details=None, prompt_tokens_details=None))

In [10]: print(response.choices[0].message.tool_calls)
[ChatCompletionMessageToolCall(function=Function(arguments='{"location": "Boston, MA", "unit": "fahrenheit"}', name='get_current_weather'), id='call_0fd8384d-1a89-4954-b105-4e2a786b299f', type='function')]


messages = [{"role": "user", "content": "What's the weather like in Mexico today?"}]

response = completion(
  model=model,
  messages=messages,
  tools=tools
)
In [12]: print(response.choices[0].message.tool_calls)
[ChatCompletionMessageToolCall(function=Function(arguments='{"location": "Mexico", "unit": "celsius"}', name='get_current_weather'), id='call_4c8883be-a1e7-40a7-ac15-f3f8f22c9d2c', type='function')]


#----------------------------------


# JSON Schema support

from litellm import completion

response = completion(
    model="ollama_chat/llama3.2", 
    messages=[{ "content": "respond in 20 words. who are you?","role": "user"}], 
    response_format={"type": "json_schema", "json_schema": {"schema": {"type": "object", "properties": {"name": {"type": "string"}}}}},
)
print(response)
# Out[]:
ModelResponse(id='chatcmpl-99febd97-c2aa-4842-b666-9578ea5ece80', created=1745750756, 
model='ollama_chat/llama3.2', object='chat.completion', system_fingerprint=None, 
choices=[Choices(finish_reason='stop', index=0, 
message=Message(content='{} ', 
role='assistant', 
tool_calls=None, 
function_call=None, 
provider_specific_fields=None))], usage=Usage(completion_tokens=3, prompt_tokens=35, 
total_tokens=38, completion_tokens_details=None, prompt_tokens_details=None))

response = completion(
    model="ollama_chat/phi4-mini", 
    messages=[{ "content": "respond in 20 words. who are you?","role": "user"}], 
    response_format={"type": "json_schema", "json_schema": {"schema": {"type": "object", "properties": {"name": {"type": "string"}}}}},
)
print(response)
# Out[]:
ModelResponse(id='chatcmpl-16fd11ba-0eb5-42a2-81c7-ecd31c271e04', created=1745750909, 
model='ollama_chat/phi4-mini', object='chat.completion', system_fingerprint=None, 
choices=[Choices(finish_reason='stop', index=0, 
message=Message(content='{"name": "ChatGPT assistant"}', 
role='assistant', 
tool_calls=None, 
function_call=None, 
provider_specific_fields=None))], usage=Usage(completion_tokens=9, 
prompt_tokens=13, total_tokens=22, completion_tokens_details=None, prompt_tokens_details=None))

response = completion(
    model="ollama_chat/gemma3:1b", 
    messages=[{ "content": "respond in 20 words. who are you?","role": "user"}], 
    response_format={"type": "json_schema", "json_schema": {"schema": {"type": "object", "properties": {"name": {"type": "string"}}}}},
)
print(response)
# Out[]:
ModelResponse(id='chatcmpl-91f04e58-21d0-42f0-bc58-9b92e5321246', created=1745751079, 
model='ollama_chat/gemma3:1b', object='chat.completion', system_fingerprint=None, 
choices=[Choices(finish_reason='stop', index=0, 
message=Message(content='{"name": " Gemma, an open-weights AI assistant created by the Gemma \
team at Google DeepMind."}', 
role='assistant', 
tool_calls=None, 
function_call=None, 
provider_specific_fields=None))], usage=Usage(completion_tokens=24, prompt_tokens=20, 
total_tokens=44, completion_tokens_details=None, prompt_tokens_details=None))

response = completion(
    model="ollama_chat/gemma3:12b", 
    messages=[{ "content": "respond in 20 words. who are you?","role": "user"}], 
    response_format={"type": "json_schema", "json_schema": {"schema": {"type": "object", "properties": {"name": {"type": "string"}}}}},
)
print(response)                                                                  
# Out[]: # NOT WORKING
ModelResponse(id='chatcmpl-159f9e77-35f6-41e6-8745-0597a92efdf2', created=1745862518, 
model='ollama_chat/gemma3:12b', object='chat.completion', system_fingerprint=None, 
choices=[Choices(finish_reason='stop', index=0, 
message=Message(content='{\n\n}\n\n \t \t \t \t \t \t \t \t \t \t', # <-- NO ANSWER
role='assistant', 
tool_calls=None, 
function_call=None, provider_specific_fields=None))], 
usage=Usage(completion_tokens=25, prompt_tokens=20, total_tokens=45, 
completion_tokens_details=None, prompt_tokens_details=None))  

response = completion(
    model="ollama_chat/gemma3:27b", 
    messages=[{ "content": "respond in 20 words. who are you?","role": "user"}], 
    response_format={"type": "json_schema", "json_schema": {"schema": {"type": "object", "properties": {"name": {"type": "string"}}}}},
)
print(response.choices[0].message.content)
# Out[]:
{"name":"Gemma"}

model = "ollama_chat/qwen3:4b"
response = completion(
    model=model, 
    messages=[{ "content": "respond in 20 words. who are you?","role": "user"}], 
    response_format={"type": "json_schema", "json_schema": {"schema": {"type": "object", "properties": {"name": {"type": "string"}}}}},
)
In [15]: print(response.choices[0].message.content)
{
  "name": "Qwen"
}

# Checking json structure
model='ollama_chat/gemma3:1b'
response = completion(
    model=model, 
    messages=[{ "content": "respond in 20 words. who are you?","role": "user"}], 
    response_format={
        "type": "json_schema", 
        "json_schema": {
            "schema": {
                "type": "object", 
                "properties": {
                    "name": {"type": "string"}
                }
            }
        }
    },
)
In [17]: print(response.choices[0].message.content)
{"name": " Gemma, a large language model created by Google DeepMind."}


