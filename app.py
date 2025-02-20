import streamlit as st
import uuid
from ui_sidebar import get_sidebar_inputs

def main():
    run_id = uuid.uuid4()
    st.title("Mini-App für Button-Test")

    inputs = get_sidebar_inputs()
    st.write("DEBUG: start_button =", inputs["start_button"], "Run-ID:", run_id)

    if not inputs["start_button"]:
        st.info("Bitte auf 'Berechnen' klicken.")
        st.stop()

    st.success(f"Button erkannt, Run-ID: {run_id}")

if __name__ == "__main__":
    main()
