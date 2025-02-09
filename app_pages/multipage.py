import streamlit as st


class MultiPage:
    """
    A framework to manage multiple Streamlit pages.

    Attributes:
        app_name (str): The name of the multi-page application.
        pages (list): A list to store pages, where each page is represented
        by a dictionary containing its title and function.
    """

    def __init__(self, app_name: str = "Multi-Page App"):
        """
        Initialize a MultiPage object.

        Args:
            app_name (str): The name of the multi-page application.
                            Default is "Multi-Page App".
        """
        self.app_name = app_name
        self.pages = []

    def app_page(self, title: str, func) -> None:
        """
        Add a new page to the multi-page application.

        Args:
            title (str): The title of the page to display in the sidebar.
            func (function): The function to be executed when the page is
            selected.
        """
        self.pages.append({"title": title, "function": func})

    def run(self) -> None:
        """
        Run the multi-page application. Displays a sidebar with page navigation
        and executes the selected page's function.
        """
        st.sidebar.title(self.app_name)
        page = st.sidebar.radio(
            "Navigation",
            self.pages,
            format_func=lambda page: page['title']
        )
        page['function']()
