/**
 * مثال استفاده از Groq با JavaScript (Node.js)
 * نیاز به نصب: npm install openai
 *
 * کلید را از طریق متغیر محیطی تنظیم کنید:
 * export GROQ_API_KEY="کلید_شما"
 */

import OpenAI from "openai";

const client = new OpenAI({
  baseURL: "https://api.groq.com/openai/v1",
  apiKey: process.env.GROQ_API_KEY,
});

async function chat(prompt, model = "llama-3.3-70b-versatile") {
  const response = await client.chat.completions.create({
    model,
    messages: [
      {
        role: "system",
        content:
          "تو یک دستیار هوشمند و مفید هستی. همیشه به زبان فارسی پاسخ بده مگر خلاف آن خواسته شود.",
      },
      { role: "user", content: prompt },
    ],
    temperature: 0.7,
  });

  return response.choices[0].message.content;
}

// اجرای مثال
chat("مفهوم Streaming در APIهای زبانی چیست؟")
  .then((answer) => console.log(answer))
  .catch((err) => console.error("خطا:", err.message));
