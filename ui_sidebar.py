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
atr_period = st.sidebar.number_input(
    label="ATR-Periode (Tage)",
    value=14,
    min_value=1,
    help="Anzahl Tage zur Berechnung der ATR (Average True Range)."
)
vj_divider = st.sidebar.radio(
    label="Teiler Vorjahr",
    options=[8, 16],
    index=1,
    help="Teiler für das Vorjahr (8 oder 16)."
)
vm_divider = st.sidebar.radio(
    label="Teiler Vormonat",
    options=[8, 16],
    index=1,
    help="Teiler für den Vormonat (8 oder 16)."
)
big_rhythm_options = ["0,36", "3,6", "36", "360", "3600"]
big_rhythm = st.sidebar.selectbox(
    "Großer Rhythmus",
    options=big_rhythm_options,
    index=3,
    help="Auswahl des großen Teilers: 0,36 / 3,6 / 36 / 360 / 3600"
)

