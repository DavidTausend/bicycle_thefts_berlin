import streamlit as st

class MultiPage:
    """Framework to handle multiple Streamlit pages."""
    
    def __init__(self, app_name: str = "Multi-Page App"):
        self.app_name = app_name
        self.pages = []

    def app_page(self, title: str, func):
        """Add a new page to the app."""
        self.pages.append({"title": title, "function": func})

    def run(self):
        """Run the app with multiple pages."""
        st.sidebar.title(self.app_name)
        page = st.sidebar.radio("Navigation", self.pages, format_func=lambda page: page['title'])
        page['function']()
