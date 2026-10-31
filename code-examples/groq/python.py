"""
مثال استفاده از Groq با کتابخانه OpenAI
Groq یکی از بهترین گزینه‌های رایگان از نظر سرعت است.
"""

import os
from openai import OpenAI

# کلید را از متغیر محیطی بخوانید (توصیه می‌شود)
api_key = os.environ.get("GROQ_API_KEY")
if not api_key:
    raise ValueError("لطفاً متغیر محیطی GROQ_API_KEY را تنظیم کنید")

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=api_key,
)

def chat(prompt: str, model: str = "llama-3.3-70b-versatile"):
    """ارسال یک پیام و دریافت پاسخ"""
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": "تو یک دستیار هوشمند، دقیق و مفید هستی. همیشه به زبان فارسی پاسخ بده مگر اینکه خلاف آن خواسته شود."
            },
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=2048,
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    پاسخ = chat("تفاوت اصلی بین مدل‌های Transformer و معماری‌های قدیمی‌تر مثل RNN چیست؟")
    print(پاسخ)
