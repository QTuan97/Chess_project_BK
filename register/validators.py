from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

def validate_email(value):
    if not "@gmail.com" in value:
        raise ValidationError("Require Google email - @gmail.com")
    return value
