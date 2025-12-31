import streamlit as st
import pandas as pd
import joblib

# Page configuration
st.set_page_config(
    page_title="Heart Disease Predictor",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        background-color: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);
        margin: 2rem auto;
    }
    h1 {
        color: #764ba2;
        font-family: 'Arial Black', sans-serif;
        text-align: center;
        padding-bottom: 10px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    .subtitle {
        text-align: center;
        color: #555;
        font-size: 1.1em;
        margin-bottom: 2rem;
        font-style: italic;
    }
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-size: 20px;
        font-weight: bold;
        border-radius: 10px;
        padding: 15px;
        border: none;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);
    }
    .section-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 10px 20px;
        border-radius: 10px;
        margin: 20px 0 15px 0;
        font-weight: bold;
        font-size: 1.2em;
    }
    label, .stSlider label, .stSelectbox label, .stNumberInput label {
        color: #000000 !important;
        font-weight: 600 !important;
        font-size: 1em !important;
    }
    .stMarkdown p {
        color: #333 !important;
    }
    </style>
""", unsafe_allow_html=True)

# Load saved model, scaler, and expected columns
model = joblib.load("knn_heart_model.pkl")
scaler = joblib.load("heart_scaler.pkl")
expected_columns = joblib.load("heart_columns.pkl")

# Header Section
st.title(" Heart Disease Risk Predictor")
st.markdown('<p class="subtitle"> AI-powered heart disease risk assessment By Harsh</p>', unsafe_allow_html=True)
st.markdown("---")

# Personal Information Section
st.markdown('<div class="section-header">👤 Personal Information</div>', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    age = st.slider("🎂 Age", 18, 100, 40, help="Your current age in years")
with col2:
    sex = st.selectbox("⚧ Sex", ["M", "F"], help="Biological sex")

# Vital Signs Section
st.markdown('<div class="section-header">📊 Vital Signs</div>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    resting_bp = st.number_input("💓 Resting Blood Pressure", 80, 200, 120, help="mm Hg")
with col2:
    cholesterol = st.number_input("🩸 Cholesterol", 100, 600, 200, help="mg/dL")
with col3:
    max_hr = st.slider("❤️ Max Heart Rate", 60, 220, 150, help="bpm")

# Clinical Tests Section
st.markdown('<div class="section-header">🔬 Clinical Tests</div>', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    chest_pain = st.selectbox("🫀 Chest Pain Type", ["ATA", "NAP", "TA", "ASY"], 
                              help="ATA: Atypical Angina, NAP: Non-Anginal Pain, TA: Typical Angina, ASY: Asymptomatic")
    resting_ecg = st.selectbox("📈 Resting ECG", ["Normal", "ST", "LVH"],
                               help="LVH: Left Ventricular Hypertrophy, ST: ST-T Wave Abnormality")
    fasting_bs = st.selectbox("🍬 Fasting Blood Sugar > 120 mg/dL", [0, 1],
                             format_func=lambda x: "Yes" if x == 1 else "No")
with col2:
    exercise_angina = st.selectbox("🏃 Exercise-Induced Angina", ["Y", "N"],
                                   format_func=lambda x: "Yes" if x == "Y" else "No")
    oldpeak = st.slider("📉 Oldpeak (ST Depression)", 0.0, 6.0, 1.0, 0.1,
                       help="ST depression induced by exercise relative to rest")
    st_slope = st.selectbox("📐 ST Slope", ["Up", "Flat", "Down"],
                           help="The slope of the peak exercise ST segment")

st.markdown("---")

# Prediction Button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    predict_button = st.button("🔮 Analyze Heart Disease Risk")

if predict_button:

    # Create a raw input dictionary
    raw_input = {
        'Age': age,
        'RestingBP': resting_bp,
        'Cholesterol': cholesterol,
        'FastingBS': fasting_bs,
        'MaxHR': max_hr,
        'Oldpeak': oldpeak,
        'Sex_' + sex: 1,
        'ChestPainType_' + chest_pain: 1,
        'RestingECG_' + resting_ecg: 1,
        'ExerciseAngina_' + exercise_angina: 1,
        'ST_Slope_' + st_slope: 1
    }

    # Create input dataframe
    input_df = pd.DataFrame([raw_input])

    # Fill in missing columns with 0s
    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    # Reorder columns
    input_df = input_df[expected_columns]

    # Scale the input
    scaled_input = scaler.transform(input_df)

    # Make prediction
    prediction = model.predict(scaled_input)[0]
    prediction_proba = model.predict_proba(scaled_input)[0]

    # Show result with animation
    st.markdown("---")
    st.markdown("### 📋 Analysis Results")
    
    # Create columns for results
    result_col1, result_col2 = st.columns([1, 1])
    
    with result_col1:
        if prediction == 1:
            st.markdown("""
                <div style='background: linear-gradient(135deg, #ff6b6b 0%, #ee5a6f 100%); 
                            padding: 30px; 
                            border-radius: 15px; 
                            text-align: center;
                            box-shadow: 0 5px 20px rgba(238, 90, 111, 0.4);'>
                    <h2 style='color: white; margin: 0;'>⚠️ High Risk</h2>
                    <p style='color: white; font-size: 18px; margin-top: 10px;'>Heart Disease Detected</p>
                </div>
            """, unsafe_allow_html=True)
            st.warning("⚕️ Please consult with a healthcare professional immediately for proper diagnosis and treatment.")
        else:
            st.markdown("""
                <div style='background: linear-gradient(135deg, #51cf66 0%, #37b24d 100%); 
                            padding: 30px; 
                            border-radius: 15px; 
                            text-align: center;
                            box-shadow: 0 5px 20px rgba(55, 178, 77, 0.4);'>
                    <h2 style='color: white; margin: 0;'>✅ Low Risk</h2>
                    <p style='color: white; font-size: 18px; margin-top: 10px;'>Heart Healthy</p>
                </div>
            """, unsafe_allow_html=True)
            st.info("💚 Continue maintaining a healthy lifestyle and regular check-ups.")
    
    with result_col2:
        st.markdown("#### Confidence Levels")
        st.metric("Low Risk Probability", f"{prediction_proba[0]*100:.1f}%")
        st.metric("High Risk Probability", f"{prediction_proba[1]*100:.1f}%")
        
        # Progress bars
        st.progress(float(prediction_proba[0]))
        st.progress(float(prediction_proba[1]))
    
    # Disclaimer
    st.markdown("---")
    st.markdown("""
        <div style='background-color: #f8f9fa; padding: 15px; border-radius: 10px; border-left: 4px solid #667eea;'>
            <strong>⚠️ Medical Disclaimer:</strong> This tool is for educational purposes only and should not replace 
            professional medical advice. Always consult with qualified healthcare providers for medical diagnosis and treatment.
        </div>
    """, unsafe_allow_html=True)