from fastapi import HTTPException


class BaseHttpException(HTTPException):
    detail: str
    error_code: int

    def __init__(
        self, *, status_code: int = 500, detail: str = "", error_code: str = "unhandled_error"
    ):
        self.error_code = error_code
        self.detail = detail
        super().__init__(status_code=status_code)


class DuplicatedAccountException(BaseHttpException):
    def __init__(self) -> None:
        super().__init__(
            status_code=409, detail="Account already exists", error_code="duplicated_account"
        )


class AccountNotFoundException(BaseHttpException):
    def __init__(self) -> None:
        super().__init__(
            status_code=404, detail="Account not found", error_code="account_not_found"
        )


class AccountNotOwnedException(BaseHttpException):
    def __init__(self) -> None:
        super().__init__(
            status_code=403, detail="Account not owned", error_code="account_not_owned"
        )
