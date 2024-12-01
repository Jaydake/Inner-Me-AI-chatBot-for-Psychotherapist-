import streamlit as st


st.set_page_config(
    page_title="Inner Me",
)

with st.sidebar:
    st.image("")
    

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
        Welcome to InnerMe – Assistant to you my Doctor.
        How may I help you.
        
    </p>
   
    <H2> Use me like  </H2> 
    <ol>
        <li class="medium-font">Submit the audio file to the  <kbd>transcript</kbd> section to receive a transcription.</li>
        <li class="medium-font">Explore  <kbd>bot</kbd> for further help through the bot</li>
    </ol>
    '''
, unsafe_allow_html=True)
