import streamlit as st
from datetime import date

def get_sidebar_inputs():
    if "start_button_pressed" not in st.session_state:
        st.session_state["start_button_pressed"] = False

    if st.sidebar.button("Berechnen"):
        st.session_state["start_button_pressed"] = True

    return {"start_button": st.session_state["start_button_pressed"]}
ticker = st.sidebar.text_input("Wertpapier (Ticker)", "BTC-USD")
analysis_date = st.sidebar.date_input("Gesuchtes Datum", value=date.today())

analysis_date = st.sidebar.date_input(
    label="Gesuchtes Datum",
    value=date.today(),
    help="Datum für die Analyse (z.B. aktueller Tag oder Vergangenheitsdatum)."
)
mode_choice = st.sidebar.radio(
    label="Suchmodus",
    options=["hoch", "tief"],
    index=0,
    help="Art der gesuchten Preisprojektion."
)

