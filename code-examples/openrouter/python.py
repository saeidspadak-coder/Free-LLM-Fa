"""
مثال استفاده از OpenRouter
دسترسی به صدها مدل از طریق یک API واحد.
مدل‌هایی که پسوند :free دارند کاملاً رایگان هستند.
کلید را از https://openrouter.ai/keys بگیرید.
"""

import os
from openai import OpenAI

api_key = os.environ.get("OPENROUTER_API_KEY")
if not api_key:
    raise ValueError("لطفاً متغیر محیطی OPENROUTER_API_KEY را تنظیم کنید")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
    default_headers={
        "HTTP-Referer": "https://github.com/saeidspadak-coder/Free-LLM-Fa",  # اختیاری ولی توصیه می‌شود
        "X-Title": "Free-LLM-Fa",
    }
)

def chat(prompt: str, model: str = "meta-llama/llama-3.3-70b-instruct:free"):
    """
    چند مدل رایگان محبوب:
    - meta-llama/llama-3.3-70b-instruct:free
    - google/gemma-2-9b-it:free
    - mistralai/mistral-7b-instruct:free
    - qwen/qwen-2.5-7b-instruct:free
    - microsoft/phi-3-mini-128k-instruct:free
    """
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": "تو یک دستیار هوشمند و مفید هستی. پاسخ‌ها را به زبان فارسی و واضح بده."
            },
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=1500,
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    پاسخ = chat("یک توضیح کوتاه و کاربردی درباره مفهوم Context Window در مدل‌های زبانی بده.")
    print(پاسخ)
