import streamlit as st

from scrape import (
    scrape_website,
    # extract_body_content, #under Work 
    clean_body_content,
    split_dom_content,
)
from parse import parse_with_ollama

# Streamlit UI
st.title("AI Web Scraper")


# Streamlit UI
st.title("AI Web Scraper")

# Add a radio button for browser selection
browser_choice = st.radio(
    "Select Browser for Scraping:",
    ("Chrome", "Firefox"),
    index=0 # Default to Chrome
)

url = st.text_input("Enter Website URL")

# Step 1: Scrape the Website
if st.button("Scrape Website"):
    if url:
        st.write(f"Scraping the website using {browser_choice}...")

        try:
            # Pass the selected browser type to the scrape_website function
            dom_content = scrape_website(url, browser_type=browser_choice.lower())

            # Note: extract_body_content was not in the previous scrape.py.
            # Assuming scrape_website already returns the full HTML or you'll handle extraction.
            # For now, I'll assume scrape_website returns the full HTML and clean_body_content processes it.
            # If extract_body_content is truly needed, you'll need to add it to scrape.py.
            # For this example, I'm directly passing dom_content to clean_body_content.
            cleaned_content = clean_body_content(dom_content)

            # Store the DOM content in Streamlit session state
            st.session_state.dom_content = cleaned_content

            # Display the DOM content in an expandable text box
            with st.expander("View Cleaned DOM Content"):
                st.text_area("Cleaned DOM Content", cleaned_content, height=300)

        except Exception as e:
            st.error(f"An error occurred during scraping: {e}")
            st.info("Please ensure your remote WebDriver service is running and configured for the selected browser.")

# Step 2: Ask Questions About the DOM Content
if "dom_content" in st.session_state:
    st.markdown("---") # Separator for better UI
    st.subheader("Ask Questions About the Scraped Content")
    parse_description = st.text_area("Describe what you want to parse (e.g., 'Extract all product names and their prices')")

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content with Ollama...")

            try:
                dom_chunks = split_dom_content(st.session_state.dom_content)
                parsed_result = parse_with_ollama(dom_chunks, parse_description)
                st.write("### Parsed Result:")
                st.write(parsed_result)
            except Exception as e:
                st.error(f"An error occurred during parsing: {e}")
                st.info("Please ensure your Ollama service is running and accessible.")
        else:
            st.warning("Please provide a description of what you want to parse.")
else:
    st.info("Scrape a website first to enable the parsing section.")