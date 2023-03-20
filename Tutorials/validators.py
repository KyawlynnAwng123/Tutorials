from django.core.exceptions import ValidationError

def email_validate_error(value):
    if not "kyawlinnaung" in value:
        raise ValidationError("You must be enter an email which is kyawlinnaung")
    

    else:
        return value
    
def username_validate_error(vlaue):
    if len(vlaue) > 5:
        raise ValidationError("User Name Must Be MoreThan Five")
    
    else:
        return vlaue

