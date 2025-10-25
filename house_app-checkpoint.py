import streamlit as st
import joblib
import numpy as np
import base64
from streamlit_option_menu import option_menu


def add_bg_from_local(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()
    css = f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;800&display=swap');

    [data-testid="stAppViewContainer"] {{
        background-image: url("data:image/png;base64,{encoded}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        font-family: 'Poppins', sans-serif !important;
        color: #f8f9fa;  
    }}

    [data-testid="stHeader"], [data-testid="stToolbar"] {{
        background: rgba(0,0,0,0);
    }}

    h1, h2, h3, p, label {{
        font-family: 'Poppins', sans-serif !important;
        text-shadow: 2px 2px 6px rgba(0,0,0,0.7);  
    }}

    .stNumberInput label {{
        font-weight: 600; 
        font-size: 15px;
        color: #ffffff !important;
        background: rgba(0,0,0,0.4);  
        padding: 4px 8px;
        border-radius: 6px;
    }}

    .stButton>button {{
        background-color: #1F618D;
        color: white;
        font-weight: 600;
        border-radius: 10px;
        padding: 10px 24px;
        transition: 0.3s;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.6);
        font-family: 'Poppins', sans-serif !important;
    }}

    .stButton>button:hover {{
        background-color: #154360;
        transform: scale(1.05);
    }}

    /* Footer style */
    .footer {{
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: rgba(0,0,0,0.6);
        color: #f1f1f1;
        text-align: center;
        padding: 8px;
        font-size: 14px;
        font-family: 'Poppins', sans-serif;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)


add_bg_from_local("bck.jpeg")

# ================== Navigation Menu ==================
selected = option_menu(
    menu_title=None,
    options=["Home", "About", "Login", "Sign Up"],
    icons=["house", "info-circle", "box-arrow-in-right", "person-plus"],
    menu_icon="list",  
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "rgba(0,0,0,0.5)"},
        "icon": {"color": "white", "font-size": "18px"}, 
        "nav-link": {
            "font-size": "16px",
            "text-align": "center",
            "margin":"0px",
            "color":"#ECF0F1",
            "font-weight":"500",
        },
        "nav-link-selected": {"background-color": "#1F618D"},
    }
)

# ================== Page Content ==================
if selected == "Home":
    st.markdown(
        """
        <h1 style='text-align: center; color: #F4D03F; font-size: 46px; font-weight: 800;'>
        🏠 DreamHome Value Estimator
        </h1>
        <p style='text-align: center; color: #ECF0F1; font-size:18px; font-weight:500;'>
        Enter your property details below and get an instant <b>AI-powered market valuation</b> 💰
        </p>
        """,
        unsafe_allow_html=True
    )

    # Load Model
    try:
        model = joblib.load("house_price_model_simple.pkl")
    except Exception as e:
        st.error(f"⚠ Error loading model: {e}")
        st.stop()

    st.subheader("🏡 Property Information")

    col1, col2 = st.columns(2)

    with col1:
        overallqual = st.number_input("Overall Quality (1-10)", min_value=1, max_value=10, value=5)
        garagecars = st.number_input("Garage Capacity (Cars)", min_value=0, max_value=5, value=2)

    with col2:
        grlivarea = st.number_input("Above Ground Living Area (sq ft)", min_value=500, max_value=5000, value=1500)
        totalbsmt = st.number_input("Total Basement Area (sq ft)", min_value=0, max_value=3000, value=800)

    fullbath = st.number_input("Number of Full Bathrooms", min_value=0, max_value=5, value=2)

    # Prediction Button
    if st.button("🔮 Predict House Price"):
        input_data = np.array([[overallqual, grlivarea, garagecars, totalbsmt, fullbath]])
        prediction = model.predict(input_data)[0]

        st.markdown(
            f"""
            <div style="text-align:center; background: rgba(0,0,0,0.6); padding:20px; 
            border-radius:15px; margin-top:20px;">
                <h2 style="color:#58D68D; font-weight:700;">💰 Estimated House Price</h2>
                <h1 style="color:#F4D03F; font-weight:800;">${prediction:,.0f}</h1>
                <p style="color:#ECF0F1; font-size:14px;">⚠ This is an AI-estimated value and may differ from real market price.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.balloons()

elif selected == "About":
    st.title("ℹ About")
    st.write(
        """
        This app is designed to estimate house prices using a Machine Learning model.  
        Enter property details such as quality, living area, and number of bathrooms,  
        and get an instant AI-powered price estimation.  
        """
    )

elif selected == "Login":
    st.title("🔑 Login")
    st.text_input("Username")
    st.text_input("Password", type="password")
    st.button("Login")

elif selected == "Sign Up":
    st.title("📝 Sign Up")
    st.text_input("Full Name")
    st.text_input("Email")
    st.text_input("Password", type="password")
    st.button("Create Account")


# ================== Footer ==================
st.markdown(
    """
    <div style="
        position: fixed;
        left: 10px;
        bottom: 10px;
        color: #f1f1f1;
        font-size: 14px;
        font-family: 'Poppins', sans-serif;
    ">
        Developed by <b style="color:#F4D03F;">KARTICK DEY</b>
    </div>
    """,
    unsafe_allow_html=True
)