from app import app, db
from flask import render_template, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user, login_required
from app.forms import CalculateInsulinForm, RegisterForm, LoginForm, CalculateInsulinForm, EditAccountForm
from app.models import User

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # Get data from the form
        username = form.username.data
        email = form.email.data
        password = form.password.data
        breakfast_insulin = form.breakfast_insulin.data
        breakfast_carb = form.breakfast_carb.data
        lunch_insulin = form.lunch_insulin.data
        lunch_carb = form.lunch_carb.data
        dinner_insulin = form.dinner_insulin.data
        dinner_carb = form.dinner_carb.data
        correction_150_199 = form.correction_150_199.data
        correction_200_249 = form.correction_200_249.data
        correction_250_299 = form.correction_250_299.data
        correction_300_349 = form.correction_300_349.data
        correction_350_399 = form.correction_350_399.data
        correction_400 = form.correction_400.data
        
        # Check if useername or email is already in db
        user_exists = User.query.filter((User.username == username)|(User.email == email)).all()
        # if it already exists, return back to register page
        if user_exists:
            flash('User with username {username} or email {email} already exists', 'danger')
            return redirect(url_for('register'))
        
        
        # Create a new user instance using form data
        new_user = User(username=username, email=email, password=password, breakfast_insulin=breakfast_insulin, breakfast_carb=breakfast_carb, lunch_insulin=lunch_insulin, lunch_carb=lunch_carb, dinner_insulin=dinner_insulin, dinner_carb=dinner_carb, correction_150_199=correction_150_199, correction_200_249=correction_200_249,correction_250_299=correction_250_299,correction_300_349=correction_300_349,correction_350_399=correction_350_399,correction_400=correction_400)
        

        login_user(new_user)
        return redirect(url_for('index'))
    
    return render_template('register.html', form=form)

@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
         # Grab the data from the form
        username = form.username.data
        password = form.password.data
        
        # Query user table for user with username
        user = User.query.filter_by(username=username).first()
        
        # If the user does not exist or has incorrect password
        if not user or not user.check_password(password):
            
            # Redirect back to login page
            flash('Username or password incorrect', 'danger')
            return redirect(url_for('login'))
        
        # If user does exist and has correct password, log user in
        login_user(user)
        flash('You have successfully logged in', 'success')
        return redirect(url_for('index'))
        


    return render_template('login.html', form=form)


@app.route('/carbCounter')
def carbCounter():
    return render_template('carbCounter.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/insulinCalculator', methods=["GET", "POST"])
def insulinCalculator():
    form = CalculateInsulinForm()
    form.meal_id.choices = ['Breakfast', 'Lunch', 'Dinner']
    # Grab the data from the form
    carbCount = form.carbCount.data
    currentBG = form.currentBG.data

    
    return render_template('insulinCalculator.html', form=form)
    
@app.route('/edit_account_info', methods=["GET", "POST"])
@login_required
def edit_account_info():
    form = EditAccountForm()
    if form.validate_on_submit():
        # Get data from the form
        breakfast_insulin = form.breakfast_insulin.data
        breakfast_carb = form.breakfast_carb.data
        lunch_insulin = form.lunch_insulin.data
        lunch_carb = form.lunch_carb.data
        dinner_insulin = form.dinner_insulin.data
        dinner_carb = form.dinner_carb.data
        correction_150_199 = form.correction_150_199.data
        correction_200_249 = form.correction_200_249.data
        correction_250_299 = form.correction_250_299.data
        correction_300_349 = form.correction_300_349.data
        correction_350_399 = form.correction_350_399.data
        correction_400 = form.correction_400.data
        
        # Update user info in database
        current_user.breakfast_insulin = breakfast_insulin
        current_user.breakfast_carb = breakfast_carb
        current_user.lunch_insulin = lunch_insulin
        current_user.lunch_carb = lunch_carb
        current_user.dinner_insulin = dinner_insulin
        current_user.dinner_carb = dinner_carb
        current_user.correction_150_199 = correction_150_199
        current_user.correction_200_249 = correction_200_249
        current_user.correction_250_299 = correction_250_299
        current_user.correction_300_349 = correction_300_349
        current_user.correction_350_399 = correction_350_399
        current_user.correction_400 = correction_400
        
        db.session.commit()
        
        flash('You have successfully updated your account info', 'success')    
    return render_template('edit_account_info.html', form=form)

