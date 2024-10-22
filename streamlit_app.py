import streamlit as st

st.title("🎈 My new Streamlit app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

# Everything is accessible via the st.secrets dict:
st.write("OPENAPI_API_KEY:", st.secrets["OPENAPI_API_KEY"]) 

# Store the value in "Environment Variable"
# This is required by some packages like LangChain
os.environ['OPENAPI_API_KEY'] = st.secrets['OPENAPI_API_KEY']