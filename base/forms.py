from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import DateField, SelectField, StringField, PasswordField, SubmitField, BooleanField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from base.models import User
from datetime import date


CATEGORY_CHOICES = (
        ('category', 'CATEGORY/INDUSTRY NOT SELECTED'),
        ('fashion', 'Fashion'),
        ('beauty', 'Beauty'),
        ('travel', 'Travel'),
        ('food', 'Food'),
        ('fitness', 'Fitness'),
        ('tech', 'Tech'),
        # ('gaming', 'Gaming'),
        # ('music', 'Music'),
        # ('lifestyle', 'Lifestyle'),
        # ('sports', 'Sports'),
        # ('finance', 'Finance'),
        # ('health', 'Health'),
        # ('education', 'Education'),
        # ('diy', 'DIY'),
        # ('photography', 'Photography')
    )

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)], render_kw={"placeholder": "Username"})
    email = StringField('Email',
                        validators=[DataRequired(), Email()], render_kw={'placeholder': "Email"})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={"placeholder": "Password"})
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')], render_kw={"placeholder": "Confirm Password"})
    is_company = BooleanField("Are you a Sponser?")
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()], render_kw={"placeholder": "Email"})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={"placeholder": "Password"})
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data, is_banned=True).first()
        if user is not None:
            raise ValidationError("Your account has been banned. Please Contact on contact@engagement.in")


class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')

class InfluencerRegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=50)], render_kw={"placeholder": "Username"})
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=20)], render_kw={"placeholder": "Formal Name"})
    category = SelectField('Category',choices=CATEGORY_CHOICES, validators=[DataRequired()], render_kw={"placeholder": "Category"})
    niche = StringField('Niche', validators=[DataRequired(), Length(min=2, max=50)], render_kw={"placeholder": "Niche"})
    reach = IntegerField('Reach', validators=[DataRequired()], render_kw={"placeholder": "Followers(Round to nearest thousand)"})
    profile_url = StringField('Profile Url', validators=[DataRequired(), Length(min=2, max=50)], render_kw={"placeholder": "Profile Url"})
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={'placeholder': "Email"})
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')
    bio = TextAreaField('Bio', validators=[Length(min=2, max=300)], render_kw={'placeholder': "Tell us more about you"})

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')
    
    def validate_category(self, category):
        if category.data == "category":
            raise ValidationError('Please select category')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')
        
    # def validate_name(self, name):
        # if ' ' not in name.data:
        #     raise ValidationError('Enter your full name')



class SponsorRegistrationForm(FlaskForm):
    sponsor_name = StringField('Sponsor name', validators=[DataRequired(), Length(min=2, max=50)], render_kw={"placeholder": "Company/Individual Name"})
    industry = SelectField('Industry',choices=CATEGORY_CHOICES, validators=[DataRequired()], render_kw={"placeholder": "Industry"})
    market_valuation = IntegerField('Market Valuation', validators=[DataRequired()], render_kw={"placeholder": "Market Valuation(Round to nearest thousand)"})
    website = StringField('Website', validators=[DataRequired(), Length(min=2, max=50)], render_kw={"placeholder": "Company's Website"})
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={'placeholder': "Email"})
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')
    bio = TextAreaField('Bio', validators=[Length(min=2, max=300)], render_kw={'placeholder': "Tell us more about you"})

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')
    
    def validate_category(self, category):
        if category.data != "category":
            raise ValidationError('Please select category')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')
        
    # def validate_name(self, name):
        # if ' ' not in name.data:
        #     raise ValidationError('Enter your full name')



class CampaignRegistrationForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=2, max=50)], render_kw={"placeholder": "Title"})
    description = TextAreaField('Description', validators=[Length(min=10, max=300)], render_kw={'placeholder': "Tell us more about campaign"})
    budget = IntegerField('Budget', validators=[DataRequired()], render_kw={"placeholder": "Budget"})
    target_audience = StringField('Target Audience', validators=[DataRequired()], render_kw={'placeholder': "Target Audience"})
    start_date = DateField("Start Date", validators=[DataRequired()])
    end_date = DateField("End date", validators=[DataRequired()])
    picture = FileField('Campaign Picture', validators=[FileAllowed(['jpg', 'png'])])
    is_disabled = BooleanField('Private?')
    category = SelectField('Category',choices=CATEGORY_CHOICES, validators=[DataRequired()], render_kw={"placeholder": "Category"})
    submit = SubmitField('Update')

    # def validate_start_date(self, start_date):
    #     if start_date.data and start_date.data < date.today():
    #         raise ValidationError('Start date must be today or a later date.')

    def validate_end_date(self, end_date):
        if end_date.data and self.start_date.data and end_date.data <= self.start_date.data:
            raise ValidationError('End date must be after the start date.')
        



