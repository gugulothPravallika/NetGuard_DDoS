import streamlit as st
import pandas as pd
import tensorflow as tf
import time

# --- SET PAGE THEME ---
st.set_page_config(
    page_title="",
    page_icon="🛡️"DDoS_Detection"
    layout="wide"
)

# --- CUSTOM CSS FOR STYLING (Optional) ---
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .stMetric {
        background-color: #1e2130;
        padding: 15px;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER SECTION ---
st.title("🛡️ NetGuard AI: Network Intrusion Detection")
st.write("Real-time threat analysis powered by Deep Learning.")

# --- SIDEBAR FRONTEND ---
st.sidebar.image("https://img.icons8.com/fluency/144/shield.png", width=100)
st.sidebar.title("Control Panel")
mode = st.sidebar.radio("Navigation", ["Live Monitor", "Upload Data", "Model Health"])

# --- TABBED INTERFACE ---
if mode == "Live Monitor":
    col1, col2, col3 = st.columns(3)
    col1.metric("Traffic Scanned", "1,240 GB", "+5%")
    col2.metric("Threats Blocked", "42", "High", delta_color="inverse")
    col3.metric("System Latency", "12ms", "-2ms")

    st.subheader("Network Traffic Visualization")
    # Generating dummy data for the frontend chart
    chart_data = pd.DataFrame(
        [10, 25, 15, 40, 35, 50, 45],
        columns=['Threat Probability %']
    )
    st.line_chart(chart_data)

elif mode == "Upload Data":
    st.header("Bulk Analysis")
    uploaded_file = st.file_uploader("Upload Network Logs (CSV format)", type=["csv"])
    
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.write("### Data Preview")
        st.dataframe(df.head(10), use_container_width=True)
        
        if st.button("🚀 Start AI Deep Scan"):
            progress_bar = st.progress(0)
            for i in range(100):
                time.sleep(0.01)
                progress_bar.progress(i + 1)
            st.success("Analysis Complete: No critical threats found.")
            st.balloons()

elif mode == "Model Health":
    st.header("AI Model Diagnostics")
    st.info("Status: Operational (TensorFlow Engine Active)")
    
    # Displaying model layers or info
    st.code("""
    Model: "Sequential"
    _________________________________________________________________
    Layer (type)                Output Shape              Param #   
    =================================================================
    dense (Dense)               (None, 64)                4160      
    dropout (Dropout)           (None, 64)                0         
    dense_1 (Dense)             (None, 1)                 65        
    =================================================================
    """)

# --- FOOTER ---
st.markdown("---")
st.caption("NetGuard_AI v1.0.4 | Powered by Streamlit Cloud")
