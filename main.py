import helpers
import streamlit as st
import base64

st.set_page_config(layout="wide")

# Create two equal width columns
col1, col2 = st.columns(2)
with col1:
    st.title("Classmate Finder")
    st.subheader("""Directions:
             1. Navigate to the "People" page in one of your classes.
             2. Copy the list and paste into Excel or Google Sheets.
             3. Save as a .csv file and upload the file below.
             4. Repeat until all your classes are uploaded.""")
with col2:
    # Load PDF file in binary mode
    instructions_pdf = "Classmate Finder.pdf"
    with open(instructions_pdf, "rb") as f:
        pdf_bytes = f.read()

    # Encode PDF to base64 text
    base64_pdf = base64.b64encode(pdf_bytes).decode("utf-8")

    # Embed PDF in an iframe using a data URI
    pdf_display = f"""
    <iframe src="data:application/pdf;base64,{base64_pdf}"
    width="100%" height="254" type="application/pdf"><iframe>
    """
    st.markdown(pdf_display, unsafe_allow_html=True)
    st.markdown(
        f'<a href="https://axel-t-b.github.io/find_shared_classes_unlv/Classmate%20Finder.pdf" target="_blank"> 🔎 Open in New Tab</a>', unsafe_allow_html=True
    )

st.markdown("---")

# Center the rest of page
left, center, right = st.columns([1, 3, 1])
with center:

    # Upload CSV files as a list of binary file-like objects
    csv_files = st.file_uploader(
        "",
        type="csv",
        accept_multiple_files=True
        )

    student_dict = {}

    if csv_files:
        # Build file dictionary {file, list of names}
        file_dict = helpers.build_file_dict(csv_files)
        for filename, content in file_dict.items():
            if not content:
                st.write(f"Warning: {filename} is missing content.")

        # Build student dictionary {name, list of classes}
        student_dict = helpers.build_student_dict(file_dict)

    st.subheader("Here are your matches:")

    # Build dictionary of matches {student, list of classes}
    matches = {
        student: classes
        for student, classes in student_dict.items()
        if len(classes) > 1
    }

    # Output person's name with their classes
    if matches:
        for student, classes in matches.items():
            st.write(f"{student} ({', '.join(classes)})")

    else:
        st.write("No matches found.")