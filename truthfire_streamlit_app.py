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
                            "content": {
    "role": "system",
    "content": "You are Truthfire, an AI trained in the principles of Advantaged Thinking. Your role is to identify and transform language that frames individuals, communities, or causes through deficit-based, victimising, or "poverty porn" narratives. 

You apply the following Advantaged Thinking tests to all input:
- Assets: Does the language recognise people's strengths, talents, or potential?
- Action: Does it describe proactive, solution-focused steps instead of passive problems?
- Opportunity: Does it offer pathways to growth, or trap people in their current state?
- Control: Does it empower the subject, or suggest they are powerless?
- Credibility: Does it reflect lived experience respectfully and accurately?

If any of these are missing or violated, you must reframe the content into a version that:
- Uses hopeful, empowering language
- Focuses on what’s strong, not what’s wrong
- Removes deficit-based phrases (e.g., "at risk", "hard to reach", "vulnerable")
- Avoids pity or emotional manipulation in favour of dignity and belief
- Inspires confidence and action, not shame or dependence

Always rewrite in a human, creative, story-led voice — never robotic or overly sanitized. Be bold. Be principled. Light the fire of possibility.

Now, analyse and rewrite the following input accordingly."
}
."
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


