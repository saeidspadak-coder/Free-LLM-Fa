<p align="center">
  <h1 align="center">Free-LLM-Fa — دایرکتوری کامل APIها و مدل‌های رایگان هوش مصنوعی</h1>
  <p align="center">
    <strong>بیش از ۲۷۰ مدل رایگان از ۵۱ ارائه‌دهنده</strong> + ابزارهای محلی برای استفاده نامحدود و خصوصی
  </p>
</p>

<p align="center">
  <a href="https://free-llm.com" target="_blank"><strong>🌐 نسخه اصلی (انگلیسی)</strong></a> ·
  <a href="#شروع-سریع">شروع سریع</a> ·
  <a href="#دایرکتوری-ارائه‌دهندگان">لیست ارائه‌دهندگان</a> ·
  <a href="#راهنماها">راهنماها</a>
</p>

<p align="center">
  <img alt="License" src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" />
  <img alt="Community" src="https://img.shields.io/badge/Community-Driven-orange?style=for-the-badge" />
  <img alt="Language" src="https://img.shields.io/badge/زبان-فارسی-blue?style=for-the-badge" />
  <img alt="Updated" src="https://img.shields.io/badge/به‌روزرسانی-اکتبر_۲۰۲۶-purple?style=for-the-badge" />
</p>

---

## این پروژه چیست؟

**Free-LLM-Fa** نسخهٔ کاملاً فارسی‌شده، گسترش‌یافته و بومی‌شده‌ی پروژهٔ معروف [nejib1/Free-LLM](https://github.com/nejib1/Free-LLM) است.

هدف ما این است که کاربران فارسی‌زبان بتوانند **بدون دردسر** و **بدون پرداخت هزینه** به بهترین مدل‌های زبانی بزرگ (LLM) دسترسی داشته باشند — چه از طریق APIهای ابری رایگان و چه با اجرای مدل‌های متن‌باز روی سیستم خودشان.

### چرا این نسخه را ساختیم؟

- ترجمه کامل و دقیق به فارسی روان
- اضافه کردن بخش‌های آموزشی مخصوص مبتدیان
- راهنمای انتخاب مدل بر اساس نیاز (کدنویسی، چت، تحقیق، تولید محتوا)
- نکات کاربردی برای کاربران ایرانی (محدودیت‌های دسترسی، پیشنهادهای جایگزین)
- مثال‌های کد با کامنت فارسی
- گسترش بخش ابزارهای محلی و سلف‌هاست
- راهنمای اتصال به ابزارهای محبوب مثل Cursor، Claude Code، Continue.dev و غیره

---

## ویژگی‌های کلیدی

| ویژگی | توضیح |
|-------|-------|
| **۵۱+ ارائه‌دهنده رایگان** | از جمله Groq، Google AI Studio، OpenRouter، Cloudflare، NVIDIA NIM و ... |
| **شفافیت کامل** | مشخص شده آیا کارت بانکی یا تأیید شماره تلفن لازم است یا خیر |
| **کد آماده** | مثال‌های Python، JavaScript و curl برای تقریباً همه ارائه‌دهندگان |
| **ابزارهای محلی** | Ollama، LM Studio، llama.cpp و ... برای استفاده کاملاً آفلاین و خصوصی |
| **به‌روزرسانی مداوم** | همگام با نسخه اصلی free-llm.com |
| **راهنمای فارسی** | آموزش گام‌به‌گام برای مبتدی تا پیشرفته |

---

## شروع سریع (کمتر از ۲ دقیقه)

### ۱. انتخاب یک ارائه‌دهنده خوب برای شروع

پیشنهاد ما برای شروع:

| رتبه | ارائه‌دهنده | نیاز به کارت؟ | محدودیت تقریبی | مناسب برای |
|------|-------------|---------------|----------------|------------|
| ۱ | **Groq** | خیر | ۳۰ درخواست در دقیقه / ۱۴٬۴۰۰ در روز | سرعت بسیار بالا، چت و کدنویسی |
| ۲ | **Google AI Studio** | خیر | محدودیت‌های مدل به مدل | مدل‌های Gemini قوی |
| ۳ | **OpenRouter** (مدل‌های `:free`) | خیر | ۵۰ درخواست در روز | دسترسی به مدل‌های متنوع |
| ۴ | **Cloudflare Workers AI** | خیر | ۱۰٬۰۰۰ نورون در روز | مدل‌های متن‌باز خوب |

### ۲. گرفتن API Key

- برای **Groq**: به [console.groq.com](https://console.groq.com) بروید → Keys → Create API Key
- برای **Google AI Studio**: به [aistudio.google.com](https://aistudio.google.com) بروید → Get API key

### ۳. استفاده فوری با پایتون

```python
from openai import OpenAI

# مثال با Groq (رایگان و بدون کارت)
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key="کلید_API_خودتان_را_اینجا_بگذارید",  # از console.groq.com بگیرید
)

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",  # یا مدل‌های دیگر مثل qwen3-...
    messages=[
        {"role": "system", "content": "تو یک دستیار هوشمند و مفید هستی که به فارسی پاسخ می‌دهی."},
        {"role": "user", "content": "سلام! یک توضیح کوتاه درباره مدل‌های زبانی بزرگ بده."}
    ],
    temperature=0.7,
)

print(response.choices[0].message.content)
```

> **نکته:** اکثر ارائه‌دهندگان رابط سازگار با OpenAI دارند. فقط `base_url` و `api_key` را عوض کنید.

---

## دایرکتوری ارائه‌دهندگان

### لایه رایگان دائمی (Permanent Free Tiers)

این ارائه‌دهندگان دسترسی رایگان مداوم با محدودیت نرخ درخواست دارند (تمام نمی‌شود).

| ارائه‌دهنده | کارت بانکی؟ | محدودیت نرخ | محدودیت روزانه | مدل‌های کلیدی |
|-------------|------------|-------------|----------------|---------------|
| [Google AI Studio](https://aistudio.google.com/) | خیر | متغیر بر اساس مدل | متغیر | Gemini 2.5 Flash، Gemini Flash-Lite |
| [Groq](https://console.groq.com/) | خیر | ۳۰ RPM | حدود ۱۴٬۴۰۰ درخواست | Llama 3.3 70B، GPT-OSS، Qwen |
| [Cloudflare Workers AI](https://dash.cloudflare.com/) | خیر | متغیر | ۱۰٬۰۰۰ نورون | Qwen، DeepSeek، GLM |
| [Mistral AI](https://console.mistral.ai/) | تأیید تلفن | ۱ درخواست/ثانیه | - | Ministral، Codestral، Mistral Large |
| [NVIDIA NIM](https://build.nvidia.com/) | تأیید تلفن | حدود ۴۰ RPM | - | Nemotron، DeepSeek |
| [Cohere](https://cohere.com/) | خیر | ۲۰ RPM | ۱٬۰۰۰ فراخوانی/ماه | Command R+، Command A |
| [Z.AI (GLM)](https://z.ai/) | ثبت‌نام | حدود ۱ req/s | حدود ۱٬۰۰۰ | GLM-4.5/4.6/4.7 Flash |
| [OVH AI](https://endpoints.ai.cloud.ovh.net/) | ثبت‌نام | ۲ RPM (آزاد) | - | Llama 3.3 70B، GPT-OSS |
| [SiliconFlow](https://siliconflow.com/) | تأیید تلفن | ثابت (بررسی در پنل) | - | GLM، Qwen |
| [ModelScope](https://modelscope.cn) | تأیید تلفن | ۵۰۰/مدل در روز | ۲٬۰۰۰ کل | DeepSeek، GLM، MiniMax |
| [LLM7.io](https://llm7.io) | خیر | ۱ req/s | ۱۰۰٬۰۰۰ توکن | Nemotron، GLM، Mistral |
| [Hetzner Inference](https://experiments.hetzner.com/inference) | خیر | ۱۰ درخواست / ۶۰ ثانیه | بدون سقف مشخص | Qwen3 |

### اعتبارهای تجدیدپذیر (Renewable Credits)

| ارائه‌دهنده | کارت؟ | پیشنهاد رایگان | مدل‌های کلیدی |
|-------------|-------|----------------|---------------|
| [OpenRouter](https://openrouter.ai/) | خیر | ۵۰ درخواست/روز (تا ۱۰۰۰ با شارژ ۱۰ دلار) | مدل‌های :free متنوع |
| [Requesty](https://requesty.ai/) | خیر | ۲۰۰–۱۰۰۰ درخواست/روز | مدل‌های رایگان متنوع |
| [Vercel AI Gateway](https://vercel.com/ai-gateway) | ثبت‌نام | اعتبار ماهانه تقریبی ۵ دلار | - |

### اعتبارهای آزمایشی یک‌بار مصرف

| ارائه‌دهنده | مبلغ تقریبی | مدت اعتبار | نکته |
|-------------|-------------|------------|------|
| Fireworks AI | اعتبار استارتر | یک‌بار | - |
| Cerebras | ۵ دلار (با کارت) | ۳۰ روز | سرعت بسیار بالا |
| Nebius | ۱ دلار | ۳۰ روز | نیاز به کارت |
| AI21 Labs | ۱۰ دلار | محدود | - |
| Scaleway | ۱ میلیون توکن | یک‌بار | - |

> **هشدار مهم:** محدودیت‌ها و شرایط دائماً تغییر می‌کنند. همیشه صفحه رسمی ارائه‌دهنده را چک کنید. اطلاعات این ریپو بر اساس داده‌های free-llm.com به‌روز می‌شود.

---

## ابزارهای محلی و سلف‌هاست (کاملاً رایگان و خصوصی)

اگر می‌خواهید بدون محدودیت اینترنت و بدون ارسال داده به سرورهای خارجی کار کنید:

| ابزار | نوع | ویژگی برجسته | لینک |
|-------|-----|--------------|------|
| **Ollama** | CLI + API | ساده‌ترین راه اجرای مدل‌های محلی، سازگار با OpenAI | [ollama.com](https://ollama.com) |
| **LM Studio** | رابط گرافیکی | مرورگر مدل، اجرای آسان GGUF، آفلاین کامل | [lmstudio.ai](https://lmstudio.ai) |
| **llama.cpp** | موتور سبک | کمترین وابستگی، اجرای روی CPU/GPU | [GitHub](https://github.com/ggml-org/llama.cpp) |
| **GPT4All** | دسکتاپ | رابط ساده و مدل‌های آماده | [gpt4all.io](https://gpt4all.io) |
| **Jan.ai** | دسکتاپ متن‌باز | جایگزین محلی ChatGPT | [jan.ai](https://jan.ai) |
| **text-generation-webui** | وب UI پیشرفته | امکانات زیاد برای کاربران حرفه‌ای | [GitHub](https://github.com/oobabooga/text-generation-webui) |
| **KoboldCpp** | سبک و سریع | مناسب نقش‌آفرینی و تولید خلاقانه | - |

### نصب سریع Ollama (پیشنهادی)

```bash
# لینوکس / مک
curl -fsSL https://ollama.com/install.sh | sh

# سپس یک مدل خوب را بکشید
ollama run llama3.2
# یا مدل‌های قوی‌تر مثل qwen2.5، gemma2، mistral و ...
```

بعد از اجرا، API محلی روی `http://localhost:11434/v1` در دسترس است و می‌توانید با همان کد OpenAI از آن استفاده کنید.

---

## اتصال به ابزارهای کدنویسی محبوب

### Cursor
Settings → Models → Add Model → Base URL و API Key مربوط به ارائه‌دهنده رایگان را وارد کنید.

### Claude Code / Continue.dev / Cline
متغیرهای محیطی یا تنظیمات base URL را به ارائه‌دهنده رایگان تغییر دهید.

جزئیات بیشتر در پوشه [`code-examples/`](code-examples/) و فایل‌های راهنما قرار خواهد گرفت.

---

## راهنمای انتخاب مدل بر اساس نیاز

| نیاز شما | پیشنهاد اول | پیشنهاد دوم | پیشنهاد سوم |
|----------|-------------|-------------|-------------|
| کدنویسی سریع | Groq (Llama 3.3 / GPT-OSS) | Google Gemini Flash | Cloudflare Workers AI |
| استدلال و تحلیل عمیق | Gemini 2.5 Pro (رایگان محدود) | مدل‌های Reasoning در OpenRouter | مدل‌های محلی بزرگ |
| تولید متن فارسی با کیفیت | Gemini Flash / Qwen | GLM Flash | مدل‌های محلی Qwen یا Gemma |
| کار کاملاً خصوصی | Ollama + مدل محلی | LM Studio | llama.cpp |
| سرعت فوق‌العاده | Groq یا Cerebras | - | - |
| استفاده رایگان نامحدود | ابزارهای محلی | - | - |

---

## نکات مهم برای کاربران ایرانی

- بسیاری از ارائه‌دهندگان بین‌المللی بدون مشکل از ایران قابل دسترسی هستند (به خصوص آن‌هایی که فقط ایمیل می‌خواهند).
- در صورت نیاز به VPN، ارائه‌دهندگانی مثل Groq، Cloudflare و OpenRouter معمولاً پایدارتر هستند.
- برای استفاده حرفه‌ای و بدون نگرانی از قطع شدن، ترکیب چند ارائه‌دهنده + ابزار محلی بهترین راه‌حل است.
- همیشه کلیدهای API را در متغیر محیطی (`export GROQ_API_KEY=...`) نگه دارید و در کد hardcode نکنید.

---

## ساختار پروژه

```
Free-LLM-Fa/
├── README.md                 # این فایل
├── CONTRIBUTING.md           # راهنمای مشارکت
├── LICENSE                   # مجوز MIT
├── code-examples/            # مثال‌های کد برای هر ارائه‌دهنده
│   ├── groq/
│   ├── google-ai-studio/
│   ├── openrouter/
│   └── ...
├── guides/                   # راهنماهای آموزشی فارسی
│   ├── beginner.md
│   ├── local-setup.md
│   ├── coding-tools.md
│   └── best-practices.md
└── docs/                     # مستندات تکمیلی
```

---

## مشارکت

این پروژه جامعه محور است. شما می‌توانید:

- اطلاعات ارائه‌دهنده جدید یا تغییر محدودیت‌ها را گزارش دهید
- مثال کد جدید اضافه کنید
- راهنمای فارسی بنویسید یا بهبود دهید
- ترجمه را اصلاح کنید

برای جزئیات به فایل [CONTRIBUTING.md](CONTRIBUTING.md) مراجعه کنید.

---

## منابع و لینک‌های مفید

- سایت اصلی (انگلیسی): [free-llm.com](https://free-llm.com)
- ریپوی اصلی: [github.com/nejib1/Free-LLM](https://github.com/nejib1/Free-LLM)
- مقایسه ارائه‌دهندگان: [free-llm.com/compare](https://free-llm.com/compare)

---

## مجوز

این پروژه تحت مجوز **MIT** منتشر شده است. می‌توانید آزادانه استفاده، تغییر و توزیع کنید.

---

<p align="center">
  ساخته‌شده با علاقه برای جامعه فارسی‌زبان هوش مصنوعی<br>
  آخرین همگام‌سازی با داده‌های اصلی: اکتبر ۲۰۲۶
</p>
