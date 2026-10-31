# راهنمای مبتدیان — از صفر تا اولین درخواست رایگان

این راهنما برای کسانی نوشته شده که تازه می‌خواهند با APIهای رایگان LLM کار کنند.

## پیش‌نیازها

- یک حساب ایمیل (Gmail یا هر چیز دیگر)
- پایتون نصب‌شده (نسخه ۳.۹ یا بالاتر توصیه می‌شود)
- آشنایی خیلی کم با خط فرمان

## مرحله ۱: نصب کتابخانه OpenAI

```bash
pip install openai
```

## مرحله ۲: گرفتن کلید رایگان از Groq (پیشنهادی)

1. به آدرس [https://console.groq.com](https://console.groq.com) بروید.
2. با گوگل یا ایمیل ثبت‌نام کنید.
3. از منوی سمت چپ روی **API Keys** کلیک کنید.
4. **Create API Key** را بزنید و نامی برای آن بگذارید.
5. کلید را کپی کنید (فقط یک بار نشان داده می‌شود).

## مرحله ۳: نوشتن اولین کد

فایلی به نام `test_groq.py` بسازید و کد زیر را داخل آن بگذارید:

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key="کلید_خودتان_را_اینجا_بگذارید"
)

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "user", "content": "سلام! خودت را معرفی کن و بگو امروز چه کمکی می‌توانی به من بکنی؟"}
    ]
)

print(response.choices[0].message.content)
```

سپس اجرا کنید:

```bash
python test_groq.py
```

اگر پاسخ فارسی یا انگلیسی دریافت کردید، تبریک می‌گوییم! شما اولین درخواست رایگان خود را با موفقیت فرستادید.

## مرحله ۴: بهتر کردن کد (امنیت)

بهتر است کلید را مستقیماً در کد ننویسید. از متغیر محیطی استفاده کنید:

```bash
# در لینوکس/مک
export GROQ_API_KEY="کلید_شما"

# در ویندوز (PowerShell)
$env:GROQ_API_KEY="کلید_شما"
```

سپس در کد:

```python
import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.environ.get("GROQ_API_KEY")
)
```

## گام‌های بعدی پیشنهادی

1. مدل‌های مختلف Groq را امتحان کنید.
2. Google AI Studio را هم امتحان کنید (مدل‌های Gemini).
3. راهنمای [local-setup.md](local-setup.md) را بخوانید تا مدل‌ها را روی سیستم خودتان اجرا کنید.
4. با ابزارهایی مثل Cursor یا Continue.dev کار کنید.

موفق باشید!
