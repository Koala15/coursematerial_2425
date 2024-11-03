def entrance_exam(grade1, grade2, grade3, grade4, grade5):
    skipt_test = 0
    taken_test = 5
    total_grade = 0

    if grade1 is None:
        skipt_test +=1
        taken_test -=1
    else:
        total_grade += grade1

    if grade2 is None:
        skipt_test +=1
        taken_test -=1
    else:
        total_grade += grade2

    if grade3 is None:
        skipt_test +=1
        taken_test -=1
    else:
        total_grade += grade3

    if grade4 is None:
        skipt_test +=1
        taken_test -=1
    else:
        total_grade += grade4

    if grade5 is None:
        skipt_test +=1
        taken_test -=1
    else:
        total_grade += grade5

    if skipt_test >= 2:
        return False
    else:
        if (total_grade / taken_test) >= 12:
            return True
        return False
