from app.utils.format import format_validation_errors


class TestFormatValidationErrorsResponse:
    def test_should_return_errors_object(self):
        expected_response = {
            "amount": ["Must be a number"],
        }

        input_errors = [
            {"loc": ["body", "amount"], "msg": "Must be a number", "type": "type_error.integer"}
        ]
        errors = format_validation_errors(errors=input_errors)
        assert errors == expected_response

    def test_should_return_errors_object_with_multiple_fields(self):
        expected_response = {
            "amount": ["Must be a number"],
            "user_id": ["value_is_missing"],
        }

        input_errors = [
            {"loc": ["body", "amount"], "msg": "Must be a number", "type": "type_error.integer"},
            {"loc": ["body", "user_id"], "msg": "value_is_missing", "type": "value_error.missing"},
        ]
        errors = format_validation_errors(errors=input_errors)
        assert errors == expected_response

    def test_should_return_errors_object_with_multiple_errors_and_multiple_fields(self):
        expected_response = {
            "amount": ["Must be a number", "should be not null"],
            "user_id": ["value_is_missing"],
        }

        input_errors = [
            {"loc": ["body", "amount"], "msg": "Must be a number", "type": "type_error.integer"},
            {"loc": ["body", "amount"], "msg": "should be not null", "type": "value_error.missing"},
            {"loc": ["body", "user_id"], "msg": "value_is_missing", "type": "value_error.missing"},
        ]

        errors = format_validation_errors(errors=input_errors)
        assert errors == expected_response
