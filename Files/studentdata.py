#The following sample file called studentdata.txt contains one line for each student in an imaginary class.
#The students name is the first thing on each line, followed by some exam scores.
#The number of scores might be different for each student.


#Using the text file studentdata.txt write a program that prints out the names of students that have more than six quiz scores.



with open("studentdata.txt") as studentdata:
    for line in studentdata:
        line = line.strip()
        value = line.split()
        if len(value) > 7 :
            print(value[0])
    



