from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField, DecimalField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email, NumberRange

class CourseForm(FlaskForm):
    CourseName = StringField('Course Name', validators=[DataRequired(), Length(max=100)])
    Description = StringField('Description')
    StartDate = DateField('Start Date', format='%Y-%m-%d')
    EndDate = DateField('End Date', format='%Y-%m-%d')
    Price = DecimalField('Price', validators=[DataRequired(), NumberRange(min=0)])
    Submit = SubmitField('Submit')

class InstructorForm(FlaskForm):
    FirstName = StringField('First Name', validators=[DataRequired(), Length(max=50)])
    LastName = StringField('Last Name', validators=[DataRequired(), Length(max=50)])
    Email = StringField('Email', validators=[DataRequired(), Email()])
    PhoneNumber = StringField('Phone Number', validators=[Length(max=15)])
    Submit = SubmitField('Submit')

class StudentForm(FlaskForm):
    FirstName = StringField('First Name', validators=[DataRequired(), Length(max=50)])
    LastName = StringField('Last Name', validators=[DataRequired(), Length(max=50)])
    Email = StringField('Email', validators=[DataRequired(), Email()])
    DateOfBirth = DateField('Date of Birth', format='%Y-%m-%d')
    Submit = SubmitField('Submit')

class EnrollmentForm(FlaskForm):
    StudentID = SelectField('Student', coerce=int, validators=[DataRequired()])
    CourseID = SelectField('Course', coerce=int, validators=[DataRequired()])
    Submit = SubmitField('Submit')

class AssessmentForm(FlaskForm):
    CourseID = SelectField('Course', coerce=int, validators=[DataRequired()])
    AssignmentName = StringField('Assignment Name', validators=[DataRequired()])
    MaxScore = StringField('Max Score', validators=[DataRequired()])
    Submit = SubmitField('Submit')

class GradeForm(FlaskForm):
    AssessmentID = SelectField('Assessment', coerce=int, validators=[DataRequired()])
    StudentID = SelectField('Student', coerce=int, validators=[DataRequired()])
    Score = IntegerField('Score', validators=[DataRequired(), NumberRange(min=0)])
    Submit = SubmitField('Submit')

class CourseInstructorForm(FlaskForm):
    CourseID = SelectField('Course', coerce=int, validators=[DataRequired()])
    InstructorID = SelectField('Instructor', coerce=int, validators=[DataRequired()])
    Submit = SubmitField('Submit')
