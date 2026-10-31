"""
مثال استفاده از Google AI Studio (Gemini)
یکی از بهترین گزینه‌های رایگان با مدل‌های قوی Gemini.
کلید را از https://aistudio.google.com دریافت کنید.
"""

import os
from openai import OpenAI

api_key = os.environ.get("GOOGLE_API_KEY") or os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise ValueError("لطفاً متغیر محیطی GOOGLE_API_KEY یا GEMINI_API_KEY را تنظیم کنید")

# Google AI Studio از endpoint سازگار با OpenAI پشتیبانی می‌کند
client = OpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=api_key,
)

def chat(prompt: str, model: str = "gemini-2.0-flash"):
    """
    مدل‌های رایج:
    - gemini-2.0-flash          (سریع و رایگان)
    - gemini-2.0-flash-lite     (سبک‌تر)
    - gemini-1.5-flash
    - gemini-1.5-pro            (قوی‌تر، محدودیت بیشتر)
    """
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": "تو یک دستیار هوشمند و دقیق هستی. همیشه به زبان فارسی پاسخ بده مگر خلاف آن خواسته شود."
            },
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    پاسخ = chat("تفاوت بین fine-tuning و RAG چیست؟ به زبان ساده توضیح بده.")
    print(پاسخ)
