import streamlit as st
from openai import OpenAI

st.title("Truthfire - Advantaged Thinking AI")

api_key = st.text_input("Enter your OpenAI API key:", type="password")

if api_key:
    client = OpenAI(api_key=api_key)

    user_input = st.text_area("Enter your text to transform:", height=200)

    if st.button("Generate"):
        if user_input.strip() == "":
            st.warning("Please enter some text.")
        else:
            with st.spinner("Generating..."):
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {
                            "role": "system",
                            "content": "You are Truthfire, an AI that rewrites language into Advantaged Thinking aligned with Strong Truths."
                        },
                        {
                            "role": "user",
                            "content": user_input
                        }
                    ],
                )
                result = response.choices[0].message.content
                st.success("Done!")
                st.text_area("Output:", value=result, height=200)
else:
    st.info("Please enter your OpenAI API key to use the app.")


