# ❤️ Heart Disease Risk Predictor

A beautiful, AI-powered web application for predicting heart disease risk using machine learning. Built with Streamlit and featuring a modern, responsive UI.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 📋 Overview

This application uses a K-Nearest Neighbors (KNN) machine learning model to predict the risk of heart disease based on various clinical parameters. The app features a stunning gradient UI with organized input sections and provides detailed risk analysis with confidence levels.

## ✨ Features

- **Modern UI Design**: Beautiful gradient background with a clean white card layout
- **Organized Input Sections**: 
  - 👤 Personal Information (Age, Sex)
  - 📊 Vital Signs (Blood Pressure, Cholesterol, Heart Rate)
  - 🔬 Clinical Tests (ECG, Chest Pain, Blood Sugar)
- **Smart Predictions**: ML-powered risk assessment with confidence probabilities
- **Visual Feedback**: Color-coded results (Red for high risk, Green for low risk)
- **Responsive Layout**: Wide layout optimized for desktop viewing
- **Interactive Elements**: Tooltips and help text for medical terms
- **Professional Results**: Confidence metrics with progress bars

## 🛠️ Technologies Used

- **Python 3.8+**
- **Streamlit**: Web framework
- **Pandas**: Data manipulation
- **Scikit-learn**: Machine learning
- **Joblib**: Model serialization

## 📦 Installation

1. **Clone the repository** (or download the files)
```bash
cd "Heart Disease predict"
```

2. **Install required packages**
```bash
pip install -r requirements.txt
```

## 🚀 Usage

Run the Streamlit app:
```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

## 📊 Input Parameters

### Personal Information
- **Age**: 18-100 years
- **Sex**: Male (M) / Female (F)

### Vital Signs
- **Resting Blood Pressure**: 80-200 mm Hg
- **Cholesterol**: 100-600 mg/dL
- **Max Heart Rate**: 60-220 bpm

### Clinical Tests
- **Chest Pain Type**: ATA, NAP, TA, ASY
- **Resting ECG**: Normal, ST, LVH
- **Fasting Blood Sugar**: > 120 mg/dL (Yes/No)
- **Exercise-Induced Angina**: Yes/No
- **Oldpeak**: ST depression (0.0-6.0)
- **ST Slope**: Up, Flat, Down

## 📁 Project Structure

```
Heart Disease predict/
│
├── app.py                      # Main Streamlit application
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
├── HeartdiseaseFinal.ipynb    # Model training notebook
│
├── knn_heart_model.pkl        # Trained KNN model
├── heart_scaler.pkl           # Feature scaler
└── heart_columns.pkl          # Expected column names
```

## 🎯 How It Works

1. **Input Collection**: User provides clinical and personal health data
2. **Data Preprocessing**: Input is formatted and scaled using the pre-trained scaler
3. **Prediction**: KNN model analyzes the data
4. **Results Display**: Shows risk level with confidence probabilities

## ⚠️ Medical Disclaimer

This tool is for **educational purposes only** and should **not replace professional medical advice**. Always consult with qualified healthcare providers for medical diagnosis and treatment.

## 👨‍💻 Author

**Akarsh**

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 📝 License

This project is open source and available for educational purposes.

## 🔮 Future Enhancements

- [ ] Add data visualization charts
- [ ] Export prediction reports as PDF
- [ ] Multi-language support
- [ ] Historical prediction tracking
- [ ] Integration with more ML models
- [ ] Mobile-responsive design improvements

## 📞 Support

For support or questions, please open an issue in the repository.

---

Made with ❤️ by Harsh
