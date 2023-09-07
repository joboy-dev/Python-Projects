from wtforms import Form, fields
from wtforms.validators import DataRequired, Length, URL

class AddCafeForm(Form):
    '''For to handle adding of cafe'''
    
    cafe_name = fields.StringField(
        label='Cafe Name',
        render_kw={'placeholder': 'Enter cafe name'},
        validators=[
            Length(min=3, max=30, message='Minimum length of 3 characters is needed and a maximum of 30 characters'),
            DataRequired(message='This field is required')
        ]
    )
    
    location = fields.URLField(
        label='Location',
        render_kw={'placeholder': 'Enter a link'},
        validators=[
            DataRequired(message='This field is required'),
            URL(message='Enter a valid url')
        ]
    )
    
    open = fields.TimeField(
        label='Opening Time',
        render_kw={'placeholder': 'Enter opening time e.g. 11AM or 11:10AM'},
        validators=[
            DataRequired(message='This field is required')
        ]
    )
    
    close = fields.TimeField(
        label='Closing Time',
        render_kw={'placeholder': 'Enter closing time e.g. 3PM or 3:30PM'},
        validators=[
            DataRequired(message='This field is required')
        ]
    )
    
    coffee_quality_choices = [
        ('✘', '✘'),
        ('☕', '☕'),
        ('☕☕', '☕☕'),
        ('☕☕☕', '☕☕☕'),
        ('☕☕☕☕', '☕☕☕☕'),
        ('☕☕☕☕☕', '☕☕☕☕☕'),
    ]
    coffee_quality = fields.SelectField(
        label='Select Coffee Quality',
        choices=coffee_quality_choices,
        default='0',
        validators=[
            DataRequired(message='This field is required')
        ]
    )
    
    wifi_strength_choices = [
        ('✘', '✘'),
        ('💪', '💪'),
        ('💪💪', '💪💪'),
        ('💪💪💪', '💪💪💪'),
        ('💪💪💪💪', '💪💪💪💪'),
        ('💪💪💪💪💪', '💪💪💪💪💪'),
    ]
    wifi_strength = fields.SelectField(
        label='Select Wifi Strength',
        choices=wifi_strength_choices,
        default='0',
        validators=[
            DataRequired(message='This field is required')
        ]
    )
    
    power_strength_choices = [
        ('✘', '✘'),
        ('🔌', '🔌'),
        ('🔌🔌', '🔌🔌'),
        ('🔌🔌🔌', '🔌🔌🔌'),
        ('🔌🔌🔌🔌', '🔌🔌🔌🔌'),
        ('🔌🔌🔌🔌🔌', '🔌🔌🔌🔌🔌'),
    ]
    power_strength = fields.SelectField(
        label='Select Power Strength',
        choices=power_strength_choices,
        default='0',
        validators=[
            DataRequired(message='This field is required')
        ]
    )
    
    