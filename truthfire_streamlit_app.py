
import streamlit as st
import openai
import os

st.set_page_config(page_title="Truthfire", layout="centered")
st.title("🔥 Truthfire – Rewrite With Purpose")
st.write("Paste your strategy, policy or comms text below. We'll rewrite it using Advantaged Thinking and Strong Truths.")

# User input
input_text = st.text_area("Your original text", height=200)

# OpenAI API key
openai_api_key = st.text_input("Enter your OpenAI API key", type="password")

# Button to trigger rewrite
if st.button("Ignite Truthfire"):
    if not input_text.strip():
        st.warning("Please paste some text to rewrite.")
    elif not openai_api_key.strip():
        st.warning("Please enter your OpenAI API key.")
    else:
        with st.spinner("Rewriting with purpose..."):
            openai.api_key = openai_api_key
            prompt = f"""
You are Truthfire, an AI rewriting tool for strategies and communications using Advantaged Thinking and Strong Truths. 
Rewrite the following text using empowering, strengths-based, human-centred language. Then explain why you made the changes.
TEXT: {input_text}
            """
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.7,
                    max_tokens=1000
                )
                output = response['choices'][0]['message']['content']
                st.subheader("🔥 Rewritten Text + Reflection")
                st.text_area("Truthfired Output", output, height=400)
            except Exception as e:
                st.error(f"Error: {e}")
