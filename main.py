import helpers
import streamlit as st

#Upload your class CSV files
st.title("Classmate Finder")
st.subheader("""Directions:
             1. Navigate to the "People" page in one of your classes.
             2. Copy the list of people and paste into Excel or Google Sheets.
             3. Save as a .csv file and upload the file below.
             4. Repeat until all your classes are uploaded.""")

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
    if file_dict == []:
        st.write("Warning: no content found in file")

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