import csv
import io

def build_file_dict(files):
    """Returns dictionary mapping a file to list of names"""
    file_dict = {}

    for file in files:
        class_name = file.name
        file_dict[class_name] = create_names_list(file)

    return file_dict

def create_names_list(file):
    """Creates a new list of just names"""

    # Convert uploaded file's binary content
    # into a text stream for CSV parsing
    string_io = io.StringIO(file.getvalue().decode("utf-8"))

    # Create CSV reader to iterate over rows from text stream
    csv_reader = csv.reader(string_io)

    next(csv_reader, None) 

    # Return list of "row[0].strip()"s per existing row
    return [row[0].strip() for row in csv_reader if row]
    
def build_student_dict(file_dict):
    """Returns dictionary of students {name, class list}"""
    student_dict = {}

    for filename, classmates in file_dict.items():
        populate_dict(filename, classmates, student_dict)

    return student_dict
        
def populate_dict(filename, classmates, student_dict):
    """Adds/Updates students and their classes"""
    for name in classmates:
        if name not in student_dict:
            student_dict[name] = []
        if filename not in student_dict[name]:
            student_dict[name].append(filename)