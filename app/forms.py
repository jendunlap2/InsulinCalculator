from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo

class RegisterForm(FlaskForm):
    username = StringField('Username :', validators=[DataRequired()])
    email = StringField('Email :', validators=[DataRequired(), Email()])
    password = PasswordField('Password :', validators=[DataRequired()])
    confirm_pass = PasswordField('Confirm Password :', validators=[DataRequired(), EqualTo('password')])
    breakfast_insulin = StringField('Units of Insulin : ', validators=[DataRequired()])
    breakfast_carb = StringField('Grams of Carbohydrates : ', validators=[DataRequired()])
    lunch_insulin = StringField('Units of Insulin : ', validators=[DataRequired()])
    lunch_carb = StringField('Grams of Carbohydrates : ', validators=[DataRequired()])
    dinner_insulin = StringField('Units of Insulin : ', validators=[DataRequired()])
    dinner_carb = StringField('Grams of Carbohydrates : ', validators=[DataRequired()])
    correction_150_199 = StringField('Units Insulin for BG of 150-199', validators=[DataRequired()])
    correction_200_249 = StringField('Units Insulin for BG of 200-249', validators=[DataRequired()])
    correction_250_299 = StringField('Units Insulin for BG of 250-299', validators=[DataRequired()])
    correction_300_349 = StringField('Units Insulin for BG of 300-349', validators=[DataRequired()])
    correction_350_399 = StringField('Units Insulin for BG of 300-349', validators=[DataRequired()])
    correction_400 = StringField('Units Insulin for BG of 400 and above', validators=[DataRequired()])
    submit = SubmitField('Register')
    
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
    
class CalculateInsulinForm(FlaskForm):
    carbCount = StringField('Total Number of Carbohydrates (g) : ', validators=[DataRequired()])
    currentBG = StringField('Current Blood Glucose Reading : ', validators=[DataRequired()])
    meal_id = SelectField('Meal time :')
    submit = SubmitField('Submit')
    
class EditAccountForm(FlaskForm):
    breakfast_insulin = StringField('Units of Insulin : ', validators=[DataRequired()])
    breakfast_carb = StringField('Grams of Carbohydrates : ', validators=[DataRequired()])
    lunch_insulin = StringField('Units of Insulin : ', validators=[DataRequired()])
    lunch_carb = StringField('Grams of Carbohydrates : ', validators=[DataRequired()])
    dinner_insulin = StringField('Units of Insulin : ', validators=[DataRequired()])
    dinner_carb = StringField('Grams of Carbohydrates : ', validators=[DataRequired()])
    correction_150_199 = StringField('Units Insulin for BG of 150-199', validators=[DataRequired()])
    correction_200_249 = StringField('Units Insulin for BG of 200-249', validators=[DataRequired()])
    correction_250_299 = StringField('Units Insulin for BG of 250-299', validators=[DataRequired()])
    correction_300_349 = StringField('Units Insulin for BG of 300-349', validators=[DataRequired()])
    correction_350_399 = StringField('Units Insulin for BG of 350-399', validators=[DataRequired()])
    correction_400 = StringField('Units Insulin for BG of 400 and above', validators=[DataRequired()])
    submit = SubmitField('Submit Changes')