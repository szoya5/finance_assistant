import streamlit as st
from agents.api_agent import get_asia_tech_risk
from agents.scrapping_agent import get_earnings_news
from agents.analysis_agent import get_aum_change, earnings_summary
from agents.language_agent import generate_brief
from agents.voice_agent import speech_to_text, text_to_speech

st.set_page_config(page_title="🧠 Finance Assistant", layout="centered")
st.title("🧠 Morning Market Brief - Voice Assistant")

st.markdown("Ask: _What’s our risk exposure in Asia tech stocks today, and highlight any earnings surprises?_")

input_mode = st.radio("Choose input mode", ["🎤 Voice", "⌨️ Button"])

query = ""
if input_mode == "🎤 Voice":
    if st.button("Record Voice"):
        query = speech_to_text()
        st.write("You said:", query)
else:
    if st.button("Get Market Brief"):
        query = "What's our risk exposure in Asia tech stocks today?"

if query:
    stocks = get_asia_tech_risk(['TSM', 'SSNLF'])
    news = get_earnings_news()
    earnings = earnings_summary(stocks)
    aum_change = get_aum_change(22, 18)
    narrative = generate_brief(query)

    final_brief = (
        f"Today, your Asia tech allocation is 22% of AUM, up from 18% yesterday.\n\n"
        f"Earnings Summary: {earnings}.\n\n"
        f"Top Headlines:\n" + "\n".join([f"- {h}" for h in news]) + "\n\n"
        f"{narrative}"
    )

    st.success(final_brief)
    text_to_speech(final_brief)
