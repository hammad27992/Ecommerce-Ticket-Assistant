import streamlit as st
import requests

st.title("E-commerce Ticket Assistant")

ticket = st.text_area("Enter Customer Ticket")

if st.button("Analyze Ticket"):

    if not ticket.strip():
        st.error("Please enter a ticket.")

    else:
        try:
            response = requests.post(
                "http://127.0.0.1:8000/analyze",
                json={
                    "ticket": ticket,
                    "prompt_version": "v2"
                },
                timeout=10
            )

            if response.status_code == 200:
                result = response.json()

                st.success("Ticket Analyzed Successfully")
                st.write("Category:", result["category"])
                st.write("Summary:", result["summary"])

            else:
                st.error(response.text)

        except requests.exceptions.RequestException:
            st.error("Backend is unavailable. Please start the API.")