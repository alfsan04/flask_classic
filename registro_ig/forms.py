from flask_wtf import FlaskForm
from wtforms import DateField, StringField, FloatField, SubmitField
from wtforms.validators import DataRequired, Length


class MovementForm(FlaskForm):
    date = DateField("Fecha", validators=[DataRequired()])
    concept = StringField("Concepto", validators=[DataRequired(), Length(min=4)])
    quantity = FloatField("Cantidad", validators=[DataRequired()])

    submit = SubmitField("Aceptar")