"""
مثال استفاده از Cloudflare Workers AI
رایگان، بدون نیاز به کارت بانکی، مناسب مدل‌های متن‌باز.
کلید و Account ID را از داشبورد Cloudflare بگیرید.
"""

import os
from openai import OpenAI

# برای Cloudflare معمولاً به Account ID و API Token نیاز دارید
account_id = os.environ.get("CLOUDFLARE_ACCOUNT_ID")
api_token = os.environ.get("CLOUDFLARE_API_TOKEN")

if not account_id or not api_token:
    raise ValueError(
        "لطفاً متغیرهای CLOUDFLARE_ACCOUNT_ID و CLOUDFLARE_API_TOKEN را تنظیم کنید.\n"
        "از داشبورد Cloudflare → Workers AI یا Account Settings می‌توانید آن‌ها را بگیرید."
    )

client = OpenAI(
    base_url=f"https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/v1",
    api_key=api_token,
)

def chat(prompt: str, model: str = "@cf/meta/llama-3.1-8b-instruct"):
    """
    چند مدل محبوب Cloudflare:
    - @cf/meta/llama-3.1-8b-instruct
    - @cf/meta/llama-3.2-3b-instruct
    - @cf/qwen/qwen1.5-14b-chat-awq
    - @cf/mistral/mistral-7b-instruct-v0.2
    - @cf/google/gemma-2-9b-it
    """
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": "تو یک دستیار فارسی‌زبان هستی که پاسخ‌های دقیق و مفید می‌دهد."
            },
            {"role": "user", "content": prompt}
        ],
        temperature=0.6,
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    پاسخ = chat("مفهوم Rate Limit در APIها چیست و چرا مهم است؟")
    print(پاسخ)
