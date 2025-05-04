import streamlit as st


st.title("📚 Davao Oriental State University")
st.subheader("A university of excellence, innovation, and inclusion")
st.caption("🇵🇭 Republic of the Philippines")

st.markdown("---")


st.sidebar.header("🔍 Filters and Options")
selected_topic = st.sidebar.selectbox(
    "Choose a topic",
    ("Data Warehousing", "Enterprise Data Management")
)

show_details = st.sidebar.checkbox("Show detailed explanations")


st.header(f"Topic: {selected_topic}")


tab1, tab2 = st.tabs(["Overview", "Key Concepts"])

with tab1:
    st.subheader("Overview")

    if selected_topic == "Data Warehousing":
        st.write("""
        Data Warehousing involves collecting, storing, and managing large volumes of data from different sources 
        to support business intelligence activities such as reporting and analytics.
        """)
    else:
        st.write("""
        Enterprise Data Management (EDM) ensures that an organization's data assets are properly managed, 
        integrated, and accessible for accurate and efficient decision-making across the enterprise.
        """)

with tab2:
    st.subheader("Key Concepts")

    col1, col2 = st.columns(2)

    with col1:
        with st.expander("📂 ETL (Extract, Transform, Load)"):
            st.write("""
            ETL is a core process in Data Warehousing where data is extracted from source systems, transformed 
            into a suitable format, and loaded into the warehouse for analysis.
            """)

        with st.expander("🛠️ Data Integration"):
            st.write("""
            Data integration combines data from different sources to provide a unified view, 
            which is crucial for both Data Warehousing and Enterprise Data Management.
            """)

    with col2:
        with st.expander("🧩 Data Governance"):
            st.write("""
            Data Governance ensures data quality, consistency, and security by defining policies, procedures, and responsibilities.
            """)

        with st.expander("📈 Business Intelligence (BI)"):
            st.write("""
            BI involves using data warehousing and analytics tools to convert data into actionable insights for business decision-making.
            """)


if show_details:
    st.markdown("---")
    st.subheader("📖 Detailed Explanations")
    if selected_topic == "Data Warehousing":
        st.write("""
        A Data Warehouse integrates historical data from various sources, optimized for querying and reporting 
        rather than transaction processing. Common architectures include star schema and snowflake schema.
        """)
    else:
        st.write("""
        Enterprise Data Management includes Master Data Management (MDM), Metadata Management, and Data Quality Management 
        — ensuring that data assets are accurate, consistent, and governed throughout the organization.
        """)

