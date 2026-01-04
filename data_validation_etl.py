def validate_user(user):
    if not user.get("id"):
        return False
    if not user.get("email"):
        return False
    return True