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

class InvalidDateRangeError(BaseAppException):
    """Raised when a task start date is after the due date"""
    def __init__(self, start_date: date, due_date: date):
        super().__init__(
            message=f"Start date '{start_date}' cannot be before due date '{due_date}'!",
            status_code=400
        )

class InvalidDeleteStatusError(BaseAppException):
    """Raised when a task's status is not set to Final"""
    def __init__(self, task_id:int):
        super().__init__(
            message=f"Task with ID: {task_id}, is not finished or set to Final!",
            status_code=409
        )