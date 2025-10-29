from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",
)

models = [
    "huggingfaceh4/zephyr-7b-beta:free",
    "meta-llama/llama-3-8b-instruct:free",
    "microsoft/wizardlm-2-8x22b:free", 
    "google/gemma-7b-it:free",
    "nousresearch/hermes-2-pro-mistral-7b:free",
    "gryphe/mythomist-7b:free",
    "openchat/openchat-7b:free",
    "cognitivecomputations/dolphin-2.6-mistral-7b:free",
    "undi95/remm-slerp-l2-13b:free",
    "pygmalionai/mythalion-13b:free"
]

for model in models:
    try:
        completion = client.chat.completions.create(
            extra_headers={
                "HTTP-Referer": "http://localhost:3000",
                "X-Title": "Test App",
            },
            model=model,
            messages=[{"role": "user", "content": "Say 'hello'"}],
            max_tokens=10
        )
        print(f"работает: {model}")
        break  
    except Exception as e:
        print(f"не работает: {model}")
