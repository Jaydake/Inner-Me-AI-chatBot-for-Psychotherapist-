import streamlit as st

st.set_page_config(
    page_title="InnerMe",
    page_icon="::"
)


    

st.header(":orange[InnerMe] Assistant",
          divider="orange")
#st.title(":orange[InnerMe] Assistant ")

st.markdown("""
            <style>
            .medium-font {
                font-size:20px !important;
            }
            </style>
            """, unsafe_allow_html=True)

st.markdown(
    '''
    <p class="medium-font"> 
        Welcome to InnerMe an AI assistant for you !!
        <br> How may I assist you.
    </p>
   
    <H2> How to use me</H2> 
    <ol>
        <li class="medium-font">Submit the audio file to the  <kbd>Transcript</kbd> section so that I can get you a Summary</li>
        <li class="medium-font">Explore  <kbd>Geminibot</kbd> for me to solve your queries.</li>
    </ol>
    '''
, unsafe_allow_html=True)
