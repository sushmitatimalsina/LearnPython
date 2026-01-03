def clean_email(email):
    if email is None:
        return "noemail@unknown.com"
    return email.lower()