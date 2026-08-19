import streamlit as st
import pandas as pd

from generators.report_generator import (
    build_full_report
)

from generators.reviewer import (
    review_report
)

from exporters.word_exporter import (
    export_word
)

from exporters.pdf_exporter import (
    export_pdf
)

st.set_page_config(
    page_title="AI Sustainability Report Generator",
    page_icon="🌱",
    layout="wide"
)

st.title(
    "🌱 AI Tool for Automated Sustainability Report Generation"
)

st.markdown(
    """
Upload KPI data and generate a sustainability report
based on historical company reporting style.
"""
)

uploaded_file = st.file_uploader(
    "Upload Sustainability KPI Excel/CSV",
    type=["xlsx", "csv"]
)

if uploaded_file:

    if uploaded_file.name.endswith(".xlsx"):

        df = pd.read_excel(
            uploaded_file
        )

    else:

        df = pd.read_csv(
            uploaded_file
        )

    st.subheader(
        "Uploaded KPI Dataset"
    )

    st.dataframe(
        df,
        use_container_width=True
    )

    if st.button(
        "Generate Sustainability Report"
    ):

        kpi_text = ""

        for _, row in df.iterrows():

            kpi_text += (
                f"{row['KPI']} : "
                f"{row['Value']}\n"
            )

        with st.spinner(
            "Generating report sections..."
        ):

            generated_report = (
                build_full_report(
                    kpi_text
                )
            )

        with st.spinner(
            "Reviewing report for consistency..."
        ):

            reviewed_report = (
                review_report(
                    generated_report
                )
            )

        st.success(
            "Report Generated Successfully"
        )

        st.subheader(
            "Preview"
        )

        st.markdown(
            reviewed_report
        )

        word_file = export_word(
            reviewed_report
        )

        pdf_file = export_pdf(
            reviewed_report
        )

        with open(
            word_file,
            "rb"
        ) as file:

            st.download_button(
                label="⬇️ Download Word Report",
                data=file.read(),
                file_name=word_file,
                mime=(
                    "application/vnd.openxmlformats-"
                    "officedocument.wordprocessingml.document"
                )
            )

        with open(
            pdf_file,
            "rb"
        ) as file:

            st.download_button(
                label="⬇️ Download PDF Report",
                data=file.read(),
                file_name=pdf_file,
                mime="application/pdf"
            )