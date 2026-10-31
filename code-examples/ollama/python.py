"""
مثال استفاده از Ollama محلی (کاملاً رایگان و آفلاین)
ابتدا Ollama را نصب و یک مدل را اجرا کنید:
    ollama run llama3.2
"""

from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",  # مقدار دلخواه است
)

response = client.chat.completions.create(
    model="llama3.2",  # یا هر مدلی که با ollama pull کشیده‌اید
    messages=[
        {
            "role": "system",
            "content": "تو یک دستیار فارسی‌زبان هستی که پاسخ‌های واضح و مفید می‌دهد."
        },
        {
            "role": "user",
            "content": "یک برنامه ساده پایتون برای محاسبه فاکتوریل بنویس و توضیح بده."
        }
    ],
    temperature=0.5,
)

print(response.choices[0].message.content)
