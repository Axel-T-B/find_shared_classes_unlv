import helpers
import streamlit as st

# Create two equal width columns
st.title("Classmate Finder")
st.subheader("""Directions:
            1. Navigate to the "People" page in one of your classes.
            2. Copy the list and paste into Excel or Google Sheets.
            3. Save as a .csv file and upload the file below.
            4. Repeat until all your classes are uploaded.""")
st.markdown(
    f'<a href="https://axel-t-b.github.io/find_shared_classes_unlv/Classmate%20Finder.pdf" target="_blank"> 🔎 Want visuals? Click here</a>', unsafe_allow_html=True
)

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