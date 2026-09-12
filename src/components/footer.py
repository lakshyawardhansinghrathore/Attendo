import streamlit as st


def footer(color="white"):
    st.markdown(
        f"""
        <div style="
            margin-top: 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            width: 100%;
        ">
            <p style="font-size: 0.9rem; font-weight: 500; opacity: 0.8; color: {color} !important; margin: 0;">
                © 2026 Attendo AI.
            </p>
            <p style="font-size: 0.9rem; font-weight: 500; opacity: 0.8; color: {color} !important; margin: 0;">
                All rights reserved.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )


def footer_home():
    footer("white")


def footer_dashboard():
    footer("black")
