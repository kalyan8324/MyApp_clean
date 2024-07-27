import streamlit as st
import requests

st.title("Chat application")
placeholder = st.empty()
id = st.text_input("Enter your search query",key="placeholder")

if st.button("Fetch Data"):
    with st.spinner("Featching data..."):
        try:
            resp = requests.get("http://127.0.0.1:8001/getCrash")
            data = resp.json()
            if resp.status_code == 200:
                st.write(resp.json())
            else:
                st.write(data)
        except requests.exceptions.HTTPError as http_err:
            st.error(f"HTTP error occurred: {http_err}")
        except Exception as e:
            st.error(f"An error occurred: {e}")


# with st.chat_message("user"):

st.sidebar.header("Additional Options")

if st.sidebar.checkbox("History"):
    if 'data' in locals():
        st.json(data)
    else:
        st.write("No data to display")



        
