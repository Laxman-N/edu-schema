from flask import Blueprint, render_template, redirect, url_for, flash, request
from app import db
from app.models import Course, Instructor, Student, Enrollment, Assessment, Grade, CourseInstructor
from app.forms import CourseForm, InstructorForm, StudentForm, EnrollmentForm, AssessmentForm, GradeForm, CourseInstructorForm

bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    return render_template('home.html')

@bp.route('/courses')
def courses():
    courses = Course.query.filter_by(deleted=False).all()
    return render_template('courses.html', courses=courses)

@bp.route('/add_course', methods=['GET', 'POST'])
def add_course():
    form = CourseForm()
    if form.validate_on_submit():
        course = Course(CourseName=form.CourseName.data,
                        Description=form.Description.data,
                        StartDate=form.StartDate.data,
                        EndDate=form.EndDate.data,
                        Price=form.Price.data)
        db.session.add(course)
        db.session.commit()
        flash('Course added successfully', 'success')
        return redirect(url_for('main.courses'))
    return render_template('add_course.html', form=form)

@bp.route('/instructors')
def instructors():
    instructors = Instructor.query.filter_by(deleted=False).all()
    return render_template('instructors.html', instructors=instructors)

@bp.route('/add_instructor', methods=['GET', 'POST'])
def add_instructor():
    form = InstructorForm()
    if form.validate_on_submit():
        instructor = Instructor(FirstName=form.FirstName.data,
                                LastName=form.LastName.data,
                                Email=form.Email.data,
                                PhoneNumber=form.PhoneNumber.data)
        db.session.add(instructor)
        db.session.commit()
        flash('Instructor added successfully', 'success')
        return redirect(url_for('main.instructors'))
    return render_template('add_instructor.html', form=form)

@bp.route('/students')
def students():
    students = Student.query.filter_by(deleted=False)
    return render_template('students.html', students=students)

@bp.route('/add_student', methods=['GET', 'POST'])
def add_student():
    form = StudentForm()
    if form.validate_on_submit():
        student = Student(FirstName=form.FirstName.data,
                          LastName=form.LastName.data,
                          Email=form.Email.data,
                          DateOfBirth=form.DateOfBirth.data)
        db.session.add(student)
        db.session.commit()
        flash('Student added successfully', 'success')
        return redirect(url_for('main.students'))
    return render_template('add_student.html', form=form)

@bp.route('/enrollments')
def enrollments():
    enrollments = Enrollment.query.filter_by(deleted=False).all()
    return render_template('enrollments.html', enrollments=enrollments)

@bp.route('/add_enrollment', methods=['GET', 'POST'])
def add_enrollment():
    form = EnrollmentForm()
    form.StudentID.choices = [(student.StudentID, f"{student.FirstName} {student.LastName}") for student in Student.query.all()]
    form.CourseID.choices = [(course.CourseID, course.CourseName) for course in Course.query.all()]
    if form.validate_on_submit():
        enrollment = Enrollment(StudentID=form.StudentID.data, CourseID=form.CourseID.data)
        db.session.add(enrollment)
        db.session.commit()
        flash('Student enrolled successfully', 'success')
        return redirect(url_for('main.enrollments'))
    return render_template('add_enrollment.html', form=form)

@bp.route('/assessments')
def assessments():
    assessments = Assessment.query.afilter_by(deleted=False).all()
    return render_template('assessments.html', assessments=assessments)

@bp.route('/add_assessment', methods=['GET', 'POST'])
def add_assessment():
    form = AssessmentForm()
    form.CourseID.choices = [(course.CourseID, course.CourseName) for course in Course.query.all()]
    if form.validate_on_submit():
        assessment = Assessment(CourseID=form.CourseID.data,
                                AssessmentName=form.AssignmentName.data,
                                MaxScore=form.MaxScore.data)
        db.session.add(assessment)
        db.session.commit()
        flash('Assessment added successfully', 'success')
        return redirect(url_for('main.assessments'))
    return render_template('add_assignment.html', form=form)

@bp.route('/grades')
def grades():
    grades = Grade.query.filter_by(deleted=False).all()
    return render_template('grades.html', grades=grades)

@bp.route('/add_grade', methods=['GET', 'POST'])
def add_grade():
    form = GradeForm()
    form.AssessmentID.choices = [(assessment.AssessmentID, assessment.AssessmentName) for assessment in Assessment.query.all()]
    form.StudentID.choices = [(student.StudentID, f"{student.FirstName} {student.LastName}") for student in Student.query.all()]
    if form.validate_on_submit():
        grade = Grade(AssessmentID=form.AssessmentID.data, StudentID=form.StudentID.data, Score=form.Score.data)
        db.session.add(grade)
        db.session.commit()
        flash('Grade added successfully', 'success')
        return redirect(url_for('main.grades'))
    return render_template('add_grade.html', form=form)

@bp.route('/course_instructors')
def course_instructors():
    course_instructors = CourseInstructor.query.filter_by(deleted=False).all()
    return render_template('course_instructors.html', course_instructors=course_instructors)

@bp.route('/add_course_instructor', methods=['GET', 'POST'])
def add_course_instructor():
    form = CourseInstructorForm()
    form.CourseID.choices = [(course.CourseID, course.CourseName) for course in Course.query.all()]
    form.InstructorID.choices = [(instructor.InstructorID, f"{instructor.FirstName} {instructor.LastName}") for instructor in Instructor.query.all()]
    if form.validate_on_submit():
        course_instructor = CourseInstructor(CourseID=form.CourseID.data, InstructorID=form.InstructorID.data)
        db.session.add(course_instructor)
        db.session.commit()
        flash('Instructor assigned to course successfully', 'success')
        return redirect(url_for('main.course_instructors'))
    return render_template('add_course_instructor.html', form=form)