class DuplicateUsernameError(Exception):
    def __init__(self, *args):
        super().__init__(*args, "duplicate username !!!")

class UserNotFoundError(Exception):
    def __init__(self, *args):
        super().__init__(*args, "User Not Found !!!")

class CourseNotFoundError(Exception):
    def __init__(self, *args):
        super().__init__(*args, "Course Not Found !!!")


class ProfessorNotFoundError(Exception):
    def __init__(self, *args):
        super().__init__(*args, "Professor Not Found !!!")