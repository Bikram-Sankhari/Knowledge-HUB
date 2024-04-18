from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField

INPUT_CLASS = {'class': 'form-input', 'style': 'width:40vw;'}
SUBMIT_CLASS = {'class': 'btn btn-primary', 'style': 'margin-top:40px;'}
# WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()], render_kw=INPUT_CLASS)
    subtitle = StringField("Subtitle", validators=[DataRequired()], render_kw=INPUT_CLASS)
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()], render_kw=INPUT_CLASS)
    body = CKEditorField("Blog Content", validators=[DataRequired()], render_kw=INPUT_CLASS)
    submit = SubmitField("Submit Post", render_kw=SUBMIT_CLASS)


class RegistrationForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()], render_kw=INPUT_CLASS)
    email = EmailField("Email", validators=[DataRequired()], render_kw=INPUT_CLASS)
    password = PasswordField("Password", validators=[DataRequired()], render_kw=INPUT_CLASS)
    submit = SubmitField("Submit", render_kw=SUBMIT_CLASS)


class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired()], render_kw=INPUT_CLASS)
    password = PasswordField("Password", validators=[DataRequired()], render_kw=INPUT_CLASS)
    submit = SubmitField("Submit", render_kw=SUBMIT_CLASS)


class CommentForm(FlaskForm):
    comment = CKEditorField("comment", validators=[DataRequired()], render_kw=INPUT_CLASS)
    submit = SubmitField("Submit Comment", validators=[DataRequired()], render_kw=INPUT_CLASS)
