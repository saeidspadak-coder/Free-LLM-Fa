# اتصال APIهای رایگان به ابزارهای کدنویسی

## Cursor

1. Settings را باز کنید (Ctrl/Cmd + ,)
2. به بخش **Models** بروید.
3. **Add Model** یا Override را انتخاب کنید.
4. Base URL و API Key مربوط به ارائه‌دهنده رایگان را وارد کنید.
5. مدل مورد نظر را انتخاب یا اضافه کنید.

مثال برای Groq:
- Base URL: `https://api.groq.com/openai/v1`
- API Key: کلید Groq شما

## Continue.dev (افزونه VS Code)

در فایل `config.json` تنظیمات زیر را اضافه کنید:

```json
{
  "models": [
    {
      "title": "Groq Llama",
      "provider": "openai",
      "model": "llama-3.3-70b-versatile",
      "apiBase": "https://api.groq.com/openai/v1",
      "apiKey": "کلید_شما"
    }
  ]
}
```

## Claude Code / Cline / سایر ایجنت‌ها

اکثر این ابزارها از متغیرهای محیطی پشتیبانی می‌کنند:

```bash
export OPENAI_BASE_URL="https://api.groq.com/openai/v1"
export OPENAI_API_KEY="کلید_شما"
```

یا برای ابزارهایی که از Anthropic استفاده می‌کنند، متغیرهای مربوطه را تنظیم کنید.

## نکته مهم

همیشه محدودیت نرخ (Rate Limit) ارائه‌دهنده را در نظر بگیرید. برای کارهای سنگین کدنویسی، ترکیب چند کلید از ارائه‌دهندگان مختلف یا استفاده از مدل محلی بهترین نتیجه را می‌دهد.
