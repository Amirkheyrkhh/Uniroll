import re


class Validator:
    @classmethod
    def name_validator(cls, name, message):
        if isinstance(name, str) and re.match(r"^[a-zA-Z\s]{2,30}$", name):
            return name
        else:
            raise ValueError(message)

    @classmethod
    def family_validator(cls, family, message):
        if isinstance(family, str) and re.match(r"^[a-zA-Z\s]{2,30}$", family):
            return family
        else:
            raise ValueError(message)

    @classmethod
    def username_validator(cls, username, message):
        if re.match(r"^[\w@!#$%^&*\s]{2,30}$", username):
            return username
        else:
            raise ValueError(message)

    @classmethod
    def password_validator(cls, password, message):
        if re.match(r"^[\w@!#$%^&*\s]{2,16}$", password):
            return password
        else:
            raise ValueError(message)

    @classmethod
    def national_code_validator(cls, national_code, message):
        if re.match(r"^[0-9]{2,10}$", national_code):
            return national_code
        else:
            raise ValueError(message)

    @classmethod
    def phone_number_validator(cls, phone_number, message):
        if re.match(r"^[0-9]{11}$", phone_number):
            return phone_number
        else:
            raise ValueError(message)

    @classmethod
    def term_validator(cls, term, message):
        if re.match(r"^[0-9]{1,2}$", term):
            return term
        else:
            raise ValueError(message)

    @classmethod
    def capacity_validator(cls, capacity, message):
        if re.match(r"^[0-9]{1,3}$", capacity):
            return capacity
        else:
            raise ValueError(message)