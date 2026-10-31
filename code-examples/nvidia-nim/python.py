"""
مثال استفاده از NVIDIA NIM
دسترسی به مدل‌های قوی مثل Nemotron و DeepSeek.
کلید را از https://build.nvidia.com بگیرید.
معمولاً نیاز به تأیید شماره تلفن دارد.
"""

import os
from openai import OpenAI

api_key = os.environ.get("NVIDIA_API_KEY")
if not api_key:
    raise ValueError("لطفاً متغیر محیطی NVIDIA_API_KEY را تنظیم کنید")

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=api_key,
)

def chat(prompt: str, model: str = "meta/llama-3.1-8b-instruct"):
    """
    چند مدل محبوب NVIDIA NIM:
    - meta/llama-3.1-8b-instruct
    - meta/llama-3.1-70b-instruct
    - nvidia/nemotron-4-340b-instruct
    - deepseek-ai/deepseek-r1
    - microsoft/phi-3-medium-128k-instruct
    """
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": "تو یک دستیار هوشمند و فنی هستی. پاسخ‌ها را به زبان فارسی و دقیق بده."
            },
            {"role": "user", "content": prompt}
        ],
        temperature=0.5,
        max_tokens=1024,
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    پاسخ = chat("تفاوت اصلی بین Inference و Training در مدل‌های زبانی چیست؟")
    print(پاسخ)
