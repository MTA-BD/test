# Import necessary libraries
import streamlit as st
from openai import OpenAI
import time

# Set API key for OpenAI (replace with your actual API key)
client = OpenAI(api_key=st.secrets.key_nai)

# Streamlit app configuration
st.set_page_config(
    page_title="Essay Express Pro",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Set the header color
st.markdown(
    "<h1 style='text-align: center; color: #7041ce;'>Essay Express Pro</h1>",
    unsafe_allow_html=True,
)


# Subheader with description
st.markdown(
    "<h3 style='color: #7041ce;'>Turbocharge Your Essay Writing Genius with Custom Key Points in Minutes!</h3>",
    unsafe_allow_html=True,
)

# Description text in small fonts
st.markdown(
    "<p style='font-size: small; color: #7041ce;'>Note: Basically it tells you what to write and how to write (Key point brainstorming), but writing depends on your creativity.</p>",
    unsafe_allow_html=True,
)

# Input boxes for user prompts
topic = str(st.text_input("What is the topic?", ""))
point_no = str(st.number_input("How many points will be in the essay?", min_value=1, value=3))
subp_no = str(st.number_input("How many subpoints will be in the essay?", min_value=1, value=2))

# Function to interact with OpenAI API
def Basic_G(userPrompt):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": userPrompt}],
    )
    return completion.choices[0].message.content

# Function to generate essay
def generate_essay():
    # Generate user prompt based on inputs
    prompt =st.secrets.a+topic+st.secrets.b+point_no+st.secrets.c+subp_no+st.secrets.d
    
    # Display loading message
    with st.spinner("Polishing your essay, almost there!"):
        time.sleep(2)  # Simulate the essay generation process
        # Call OpenAI API and get response
        response = Basic_G(prompt)

    # Display the generated essay
    st.markdown(
        f"<div style='border: 1px solid #7041ce; padding: 10px; margin-top: 20px;'><p style='font-weight: bold; color: #7041ce;'>Generated Essay:</p>{response}</div>",
        unsafe_allow_html=True,
    )

# Button to generate essay
if st.button("Generate Essay"):
    generate_essay()
