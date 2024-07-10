import streamlit as st
import os
import importlib.util
from streamlit_navigation_bar import st_navbar

# Seite konfigurieren (nur einmal in der Hauptdatei)
st.set_page_config(
    page_title="Portfolio Performance", 
    page_icon=":chart_with_upwards_trend:", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

pages = ["Your Portfolio", "KPIs", "Stock Searcher", "Yahoo Finance"]
parent_dir = os.path.dirname(os.path.abspath(__file__))
urls = {"Yahoo Finance": "https://finance.yahoo.com/"}  # Hier können Sie URLs hinzufügen, wenn nötig
styles = {
    "nav": {
        "background-color": "cornflowerblue",
        "justify-content": "center",
    },
    "img": {
        "padding-right": "14px",
    },
    "span": {
        "color": "whitesmoke",
        "padding": "30px",
        "font-family": "monospace",  # Font-Family anpassen
        "font-size": "17px",  # Schriftgröße anpassen
    },
    "active": {
        "background-color": "whitesmoke",
        "color": "cornflowerblue",
        "font-weight": "normal",
        "padding": "25px",
        "font-family": "monospace",  # Font-Family anpassen
        "font-size": "19px",  # Schriftgröße anpassen
    }

}
options = {
    "show_menu": False,
    "show_sidebar": False,
}

page = st_navbar(
    pages,
    urls=urls,
    styles=styles,
    options=options,
)

# Dynamisches Laden der Seitenmodule
def load_page_module(page_name):
    module_name = f"pages.{page_name}"
    module_path = os.path.join(parent_dir, f"{page_name}.py")
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

# Dictionary mit den Seiten und deren Funktionen
functions = {
    "Your Portfolio": "1_your_portfolio",
    "KPIs": "2_KPIs",
    "Stock Searcher": "3_stock_searcher",
}

selected_page = functions.get(page)
if selected_page:
    page_module = load_page_module(selected_page)
    page_module.app()
