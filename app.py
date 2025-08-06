import streamlit as st
import os
from converter import convert_pdf_to_word # Import the core function

# --- Streamlit User Interface ---

st.set_page_config(page_title="PDF to Word Converter", layout="centered")

st.title("📄 PDF to Word Converter")
st.markdown("Upload your PDF file, and we'll convert it to an editable Word document. The app handles both regular and scanned PDFs using OCR.")

# Instructions in a sidebar
with st.sidebar:
    st.header("Instructions")
    st.info(
        """
        1.  **Upload a PDF file** using the file uploader.
        2.  Click the **"Convert to Word"** button.
        3.  Wait for the conversion to complete.
        4.  Click **"Download Word Document"** to save your file.
        """
    )
    st.warning(
        """
        **Note:** For OCR to work, you must have Google's Tesseract-OCR engine installed on the system running this app.
        """
    )
    st.info("This app is composed of two files: `app.py` (the UI) and `converter_logic.py` (the core engine).")


# File uploader
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    # Display the name of the uploaded file
    st.success(f"File Uploaded: **{uploaded_file.name}**")

    # Convert button
    if st.button("Convert to Word", type="primary"):
        with st.spinner("Converting... This may take a moment, especially for scanned PDFs..."):
            # Create a placeholder for status updates
            status_placeholder = st.empty()
            
            # Call the conversion function from the other file
            result_docx_stream = convert_pdf_to_word(uploaded_file, status_placeholder)

            # Clear the status message once done
            status_placeholder.empty()

            if result_docx_stream:
                st.success("🎉 Conversion Successful!")

                # Get the original filename without extension
                base_filename = os.path.splitext(uploaded_file.name)[0]
                docx_filename = f"{base_filename}.docx"

                # Provide the download button
                st.download_button(
                    label="⬇️ Download Word Document",
                    data=result_docx_stream,
                    file_name=docx_filename,
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                )
