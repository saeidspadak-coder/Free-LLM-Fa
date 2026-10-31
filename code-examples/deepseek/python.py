"""
مثال استفاده از DeepSeek
مدل‌های قوی و مقرون‌به‌صرفه (گاهی لایه‌های رایگان یا اعتبار آزمایشی دارد).
کلید را از https://platform.deepseek.com دریافت کنید.
"""

import os
from openai import OpenAI

api_key = os.environ.get("DEEPSEEK_API_KEY")
if not api_key:
    raise ValueError("لطفاً متغیر محیطی DEEPSEEK_API_KEY را تنظیم کنید")

client = OpenAI(
    base_url="https://api.deepseek.com",
    api_key=api_key,
)

def chat(prompt: str, model: str = "deepseek-chat"):
    """
    مدل‌های اصلی:
    - deepseek-chat          (عمومی)
    - deepseek-reasoner      (استدلال قوی‌تر)
    """
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": "تو یک دستیار هوشمند، دقیق و مفید هستی. پاسخ‌ها را به زبان فارسی ارائه کن."
            },
            {"role": "user", "content": prompt}
        ],
        temperature=0.6,
        max_tokens=2048,
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    پاسخ = chat("تفاوت بین Zero-shot، Few-shot و Chain-of-Thought prompting چیست؟")
    print(پاسخ)
