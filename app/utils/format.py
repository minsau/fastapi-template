def format_validation_errors(errors):
    """
    Format the errors from the validation
    """
    formatted_errors: dict = {}
    for error in errors:
        if error["loc"][1] not in formatted_errors:
            formatted_errors[error["loc"][1]] = []
        formatted_errors[error["loc"][1]].append(error["msg"])
    return formatted_errors
