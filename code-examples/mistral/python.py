"""
مثال استفاده از Mistral AI (La Plateforme)
مدل‌های قوی مثل Ministral و Codestral.
کلید را از https://console.mistral.ai بگیرید.
توجه: ممکن است نیاز به تأیید شماره تلفن داشته باشد.
"""

import os
from openai import OpenAI

api_key = os.environ.get("MISTRAL_API_KEY")
if not api_key:
    raise ValueError("لطفاً متغیر محیطی MISTRAL_API_KEY را تنظیم کنید")

client = OpenAI(
    base_url="https://api.mistral.ai/v1",
    api_key=api_key,
)

def chat(prompt: str, model: str = "mistral-small-latest"):
    """
    مدل‌های رایج:
    - mistral-small-latest
    - mistral-large-latest
    - codestral-latest          (عالی برای کدنویسی)
    - ministral-8b-latest
    - open-mistral-nemo
    """
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": "تو یک دستیار هوشمند و حرفه‌ای هستی. پاسخ‌ها را به زبان فارسی و ساختاریافته بده."
            },
            {"role": "user", "content": prompt}
        ],
        temperature=0.5,
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    پاسخ = chat("تفاوت اصلی بین مدل‌های Dense و Mixture-of-Experts (MoE) چیست؟")
    print(پاسخ)
