# 📈 MarketGuide Bot – Investment Learning & Market Commentary Assistant

Built an interactive chat-based assistant that helps users:
1. Learn investing concepts (Beginner → Intermediate).
2. Get live market commentary on request.

Crucial Constraint: This product must NOT provide buy/sell recommendations, stock tips,
or personalized advice. It acts as a coach/commentator, not an advisor.

## 🤖 Telegram Bot

The assistant is deployed as a Telegram bot and can be accessed here:

👉 **Bot Username:** `@stockmarket_coach_bot`

The bot operates using **two clearly separated modes**:
- **Coach Mode** – for learning investment concepts
- **Commentary Mode** – for understanding market movements

Any request that asks for financial advice is automatically refused and redirected to educational explanations.

---

## 🎯 Core Capabilities

### 🎓 Coach Mode (Teaching Persona)
Coach Mode focuses on **learning and clarity**.

- Explains concepts such as:
  - SIPs
  - Risk & diversification
  - ETFs
  - Long-term investing basics
- Uses simple, real-world analogies
- Designed for beginners and early intermediate users
- Explicitly avoids:
  - Stock picks
  - Buy/sell recommendations
  - Return guarantees or predictions

---

### 📰 Commentary Mode (Market News Persona)
Commentary Mode focuses on **context, not opinion**.

- Explains why markets moved on a given day
- Covers:
  - Macroeconomic factors
  - Global cues
  - Policy updates and earnings context
- Uses neutral, news-style language
- Does **not** provide forecasts, targets, or trading strategies

---

## 🛡️ Safety & Compliance Design

Safety is a **first-class requirement** in this project.

### The bot will refuse requests like:
- “Which stock should I buy?”
- “Give me intraday tips”
- “How can I get guaranteed returns?”

### Instead, it will:
- Clearly state the limitation
- Redirect users toward learning frameworks
- Encourage concept-based understanding

> All guardrails are enforced at the **application layer**, not left entirely to the language model.

---

## 🧩 Platform Overview

- User Interface: **Telegram Bot**
- Backend: **API-based architecture**
- Deployment: **Free-tier serverless hosting**
- Role: **Coach & commentator**, not an advisor

---

## ⚙️ Technology Stack

- **Backend Framework:** FastAPI (Python)
- **Language Model:** Google Gemini (`gemini-pro`)
- **Messaging API:** Telegram Bot API
- **Hosting:** Serverless deployment (Vercel / equivalent)
- **Configuration:** Environment variables (`.env`)

---

## 🏗️ System Architecture

```text
User (Telegram)
      ↓
Telegram Webhook
      ↓
FastAPI Backend
      ↓
Safety & Intent Filters
      ↓
Mode Router (Coach / Commentary)
      ↓
Prompt Construction
      ↓
Gemini Language Model
```

## 🛠️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/Stock-Market-Bot.git
cd Stock-Market-Bot
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a .env file in the project root:
```bash
GEMINI_API_KEY=your_gemini_api_key
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
```

### 4. Create a Telegram Bot

Open Telegram → @BotFather

Run /newbot

Copy the bot token and add it to .env

### 5. Run Locally (Optional)
```bash
uvicorn api.index:app --reload
```

### 6. Deploy to Vercel

Push the repo to GitHub

Import the project in Vercel

Add GEMINI_API_KEY and TELEGRAM_BOT_TOKEN as environment variables

Deploy

### 7. Set Telegram Webhook

After deployment:

https://api.telegram.org/bot<YOUR_BOT_TOKEN>/setWebhook?url=https://your-project.vercel.app/api/webhook

### 8. Test the Bot

Open Telegram and try:

/start

/mode coach

/mode market