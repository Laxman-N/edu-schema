from app import db

class Course(db.Model):
    __tablename__ = 'Courses'
    CourseID = db.Column(db.Integer, primary_key=True)
    CourseName = db.Column(db.String(100), nullable=False)
    Description = db.Column(db.Text)
    StartDate = db.Column(db.Date)
    EndDate = db.Column(db.Date)
    Price = db.Column(db.Numeric(10, 2), nullable=False)
    deleted = db.Column(db.Boolean, default=False)

class Instructor(db.Model):
    __tablename__ = 'Instructors'
    InstructorID = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(50), nullable=False)
    LastName = db.Column(db.String(50), nullable=False)
    Email = db.Column(db.String(100), unique=True, nullable=False)
    PhoneNumber = db.Column(db.String(15))
    deleted = db.Column(db.Boolean, default=False)

class Student(db.Model):
    __tablename__ = 'Students'
    StudentID = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(50), nullable=False)
    LastName = db.Column(db.String(50), nullable=False)
    Email = db.Column(db.String(100), unique=True, nullable=False)
    DateOfBirth = db.Column(db.Date)
    EnrollmentDate = db.Column(db.Date, default=db.func.current_timestamp())
    deleted = db.Column(db.Boolean, default=False)

class Enrollment(db.Model):
    __tablename__ = 'Enrollments'
    EnrollmentID = db.Column(db.Integer, primary_key=True)
    StudentID = db.Column(db.Integer, db.ForeignKey('Students.StudentID'), nullable=False)
    student = db.relationship('Student', backref=db.backref('enrollments', lazy=True))
    CourseID = db.Column(db.Integer, db.ForeignKey('Courses.CourseID'), nullable=False)
    EnrollmentDate = db.Column(db.Date, default=db.func.current_timestamp())
    student = db.relationship('Student', backref='enrollments')
    course = db.relationship('Course', backref='enrollments')
    deleted = db.Column(db.Boolean, default=False)

class Assessment(db.Model):
    __tablename__ = 'Assessments'
    AssessmentID = db.Column(db.Integer, primary_key=True)
    CourseID = db.Column(db.Integer, db.ForeignKey('Courses.CourseID'), nullable=False)
    AssessmentName = db.Column(db.String(100), nullable=False)
    MaxScore = db.Column(db.Integer, nullable=False)
    course = db.relationship('Course', backref='assessments')
    deleted = db.Column(db.Boolean, default=False)

class Grade(db.Model):
    __tablename__ = 'Grades'
    GradeID = db.Column(db.Integer, primary_key=True)
    AssessmentID = db.Column(db.Integer, db.ForeignKey('Assessments.AssessmentID'), nullable=False)
    StudentID = db.Column(db.Integer, db.ForeignKey('Students.StudentID'), nullable=False)
    Score = db.Column(db.Integer, nullable=False)
    assessment = db.relationship('Assessment', backref='grades')
    student = db.relationship('Student', backref='grades')
    deleted = db.Column(db.Boolean, default=False)
class CourseInstructor(db.Model):
    __tablename__ = 'CourseInstructors'
    CourseInstructorID = db.Column(db.Integer, primary_key=True)
    CourseID = db.Column(db.Integer, db.ForeignKey('Courses.CourseID'), nullable=False)
    InstructorID = db.Column(db.Integer, db.ForeignKey('Instructors.InstructorID'), nullable=False)
    AssignmentDate = db.Column(db.Date, default=db.func.current_timestamp())
    course = db.relationship('Course', backref='course_instructors')
    instructor = db.relationship('Instructor', backref='course_instructors')
    deleted = db.Column(db.Boolean, default=False)