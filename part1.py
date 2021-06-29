import csv

outfile = open("student_name.csv", 'w')
outfile_header = "First Name,Last Name\n"
outfile.write(outfile_header)

with open("Grades.csv", 'r') as infile:
    reader = csv.reader(infile, delimiter=",")
    header = next(reader)
    
    for row in reader:
        student_first_name = row[0]
        student_last_name = row[1]
        student_year = row[2]
        student_grade = row[3]
        # print(student_first_name, student_last_name, student_year, student_grade )
        line = "{},{}\n".format(student_first_name, student_last_name)
        outfile.write(line)
outfile.close()
