from dataStructs import *
from db.databaseHandler import *

if __name__ == "__main__":
    kevin = Student("6176868207", "Kevin", "Yang", SchoolName.NEWTON_SOUTH, 10)
    roshan = Student("6175525098", "Roshan", "Karim", SchoolName.NEWTON_NORTH, 10)
    
    NORM = Teacher("RYAN", "NORMANDIN", SchoolName.NEWTON_SOUTH)
    PAL = Teacher("ALEX", "PALILUNAS", SchoolName.NEWTON_SOUTH)
    BECKER = Teacher("RACHEL", "BECKER", SchoolName.NEWTON_SOUTH)
    KOZUCH = Teacher("MICAEL", "KOZUCH", SchoolName.NEWTON_SOUTH)
    CROSBY = Teacher("ALAN", "CROSBY", SchoolName.NEWTON_SOUTH)
    RUGG = Teacher("ILANA", "RUGG", SchoolName.NEWTON_SOUTH)

    schedule = Schedule(NORM, PAL, BECKER, KOZUCH, CROSBY, RUGG)

    db = DatabaseHandler(SchoolName.NEWTON_SOUTH)
    db.addStudentToStudentDirectory(kevin)
    db.addTeacherToTeacherDirectory(NORM)
    db.addTeacherToTeacherDirectory(BECKER)
    # print(db.addClassToClasses(db.getTeacherID(NORM), SchoolBlock.A, db.getStudentID(kevin)))
    # db.addStudentToUserDirectory(roshan) 
    db.addTeacherToTeacherDirectory(PAL)
    print(db.getStudent(kevin))
    print(db.getStudent(roshan))
    print(db.getTeacher(NORM))
    print(db.addStudent(kevin, schedule))
    print(db.student_id)
    print(db.queryStudentsByAbsentTeacher(NORM, SchoolBlock.A))
    # print(db.removeStudentFromUserDirectory(kevin))