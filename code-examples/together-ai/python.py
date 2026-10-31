"""
مثال استفاده از Together AI
پلتفرم قوی برای مدل‌های متن‌باز با سرعت خوب.
کلید را از https://api.together.xyz/settings/api-keys بگیرید.
"""

import os
from openai import OpenAI

api_key = os.environ.get("TOGETHER_API_KEY")
if not api_key:
    raise ValueError("لطفاً متغیر محیطی TOGETHER_API_KEY را تنظیم کنید")

client = OpenAI(
    base_url="https://api.together.xyz/v1",
    api_key=api_key,
)

def chat(prompt: str, model: str = "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo"):
    """
    چند مدل محبوب:
    - meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo
    - meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo
    - Qwen/Qwen2.5-7B-Instruct-Turbo
    - mistralai/Mixtral-8x7B-Instruct-v0.1
    - deepseek-ai/DeepSeek-V3
    """
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": "تو یک دستیار هوشمند و مفید هستی. همیشه به زبان فارسی پاسخ بده."
            },
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    پاسخ = chat("مفهوم Temperature در تولید متن با مدل‌های زبانی چیست؟")
    print(پاسخ)
