from datetime import date

class BaseAppException(Exception):
    """This is the base exception for all application errors"""
    def __init__(self, message: str, status_code: int = 400):
        super().__init__(message)
        self.message = message
        self.status_code = status_code

class InvalidDueDateError(BaseAppException):
    """Raised when a task has been created with a due date in the past"""
    def __init__(self, due_date: date):
        super().__init__(
            message=f"Due date '{due_date}' is in the past.",
            status_code=400
        )
