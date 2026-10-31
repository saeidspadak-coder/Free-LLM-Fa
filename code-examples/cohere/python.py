"""
مثال استفاده از Cohere
کلید را از https://dashboard.cohere.com/api-keys بگیرید.
لایه رایگان محدودیت ماهانه دارد (حدود ۱۰۰۰ فراخوانی).
"""

import os
from openai import OpenAI

api_key = os.environ.get("COHERE_API_KEY")
if not api_key:
    raise ValueError("لطفاً متغیر محیطی COHERE_API_KEY را تنظیم کنید")

# Cohere هم endpoint سازگار با OpenAI دارد
client = OpenAI(
    base_url="https://api.cohere.com/compatibility/v1",
    api_key=api_key,
)

def chat(prompt: str, model: str = "command-r-plus-08-2024"):
    """
    مدل‌های رایج:
    - command-r-plus-08-2024
    - command-r-08-2024
    - command-a-03-2025
    - command-r7b-12-2024
    """
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": "تو یک دستیار دقیق و حرفه‌ای هستی. پاسخ‌ها را به زبان فارسی و واضح ارائه کن."
            },
            {"role": "user", "content": prompt}
        ],
        temperature=0.6,
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    پاسخ = chat("مفهوم Embedding در مدل‌های زبانی چیست و چه کاربردی دارد؟")
    print(پاسخ)
