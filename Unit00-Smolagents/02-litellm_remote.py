
# Lap HP Pavilion 14 /dev/sda3 env: nlp (ollama: gemma3:1b, llama3.2, phi4-mini)
# 2025APR27


# CONSULTING LITELLM doc to use the litellm API with completion:
https://docs.litellm.ai/docs/providers/huggingface

import os
from litellm import completion
from dotenv import load_dotenv

USB = "KING32-2"
PATHP = "/media/clm/" + USB + "/" + \
"tech/exer/NLP/00-hugging_face/04-Agents_course/Unit00-Smolagents/"

load_dotenv(dotenv_path=PATHP + ".env")
HF_TOKEN = os.getenv("HF_TOKEN")

# WARNING: This is NON-FREE; uses credits & money from the Huggingface account.
response = completion(
    model="huggingface/google/gemma-3-1b-it",
    messages=[
        {
            "role": "user",
            "content": "How many r's are in the word 'strawberry'?",
        }
    ]
)
# Out[]:
APIError: litellm.APIError: HuggingfaceException - Model google/gemma-3-1b-it is not supported 
for provider hf-inference


response = completion(
    model="huggingface/meta-llama/Llama-3.3-70B-Instruct",
    messages=[
        {
            "role": "user",
            "content": "How many r's are in the word 'strawberry'?",
        }
    ],
    api_key=HF_TOKEN, # is optional; use if not specified in .env
)
In [11]: print(response)
ModelResponse(id='56837bb3-17cb-4f14-8391-f3c15db1e272', created=1745915777, 
model='meta-llama/Llama-3.3-70B-Instruct', object='chat.completion', 
system_fingerprint='3.2.1-sha-4d28897', 
choices=[Choices(finish_reason='stop', index=0, 
message=Message(content="There are 2 r's in the word'strawberry' and also 2 b's.", 
role='assistant', 
tool_calls=None, 
function_call=None, provider_specific_fields=None))], usage=Usage(completion_tokens=22, 
prompt_tokens=48, total_tokens=70, completion_tokens_details=None, prompt_tokens_details=None))


response = completion(
    model="huggingface/sambanova/Qwen/Qwen2.5-72B-Instruct",
    messages=[
        {
            "role": "user",
            "content": "How many r's are in the word 'strawberry'?",
        }
    ]
)
# Out[]:
APIError: litellm.APIError: HuggingfaceException - Model Qwen/Qwen2.5-72B-Instruct is not 
supported for provider sambanova


response = completion(
    model="huggingface/together/deepseek-ai/DeepSeek-R1",
    messages=[
        {
            "role": "user",
            "content": "How many r's are in the word 'strawberry'?",
        }
    ]
)
In [15]: print(response)
ModelResponse(id='ns1duVZ-zqrih-937d82ef6b5658cc', created=1745916203, 
model='deepseek-ai/DeepSeek-R1', object='chat.completion', system_fingerprint=None, 
choices=[Choices(finish_reason='stop', index=0, 
message=Message(content='\n\nThe word \'strawberry\' is spelled **S-T-R-A-W-B-E-R-R-Y**. \
Breaking it down letter by letter:\n\n1. S  \n2. T  \n3. **R**  \n4. A  \n5. W  \n6. B  \n \
7. E  \n8. **R**  \n9. **R**  \n10. Y  \n\nThe letter **r** appears **3 times** (positions 3, 8, '
'and 9). \n\n**Answer:** There are **3** r\'s in "strawberry".', 
role='assistant', 
tool_calls=None, 
function_call=None, 
reasoning_content="\nOkay, let's see. The user is asking how many times the letter 'r' appears "
"in the word 'strawberry'. Hmm, first, I need to make sure I spell the word correctly. " \
"Strawberry. S-T-R-A-W-B-E-R-R-Y. Wait, let me break it down letter by letter.\n\nStarting with " \
"the first letter: S. Then T. Next is R. That's the third letter. So that's one 'r' so far. " \
"Then A, W, B, E. After E comes R again. So that's the second 'r'. Then another R right after? 
Let me check again. S-T-R-A-W-B-E-R-R-Y. Yes, after E, there's R and then another R before Y. '
'So that's two 'r's in a row. So total of three 'r's? Wait, no. Let me count again.\n\n
Breaking it down:\n\n1. S\n2. T\n3. R (first 'r')\n4. A\n5. W\n6. B\n7. E\n8. R (second 'r')\n
9. R (third 'r')\n10. Y\n\nWait, but that's 10 letters. Let me confirm the spelling. Strawberry '
'is spelled S-T-R-A-W-B-E-R-R-Y. Yes, that's correct. So the letters are S, T, R, A, W, B, E, R, 
R, Y. So positions 3, 8, and 9 are 'r's. That makes three 'r's. But wait, I thought maybe I was 
miscounting. Let me write them out:\n\nS (1), T (2), R (3), A (4), W (5), B (6), E (7), R (8), 
R (9), Y (10). So yes, three 'r's. But wait, sometimes people might miss the double 'r' in the 
middle. Let me check another source. If I look up the spelling of strawberry, it's '
'S-T-R-A-W-B-E-R-R-Y. So the correct spelling does have two 'r's after the 'e'. So that's two 
'r's there plus the one at the beginning? Wait, no. The first 'r' is at position 3, then after 
'e' (position 7) comes two 'r's (positions 8 and 9). So total of three 'r's. But wait, no. 
Let me recount. Position 3: R. Then positions 8 and 9: R and R. So that's three 'r's total. '
'But when I spell it out, strawberry is S-T-R-A-W-B-E-R-R-Y. So letters: S, T, R, A, W, B, E, R, '
'R, Y. So that's three 'r's. Wait, but I think I might be making a mistake here. Let me check 
again. Let's write each letter with its position:\n\n1. S\n2. T\n3. R\n4. A\n5. W\n6. B\n7. E\n8. '
'R\n9. R\n10. Y\n\nYes, positions 3, 8, and 9. So three 'r's. But I'm a bit confused because 
sometimes people might think there's only two. Wait, maybe I'm overcomplicating. Let me just 
count them again. S-T-R-A-W-B-E-R-R-Y. So R is at the third letter, then after E, there are two 
R's. So that's three R's in total. Therefore, the answer should be three. But wait, I'm not sure. 
Let me check another way. Maybe I can write the word and underline each 'r':\n\nS T R A W B E R R 
Y\n\nSo the R's are at the third position, then the eighth and ninth. So three R's. Yeah, that 
seems right. So the answer is 3.\n", 
provider_specific_fields={'reasoning_content': "\nOkay, let's see. The user is asking how many "
"times the letter 'r' appears in the word 'strawberry'. Hmm, first, I need to make sure I spell "
"the word correctly. Strawberry. S-T-R-A-W-B-E-R-R-Y. Wait, let me break it down letter by "
"letter.\n\nStarting with the first letter: S. Then T. Next is R. That's the third letter. So 
that's one 'r' so far. Then A, W, B, E. After E comes R again. So that's the second 'r'. Then 
another R right after? Let me check again. S-T-R-A-W-B-E-R-R-Y. Yes, after E, there's R and then '
'another R before Y. So that's two 'r's in a row. So total of three 'r's? Wait, no. Let me count 
again.\n\nBreaking it down:\n\n1. S\n2. T\n3. R (first 'r')\n4. A\n5. W\n6. B\n7. E\n8. R (second 
'r')\n9. R (third 'r')\n10. Y\n\nWait, but that's 10 letters. Let me confirm the spelling. '
'Strawberry is spelled S-T-R-A-W-B-E-R-R-Y. Yes, that's correct. So the letters are S, T, R, A, 
W, B, E, R, R, Y. So positions 3, 8, and 9 are 'r's. That makes three 'r's. But wait, I thought 
maybe I was miscounting. Let me write them out:\n\nS (1), T (2), R (3), A (4), W (5), B (6), 
E (7), R (8), R (9), Y (10). So yes, three 'r's. But wait, sometimes people might miss the 
double 'r' in the middle. Let me check another source. If I look up the spelling of strawberry, 
it's S-T-R-A-W-B-E-R-R-Y. So the correct spelling does have two 'r's after the 'e'. So that's two 
'r's there plus the one at the beginning? Wait, no. The first 'r' is at position 3, then after 
'e' (position 7) comes two 'r's (positions 8 and 9). So total of three 'r's. But wait, no. Let 
me recount. Position 3: R. Then positions 8 and 9: R and R. So that's three 'r's total. But when '
'I spell it out, strawberry is S-T-R-A-W-B-E-R-R-Y. So letters: S, T, R, A, W, B, E, R, R, Y. So '
'that's three 'r's. Wait, but I think I might be making a mistake here. Let me check again. Let's '
'write each letter with its position:\n\n1. S\n2. T\n3. R\n4. A\n5. W\n6. B\n7. E\n8. R\n9. '
'R\n10. Y\n\nYes, positions 3, 8, and 9. So three 'r's. But I'm a bit confused because sometimes 
people might think there's only two. Wait, maybe I'm overcomplicating. Let me just count them 
again. S-T-R-A-W-B-E-R-R-Y. So R is at the third letter, then after E, there are two R's. So '
'that's three R's in total. Therefore, the answer should be three. But wait, I'm not sure. Let 
me check another way. Maybe I can write the word and underline each 'r':\n\nS T R A W B E R R Y\n
\nSo the R's are at the third position, then the eighth and ninth. So three R's. Yeah, that seems 
right. So the answer is 3.\n"}))], usage=Usage(completion_tokens=955, prompt_tokens=17, 
total_tokens=972, completion_tokens_details=None, prompt_tokens_details=None), prompt=[])


response = completion(
    model="huggingface/Qwen/QwQ-32B",
    messages=[
        {
            "role": "user",
            "content": "How many r's are in the word 'strawberry'?",
        }
    ]
)
# Out[]:
HTTPStatusError: Server error '503 Service Temporarily Unavailable' for url 'https://router.huggingface.co/hf-inference/models/Qwen/QwQ-32B/v1/chat/completions'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/503


response = completion(
    model="huggingface/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B",
    messages=[
        {
            "role": "user",
            "content": "How many r's are in the word 'strawberry'?",
        }
    ]
)
In [15]: print(response)
ModelResponse(id='8b31be05-1743-47a6-9860-a52d237f3a5f', created=1745917866, 
model='deepseek-ai/DeepSeek-R1-Distill-Qwen-32B', object='chat.completion', 
system_fingerprint='3.2.1-sha-4d28897', choices=[Choices(finish_reason='stop', index=0, 
message=Message(content="Okay, so I need to figure out how many times the letter 'r' appears in "
"the word 'strawberry.' Hmm, let me think about this step by step.\n\nFirst, I should probably "
"write out the word to visualize it better. The word is S-T-R-A-W-B-E-R-R-Y. Now, I'll go through "
"each letter one by one to count the 'r's.\n\nStarting from the beginning: S, no; T, no; R, yes, "
"that's the first 'r.' Then A, W, B, E—none of those. Next comes another R, so that's the second "
"'r.' After that, another R—wait, so that's the third 'r'? Or did I miss something? Wait no, let "
"me double-check. The word is S-T-R-A-W-B-E-R-R-Y. So after E, it's R-R-Y. So first R after E, "
"then another R before Y. So that's two R's in the end. So overall, S-T-R-A-W-B-E-R-R-Y—so the "
"first R is the third letter, and then R-R towards the end, making that two more R's. So total R's "
"are one from the third position and two from the end, which makes three R's in total. Wait, no, "
"that doesn't make sense because I should only count each occurrence, not add them up that way.\n"
"nWait, perhaps I should write the letters with their positions to be clear. Let's list them:\n\n"
"1. S\n2. T\n3. R\n4. A\n5. W\n6. B\n7. E\n8. R\n9. R\n10. Y\n\nSo looking at this list, R appears "
"at positions 3, 8, and 9. Therefore, there are three 'r's in 'strawberry.' Wait, but that feels "
"a bit high. Did I count correctly? Let me check again. The word is spelled S-T-R-A-W-B-E-R-R-Y. "
"So from S to T to R—yes, that's one R. Then after E comes R and another R before Y, so two more "
"R's. So in total, three R's. Yeah, that makes sense. So the answer should be three.\n\nWait, but "
"sometimes people might think there's only two R's because of the double R at the end. Maybe I "
"should also consider if the double R is counted as two separate R's or just one, but in reality, "
"each R is a separate occurrence. So each R in the double is counted individually. So yes, three "
"R's in total.\n</think>\n\nThe word 'strawberry' contains three 'r's. \n\n**Step-by-Step "
"Explanation:**\n\n1. **Write out the word:** S-T-R-A-W-B-E-R-R-Y.\n2. **Identify each letter and "
"its position:**\n   - 1. S\n   - 2. T\n   - 3. R\n   - 4. A\n   - 5. W\n   - 6. B\n   - 7. E\n   "
"- 8. R\n   - 9. R\n   - 10. Y\n3. **Count the 'r's:** R is at positions 3, 8, and 9.\n4. **Total "
"count:** 3 'r's.\n\n**Final Answer:** There are three 'r's in the word 'strawberry.'", 
role='assistant', tool_calls=None, function_call=None, provider_specific_fields=None))], 
usage=Usage(completion_tokens=728, prompt_tokens=18, total_tokens=746, 
completion_tokens_details=None, prompt_tokens_details=None))

# Using parameters
response = completion(
    model="huggingface/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B",
    messages=[
        {
            "role": "user",
            "content": "How many r's are in the word 'strawberry'?",
        }
    ],
    temperature = 0.5,
    max_tokens = 20
)
In [15]: print(response)
ModelResponse(id='0e6e6a40-e923-4a4c-97e8-7bd8ad56fddf', created=1745918897, 
model='deepseek-ai/DeepSeek-R1-Distill-Qwen-32B', object='chat.completion', 
system_fingerprint='3.2.1-sha-4d28897', 
choices=[Choices(finish_reason='length', index=0, 
message=Message(content="Okay, so I need to figure out how many times the letter 'r' appears in "
"the word", 
role='assistant', 
tool_calls=None, 
function_call=None, 
provider_specific_fields=None))], usage=Usage(completion_tokens=20, prompt_tokens=18, 
total_tokens=38, completion_tokens_details=None, prompt_tokens_details=None))

#---------------------------------------------

# Function Calling

You can extend the model's capabilities by giving them access to tools. Here is an example with 
function calling using Llama-3.3-70B-Instruct model through Sambanova.

import os
from litellm import completion

# Set your Hugging Face Token
os.environ["HF_TOKEN"] = "hf_xxxxxx"

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
messages = [
    {
        "role": "user",
        "content": "What's the weather like in Boston today?",
    }
]

response = completion(
    model="huggingface/sambanova/meta-llama/Llama-3.3-70B-Instruct", 
    messages=messages,
    tools=tools,
    tool_choice="auto"
)
print(response)
ModelResponse(id='faa682c1-9680-4751-89d6-9ce955ed2a56', created=1745918328.064077, 
model='Meta-Llama-3.3-70B-Instruct', object='chat.completion', system_fingerprint='fastcoe', 
choices=[Choices(finish_reason='tool_calls', index=0, 
message=Message(content=None, role='assistant', 
tool_calls=[ChatCompletionMessageToolCall(function=Function(
arguments='{"location":"Boston, MA","unit":"fahrenheit"}', name='get_current_weather'), 
id='call_06aad2cc6b0c4bbca9', type='function')], 
function_call=None, provider_specific_fields=None))], 
usage=Usage(completion_tokens=32, prompt_tokens=234, total_tokens=266, 
completion_tokens_details=None, prompt_tokens_details=None, 
completion_tokens_after_first_per_sec=414.06492005209907, 
completion_tokens_after_first_per_sec_first_ten=452.9517797796961, 
completion_tokens_per_sec=260.3722900133317, end_time=1745918328.0640328, is_last_response=True, 
start_time=1745918327.936912, stop_reason='tool_calls', 
time_to_first_token=0.05225324630737305, total_latency=0.12290094310097868, 
total_tokens_per_sec=2164.3446607358196))
