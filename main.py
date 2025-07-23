import streamlit as st
from scrape import scrape_website

st.title("AI Web Scraper")
url = st.text_input("Enter a Url : ")

if st.button("Scrape Site"):
    st.write("Scraping Website")
    result = scrape_website(url)
    print(result)