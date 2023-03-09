def getStudentCount ():   
    return int (input ("Enter the number of students: "))

def getCourseCount ():
    return int (input ("Enter the number of courses: "))

def getCourseDetails ():
    cID = input ("Enter course ID: ")
    cName = input ("Enter course name: ")
    return cID, cName

def getStudentDetails ():
    sID = input ("Enter student ID: ")
    sName = input ("Enter student name: ")
    sDOB = input ("Enter student's DOB: ")
    return sID, sName, sDOB

def getMarks (sID, cID):
    prompt = f"Enter marks for student {sID} for course {cID}: ".format (sID, cID)
    input (prompt)
    nStudents = getStudentCount ()
    studentLst = []
    for i in range (nStudents):
        sID, Name, DOB = getStudentDetails ()
        studentLst.append ((sID, Name, DOB))
        nCourses = getCourseCount ()
        courseLst = []
        for i in range (nCourses):
            cID, cName = getCourseDetails ()
            courseLst.append ((cID, cName))
            d = {}
            n = int (input ("Enter the number of student-course marks do you want to enter:"))
            for i in range (n):
                while True:
                    sID = input ("Enter student ID: ")
                    cID = input ("Enter course ID: ")
                    if sID not in [student [0] for student in studentLst]:
                        print ("Invalid student ID")
                        continue
                    if cID not in [course [0] for course in courseLst]:
                        print ("Invalid course ID")
                        continue
                    break
                mark = int (input ("Enter mark: "))
                if cID in d:
                    d [cID].append ((sID, mark))
                else:
                    d [cID] = [(sID, mark)]
                    print ("\nListing all students ...")
                    for s in studentLst:
                        print (f"Student ID: {s[0]} Name: {s[1]} DOB: {s[2]}")
                        print ("\nListing all courses ...")
                        for c in courseLst:
                            print (f"Course ID: {c[0]} Name: {c[1]}")
                        cID = input ("\nWhich course do you want to see all student marks for?")
                        if cID in d:
                            for tups in d [cID]:
                                print (f"Student {tups[0]} got {tups [1]} marks")
                        else :
                            print ("Invalid course ID")
                            print ("End of program")