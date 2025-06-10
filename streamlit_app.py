import pickle
import os
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu

# Load model
stroke_model = pickle.load(open("stroke.sav", 'rb'))

# Mapping dictionaries
gender_map = {"Male": 1, "Female": 0, "Other": 2}
hypertension_map = {"Yes": 1, "No": 0}
heart_disease_map = {"Yes": 1, "No": 0}
married_map = {"Yes": 1, "No": 0}
work_type_map = {
    "Private": 0, "Self-employed": 1, "Govt_job": 2, "Children": 3, "Never_worked": 4
}
residence_map = {"Urban": 1, "Rural": 0}
smoking_map = {
    "formerly smoked": 0, "never smoked": 1, "smokes": 2, "Unknown": 3
}

# Initialize session state
if "user_input" not in st.session_state:
    st.session_state.user_input = {}
if "stroke_risk" not in st.session_state:
    st.session_state.stroke_risk = None

# Sidebar navigation
with st.sidebar:
    selected = option_menu(
        "Stroke Risk App",
        ["🏠 Welcome", "📝 Enter Details", "🔍 Predict Stroke", "💡 Recommendations", "❓ FAQs"],
        icons=["house", "pencil", "search", "lightbulb", "question-circle"],
        menu_icon="heart-pulse",
        default_index=0
    )

# Welcome Page
if selected == "🏠 Welcome":
    st.title("🏥 Welcome to Stroke Risk Prediction App")
    st.markdown("""
    This app helps you estimate your risk of stroke based on health-related information.
    
    *Features:*
    - Fill in your details
    - Get predictions instantly
    - Receive personalized health advice
    """)

# Enter Details Page
elif selected == "📝 Enter Details":
    st.title("📝 Enter Your Health & Personal Details")
    with st.form("user_form"):
        col1, col2, col3 = st.columns(3)

        with col1:
            gender = st.selectbox("Gender", list(gender_map.keys()))
        with col2:
            age = st.number_input("Age", min_value=0, max_value=120, value=30)
        with col3:
            hypertension = st.selectbox("Hypertension", list(hypertension_map.keys()))

        with col1:
            heart_disease = st.selectbox("Heart Disease", list(heart_disease_map.keys()))
        with col2:
            married = st.selectbox("Ever Married", list(married_map.keys()))
        with col3:
            work_type = st.selectbox("Work Type", list(work_type_map.keys()))

        with col1:
            residence = st.selectbox("Residence Type", list(residence_map.keys()))
        with col2:
            glucose = st.number_input("Average Glucose Level", min_value=10.0, value=90.0)
        with col3:
            bmi = st.number_input("Body Mass Index", min_value=3.0, value=22.0)

        with col1:
            smoking = st.selectbox("Smoking Status", list(smoking_map.keys()))

        submitted = st.form_submit_button("Save Details")
        if submitted:
            st.session_state.user_input = {
                "Gender": gender,
                "Age": age,
                "Hypertension": hypertension,
                "Heart Disease": heart_disease,
                "Married": married,
                "Work Type": work_type,
                "Residence": residence,
                "Glucose": glucose,
                "BMI": bmi,
                "Smoking": smoking
            }
            st.success("✅ Details saved! Go to 'Predict Stroke' to continue.")

# Prediction Page
elif selected == "🔍 Predict Stroke":
    st.title("🔍 Stroke Risk Prediction")

    if not st.session_state.user_input:
        st.warning("⚠ Please fill in your details on the 'Enter Details' page.")
    else:
        # Encode input
        ui = st.session_state.user_input
        input_data = [
            gender_map[ui["Gender"]],
            ui["Age"],
            hypertension_map[ui["Hypertension"]],
            heart_disease_map[ui["Heart Disease"]],
            married_map[ui["Married"]],
            work_type_map[ui["Work Type"]],
            residence_map[ui["Residence"]],
            ui["Glucose"],
            ui["BMI"],
            smoking_map[ui["Smoking"]]
        ]
        prediction = stroke_model.predict([input_data])
        st.session_state.stroke_risk = prediction[0]

        if prediction[0] == 1:
            st.error("⚠ Stroke Risk Detected")
        else:
            st.success("✅ No Stroke Risk Detected")

# Recommendations Page
elif selected == "💡 Recommendations":
    st.title("💡 Health Recommendations")

    if st.session_state.stroke_risk is None:
        st.info("Please run a prediction first.")
    else:
        if st.session_state.stroke_risk == 1:
            st.warning("🧠 At Risk: Consider these actions:")
            st.markdown("""
            - 🏃 Engage in daily physical activity  
            - 🥗 Follow a balanced, low-salt diet  
            - 🚭 Quit smoking and limit alcohol  
            - 💊 Take meds for blood pressure & diabetes  
            - 🩺 Regular health checkups  
            """)
        else:
            st.success("🎉 You are at low risk!")
            st.markdown("""
            - 👍 Maintain current healthy habits  
            - 🧘‍♀ Manage stress  
            - 🧂 Avoid high-sodium foods  
            - 💧 Stay hydrated  
            - 🩺 Get periodic health assessments  
            """)

# FAQs Page
elif selected == "❓ FAQs":
    st.title("❓ Frequently Asked Questions")
    with st.expander("What is a stroke?"):
        st.write("A stroke is when blood flow to the brain is blocked, causing brain damage.")
    with st.expander("What are the symptoms of stroke?"):
        st.write("Symptoms include sudden numbness, confusion, trouble seeing, walking, or speaking.")
    with st.expander("Is this a medical diagnosis?"):
        st.write("No, this is a prediction tool. Always consult a doctor for medical advice.")
    with st.expander("Can lifestyle changes reduce my risk?"):
        st.write("Yes! Exercise, healthy eating, and avoiding tobacco and alcohol reduce stroke risk.")
