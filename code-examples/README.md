# مثال‌های کد (Code Examples)

در این پوشه برای هر ارائه‌دهنده اصلی، مثال آماده و قابل اجرا قرار دارد.

## ساختار

هر پوشه مربوط به یک ارائه‌دهنده است و معمولاً شامل فایل `python.py` می‌شود.

| پوشه | ارائه‌دهنده | نیاز به کلید |
|------|-------------|--------------|
| `groq/` | Groq | `GROQ_API_KEY` |
| `google-ai-studio/` | Google AI Studio (Gemini) | `GOOGLE_API_KEY` |
| `openrouter/` | OpenRouter | `OPENROUTER_API_KEY` |
| `cloudflare-workers-ai/` | Cloudflare Workers AI | `CLOUDFLARE_ACCOUNT_ID` + `CLOUDFLARE_API_TOKEN` |
| `mistral/` | Mistral AI | `MISTRAL_API_KEY` |
| `cohere/` | Cohere | `COHERE_API_KEY` |
| `nvidia-nim/` | NVIDIA NIM | `NVIDIA_API_KEY` |
| `together-ai/` | Together AI | `TOGETHER_API_KEY` |
| `deepseek/` | DeepSeek | `DEEPSEEK_API_KEY` |
| `ollama/` | Ollama (محلی) | نیازی به کلید نیست |

## نحوه استفاده کلی

1. کلید API مربوطه را از سایت ارائه‌دهنده بگیرید.
2. آن را به صورت متغیر محیطی تنظیم کنید (توصیه می‌شود):
   ```bash
   export GROQ_API_KEY="کلید_شما"
   ```
3. فایل مثال را اجرا کنید:
   ```bash
   python code-examples/groq/python.py
   ```

## نکات مهم

- تقریباً همه مثال‌ها از کتابخانه رسمی `openai` استفاده می‌کنند چون اکثر ارائه‌دهندگان رابط سازگار با OpenAI دارند.
- همیشه کلیدها را در کد hardcode نکنید.
- محدودیت نرخ (Rate Limit) هر ارائه‌دهنده را در نظر بگیرید.
- برای استفاده محلی و بدون محدودیت، پوشه `ollama` را ببینید.

اگر مثال جدیدی اضافه کردید یا خطایی پیدا کردید، خوشحال می‌شویم Pull Request بزنید.
