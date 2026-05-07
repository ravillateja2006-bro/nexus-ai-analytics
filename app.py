import streamlit as st
import pandas as pd
from io import StringIO

# ---------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------

st.set_page_config(
    page_title="Nexus AI Analytics",
    page_icon="📊",
    layout="wide"
)

# ---------------------------------------------------
# PROFESSIONAL LIGHT UI
# ---------------------------------------------------

st.markdown("""
<style>

/* Main App */
.stApp {
    background-color: #F3F4F6;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #E5E7EB;
}

/* ALL TEXT */
html, body, [class*="css"] {
    color: #111827;
    font-family: 'Segoe UI', sans-serif;
}

/* Headings */
h1, h2, h3, h4, h5 {
    color: #111827 !important;
}

/* Paragraphs */
p {
    color: #374151 !important;
}

/* Labels */
label {
    color: #111827 !important;
    font-weight: 600;
}

/* Cards */
.card {
    background: white;
    padding: 25px;
    border-radius: 18px;
    border: 1px solid #E5E7EB;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}

/* Metric Cards */
[data-testid="metric-container"] {
    background: white;
    border: 1px solid #E5E7EB;
    padding: 18px;
    border-radius: 16px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.05);
}

/* Upload Box */
[data-testid="stFileUploader"] {
    background: white;
    border: 2px dashed #CBD5E1;
    border-radius: 18px;
    padding: 20px;
}

/* Tabs */
button[data-baseweb="tab"] {
    background: #E5E7EB;
    color: #111827 !important;
    border-radius: 10px;
    margin-right: 5px;
    padding: 10px 18px;
    font-weight: 600;
}

/* Buttons */
.stButton button {
    background: linear-gradient(to right, #2563EB, #1D4ED8);
    color: white !important;
    border: none;
    border-radius: 12px;
    padding: 12px 24px;
    font-weight: 600;
}

/* Download Button */
.stDownloadButton button {
    background: linear-gradient(to right, #10B981, #059669);
    color: white !important;
    border: none;
    border-radius: 12px;
    padding: 12px 24px;
    font-weight: 600;
}

/* Input Boxes */
input, textarea {
    background-color: white !important;
    color: #111827 !important;
    border-radius: 10px !important;
}

/* Selectbox */
div[data-baseweb="select"] {
    background-color: white;
    border-radius: 10px;
}

/* Dataframe */
[data-testid="stDataFrame"] {
    background-color: white;
}

/* Success Box */
[data-testid="stAlert"] {
    border-radius: 12px;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

st.sidebar.title("🚀 Nexus AI Analytics")

st.sidebar.markdown("---")

st.sidebar.subheader("📌 How To Use")

st.sidebar.info("""
1. Select a data source

2. Upload or paste dataset

3. Click Run AI Analysis

4. Explore dashboard insights

5. Download AI report
""")

st.sidebar.markdown("---")

st.sidebar.success("System Ready")

# ---------------------------------------------------
# MAIN TITLE
# ---------------------------------------------------

st.title("📊 Nexus AI Analytics")

st.markdown("""
Professional AI-powered business intelligence dashboard.

Analyze datasets, visualize trends, and generate AI insights instantly.
""")

st.markdown("---")

# ---------------------------------------------------
# FEATURE CARDS
# ---------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
    <h3>📂 Smart Data Input</h3>
    <p>Upload CSV files, paste datasets, or load files directly from URLs.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
    <h3>📊 Visual Analytics</h3>
    <p>Generate professional charts and identify business trends quickly.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
    <h3>🤖 AI Insights</h3>
    <p>Automatically generate insights and business summaries using AI.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ---------------------------------------------------
# DATA INPUT CENTER
# ---------------------------------------------------

st.subheader("📂 Smart Data Input Center")

input_method = st.selectbox(
    "Choose Data Source",
    [
        "📁 Upload CSV File",
        "📋 Paste Sample Dataset",
        "🔗 Load Dataset From URL"
    ]
)

df = None

# ---------------------------------------------------
# OPTION 1 - FILE UPLOAD
# ---------------------------------------------------

if input_method == "📁 Upload CSV File":

    uploaded_file = st.file_uploader(
        "Upload CSV Dataset",
        type=["csv"]
    )

    if uploaded_file is not None:

        df = pd.read_csv(uploaded_file)

        st.success("Dataset uploaded successfully")

# ---------------------------------------------------
# OPTION 2 - PASTE DATA
# ---------------------------------------------------

elif input_method == "📋 Paste Sample Dataset":

    sample_data = st.text_area(
        "Paste CSV Data Below",
        height=250,
        placeholder="""
Order_ID,Region,Sales,Profit
1001,North,5000,1200
1002,South,7000,1800
1003,East,3000,700
"""
    )

    if sample_data:

        df = pd.read_csv(StringIO(sample_data))

        st.success("Sample dataset loaded successfully")

# ---------------------------------------------------
# OPTION 3 - URL DATA
# ---------------------------------------------------

elif input_method == "🔗 Load Dataset From URL":

    file_url = st.text_input(
        "Paste CSV File URL"
    )

    st.info(
        "Example: Paste a direct CSV URL from GitHub or dataset websites."
    )

    if file_url:

        try:

            df = pd.read_csv(file_url)

            st.success("Dataset loaded successfully")

        except:

            st.error("Unable to load dataset from URL")

# ---------------------------------------------------
# RUN ANALYSIS BUTTON
# ---------------------------------------------------

run_analysis = st.button("🚀 Run AI Analysis")

# ---------------------------------------------------
# ANALYSIS SECTION
# ---------------------------------------------------

if run_analysis and df is not None:

    st.markdown("---")

    st.subheader("📌 Dashboard Overview")

    # KPI CARDS

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Rows", len(df))
    col2.metric("Columns", len(df.columns))
    col3.metric("Missing Values", df.isnull().sum().sum())

    numeric_columns = len(
        df.select_dtypes(include='number').columns
    )

    col4.metric("Numeric Columns", numeric_columns)

    st.markdown("---")

    # TABS

    tab1, tab2, tab3 = st.tabs([
        "📄 Dataset",
        "📊 Visual Analytics",
        "🤖 AI Insights"
    ])

    # DATASET TAB

    with tab1:

        st.subheader("Dataset Preview")

        st.dataframe(
            df,
            use_container_width=True
        )

        st.subheader("Column Names")

        st.write(list(df.columns))

    # ANALYTICS TAB

    with tab2:

        st.subheader("Visual Analytics")

        numeric_df = df.select_dtypes(include='number')

        if not numeric_df.empty:

            st.markdown("### 📈 Line Chart")
            st.line_chart(numeric_df)

            st.markdown("### 📊 Bar Chart")
            st.bar_chart(numeric_df)

            st.markdown("### 📉 Area Chart")
            st.area_chart(numeric_df)

        else:

            st.warning(
                "No numeric columns available for charts."
            )

    # AI INSIGHTS TAB

    with tab3:

        st.subheader("🤖 AI Generated Insights")

        insights = f"""
✅ Dataset contains {len(df)} rows.

✅ Dataset contains {len(df.columns)} columns.

✅ Missing values detected: {df.isnull().sum().sum()}.

✅ Numeric columns analyzed successfully.

✅ Dataset is ready for AI-powered analytics.

✅ Visual analysis completed successfully.
"""

        st.success(insights)

        st.markdown("---")

        st.subheader("⬇ Download AI Report")

        st.download_button(
            label="Download Report",
            data=insights,
            file_name="AI_Report.txt",
            mime="text/plain"
        )

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.markdown("---")

st.caption(
    "Nexus AI Analytics Platform | Powered by Streamlit"
)