# finance_assistant

# 🧠 Multi-Agent Finance Assistant (Voice-Enabled)

This project is a multi-agent, multi-source financial assistant that answers:

> “What’s our risk exposure in Asia tech stocks today, and highlight any earnings surprises?”

It integrates real-time stock data, web scraping, document retrieval, local LLM-based narrative generation, and a simple Streamlit UI for interaction.

---

## 🎯 Use Case

Every trading day at 8 AM, a portfolio manager asks:

> _“What’s our risk exposure in Asia tech stocks today, and highlight any earnings surprises?”_

The assistant responds with a dynamic spoken or written brief that includes:
- Risk % change in Asian tech stocks
- Recent earnings surprises
- Regional financial sentiment based on vector-retrieved documents

---

## 🏗 Architecture

User (Voice/Text)
↓
Streamlit App UI
↓
[API Agent] → yfinance: stock % change
[Scraping Agent] → BeautifulSoup: top headlines
[Retriever Agent] → FAISS: embeds + searches context
[Analysis Agent] → AUM % change, earnings logic
[Language Agent] → flan-t5-small LLM (transformers)
↓
Generated Market Brief → Text (TTS optional)


Deployment (Hugging Face or Streamlit Cloud)
1. Place app.py in the root

2. Disable/remove text_to_speech() calls

3. Make sure requirements.txt includes:

  streamlit(app.py)
  faiss-cpu
  sentence-transformers

4. Push to Hugging Face Spaces or Streamlit Cloud


