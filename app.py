import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime

from src.prediction import WineQualityPredictor

# ---------------------------
# Page Configuration
# ---------------------------
st.set_page_config(
    page_title="Wine Quality Prediction",
    page_icon="🍷",
    layout="wide"
)

predictor = WineQualityPredictor()

# ---------------------------
# Custom CSS
# ---------------------------
st.markdown("""
<style>

.main{
    background-color:#0E1117;
}

.big-title{
    font-size:45px;
    font-weight:bold;
    color:white;
}

.subtitle{
    font-size:18px;
    color:#BBBBBB;
}

.card{
    background-color:#1E1E1E;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 0px 12px rgba(0,0,0,0.4);
}

.result{
    background:#1B4332;
    padding:25px;
    border-radius:15px;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------
# Sidebar
# ---------------------------

st.sidebar.title("🍷 Wine Quality Predictor")

st.sidebar.markdown("---")

st.sidebar.subheader("Project")

st.sidebar.write("""
This project predicts the quality of wine using Machine Learning based on its chemical properties.
""")

st.sidebar.markdown("### Model")

st.sidebar.success("Support Vector Classifier (SVC)")

st.sidebar.markdown("### Dataset")

st.sidebar.info("Wine Quality Dataset (Kaggle)")

st.sidebar.markdown("### Developer")

st.sidebar.write("**Diya Sarkar**")

st.sidebar.markdown("---")

st.sidebar.caption("Machine Learning Portfolio Project")

# ---------------------------
# Title
# ---------------------------

st.markdown(
    "<div class='big-title'>🍷 Wine Quality Prediction System</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Predict Wine Quality using Chemical Properties and Machine Learning.</div>",
    unsafe_allow_html=True
)

st.write("")

# ---------------------------
# Inputs
# ---------------------------

col1, col2 = st.columns(2)

with col1:

    fixed_acidity = st.number_input("Fixed Acidity", value=7.4)

    volatile_acidity = st.number_input("Volatile Acidity", value=0.70)

    citric_acid = st.number_input("Citric Acid", value=0.00)

    residual_sugar = st.number_input("Residual Sugar", value=1.90)

    chlorides = st.number_input("Chlorides", value=0.076)

    free_sulfur_dioxide = st.number_input(
        "Free Sulfur Dioxide",
        value=11.0
    )

with col2:

    total_sulfur_dioxide = st.number_input(
        "Total Sulfur Dioxide",
        value=34.0
    )

    density = st.number_input("Density", value=0.9978)

    pH = st.number_input("pH", value=3.51)

    sulphates = st.number_input("Sulphates", value=0.56)

    alcohol = st.number_input("Alcohol", value=9.4)

# ---------------------------
# Predict Button
# ---------------------------

if st.button("🔮 Predict Wine Quality", use_container_width=True):

    sample = [

        fixed_acidity,

        volatile_acidity,

        citric_acid,

        residual_sugar,

        chlorides,

        free_sulfur_dioxide,

        total_sulfur_dioxide,

        density,

        pH,

        sulphates,

        alcohol

    ]

    prediction, confidence = predictor.predict(sample)

    st.write("")

    st.success("Prediction Completed Successfully!")

    # ----------------------------------------
    # Quality Rating
    # ----------------------------------------

    if prediction <= 4:

        rating = "Poor Wine 🍷"

        color = "red"

    elif prediction <= 6:

        rating = "Average Wine 🍷"

        color = "orange"

    else:

        rating = "Excellent Wine 🍷"

        color = "green"

    # ----------------------------------------
    # Metrics
    # ----------------------------------------

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Predicted Quality",
        prediction
    )

    c2.metric(
        "Confidence",
        f"{confidence:.2f}%"
    )

    c3.metric(
        "Rating",
        rating
    )

    st.write("")

    # ----------------------------------------
    # Gauge Chart
    # ----------------------------------------

    gauge = go.Figure(

        go.Indicator(

            mode="gauge+number",

            value=confidence,

            title={"text":"Prediction Confidence"},

            gauge={

                "axis":{"range":[0,100]},

                "bar":{"color":"green"}

            }

        )

    )

    st.plotly_chart(
        gauge,
        use_container_width=True
    )

    # ----------------------------------------
    # Input Summary
    # ----------------------------------------

    st.subheader("📋 Input Summary")

    df = pd.DataFrame({

        "Feature":[

            "Fixed Acidity",

            "Volatile Acidity",

            "Citric Acid",

            "Residual Sugar",

            "Chlorides",

            "Free Sulfur Dioxide",

            "Total Sulfur Dioxide",

            "Density",

            "pH",

            "Sulphates",

            "Alcohol"

        ],

        "Value":sample

    })

    st.dataframe(
        df,
        use_container_width=True
    )

    # ----------------------------------------
    # Bar Chart
    # ----------------------------------------

    st.subheader("📊 Chemical Properties")

    fig = px.bar(

        df,

        x="Feature",

        y="Value",

        color="Value",

        text="Value"

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    # ----------------------------------------
    # Download Report
    # ----------------------------------------

    report = pd.DataFrame({

        "Prediction":[prediction],

        "Confidence":[confidence],

        "Rating":[rating],

        "Generated On":[datetime.now()]

    })

    csv = report.to_csv(index=False)

    st.download_button(

        label="📥 Download Prediction Report",

        data=csv,

        file_name="wine_prediction_report.csv",

        mime="text/csv"

    )

st.markdown("---")

st.caption(
    "Built with ❤️ using Python, Streamlit, Scikit-learn and Plotly | © 2026 Diya Sarkar"
)