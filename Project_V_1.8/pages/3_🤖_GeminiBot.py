import streamlit as st 
import google.generativeai as genai
import numpy as np
import pandas as pd 
import textwrap

st.set_page_config(
    page_title="InnerMe",
    page_icon=":cyclone:"
)

# Sidebar
with st.sidebar:
    st.success('''
               Try out this question: 
               > **What stops the patient from doing her job?**  
               > Don't forget to say **Thank you**     
               ''')
    st.markdown("**Note**: if the Questions are not included in the passage it won't respond ")

# Directly include Gemini API key
gemini_api = "AIzaSyCaDc5DQshbiyouwOTj3Sop3CFreJw3egg"  # Replace this with your actual API key
genai.configure(api_key=gemini_api)
model = genai.GenerativeModel('gemini-pro')

# Load transcript
with open("./assets/documents/Social_Anxiety.txt") as f:
    trans = f.read()

# Define chunking function
def chunk(text):
    return text.split("\n\n")  # Alternative chunking method

tran = chunk(trans)

# Embed transcripts
@st.cache_data(show_spinner=False)
def embed_trans(tran):
    model = "models/embedding-001"
    return genai.embed_content(
        model=model,
        content=tran,
        task_type="retrieval_document",
        title='transcription embedding'
    )['embedding']

# Semantic search embedding
@st.cache_data(show_spinner=False)
def find_best_passage(prompt, dataframe):
    model = "models/embedding-001"
    query_embedding = genai.embed_content(
        model=model,
        content=prompt,
        task_type="retrieval_query"
    )
    dot_products = np.dot(np.stack(dataframe['Embedding']), query_embedding["embedding"])
    idx = np.argmax(dot_products)
    return dataframe.iloc[idx]['Text']

# Gemini's personality prompt
def make_prompt(query, relevant_passage):
    escaped = relevant_passage.replace("'", "").replace('"', "").replace("\n", " ")
    prompt = textwrap.dedent("""You are a helpful and informative bot that answers questions using text from the reference passage included below.
    Be sure to respond in a complete sentence, being comprehensive, including all relevant background information.
    However, you are talking to a doctor, so strike a friendly and conversational tone. 
    QUESTION: '{query}'
    PASSAGE: '{relevant_passage}'

    ANSWER:
    """).format(query=query, relevant_passage=escaped)
    return prompt

# Create dataframe
df = pd.DataFrame(tran, columns=['Text'])
df['Embedding'] = df['Text'].apply(embed_trans)

# Chatbot interface
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

if prompt := st.chat_input("Say something"):
    embed = find_best_passage(prompt=prompt, dataframe=df)
    with st.chat_message('user'):
        st.markdown(prompt)
    st.session_state.messages.append({"role": 'user', "content": prompt})
        
    with st.chat_message('assistant'):
        message_place = st.empty()
        full_response = ""
        query = make_prompt(prompt, embed)
        for response in model.generate_content(query):
            full_response += (response.text or "")
            message_place.markdown(full_response + " ")
        message_place.markdown(full_response)
        st.session_state.messages.append({"role": 'assistant', "content": full_response})
