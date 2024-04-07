from llama_cpp import Llama

# Initialize the Llama instance with the path to the downloaded model
llm = Llama(
    model_path="../models/mistral-7b-instruct-v0.2.Q5_K_M.gguf",

)

user_prompt = 'What is the meaning of life?'

complete_prompt = f"[INS]You are an assistant that replies to the user's requests. Answer the user with the appropriate reply.\n\nUser: {user_prompt}[/INS]\n\nAssistant: "

output = llm(complete_prompt, max_tokens=None)

print('Output:')
print(output['choices'][0]['text'])