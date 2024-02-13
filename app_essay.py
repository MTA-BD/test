# Import necessary libraries
import streamlit as st
from openai import OpenAI
import time

# Set API key for OpenAI (replace with your actual API key)
client = OpenAI(api_key="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")

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
topic = st.text_input("What is the topic?", "")
point_no = st.number_input("How many points will be in the essay?", min_value=1, value=3)
subp_no = st.number_input("How many subpoints will be in the essay?", min_value=1, value=2)

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
    prompt = f"Suppose you are an expert in English language and Essay writing with an experience of 30 years. Now you have to help me in writing an essay about {topic} Begin by writing an awesome title for the essay. Then, you have to write an extraordinary and unique Topic sentence for the essay. Write the topic sentence in different sections. Then write an introduction paragraph. Then write {point_no} points on the topic sentence for the essay. Then add the description for each point. Remember to provide the descriptions in more than {subp_no} subpoints for each main point. Remember that the main points of the essay must be related and led by the Topic sentence. Keep the main points unique from one another. Remember to give information in the essay where needed. Add reference of the information. But don't use information too much. Add one real quote of a famous person completely related to the point of the essay. Don't give any kind of unreal quote which was not told by any speaker. Also, the reference of the quote that means by whom, where, and when the quote was told must be added beside the quote. Remember to give an idea of the main idea of the essay and the ideas of each main point in the introduction paragraph. You must write the introduction paragraph as like as the reader will be highly interested in the essay. But don't give the spoiler and the whole thing in the intro paragraph; so that the reader will be interested in reading the whole paragraph. At last, write a conclusion point. In the conclusion paragraph, summarize the whole essay in a few sentences. But keep in mind that the intro and conclusion para won't be completely the same. Bold and Highlight the words which are like the ornaments of the sentences or the artistic words, which will bear the witness of language proficiency, of the introduction and conclusion para. Also, write real quotes for the intro and the conclusion paragraph. If you use any artistic word or sentences, give the explanation of those in understandable and easy language; so that I can understand them properly."

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

# Footer
st.markdown(
    "<p style='text-align: center; font-size: small; color: #7041ce; margin-top: 20px;'>Developed by Md. Taseen Alam</p>",
    unsafe_allow_html=True,
)
