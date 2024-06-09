from controller.exceptions.my_exceptions import UserNotFoundError
from model.da.da import Da
from model.entity.user import User


class UserDa(Da):
    def save(self, user):
        self.connect()
        self.cursor.execute(
            "INSERT INTO USER_TBL(NAME, FAMILY, GENDER, NATIONAL_CODE, BIRTHDATE, ADRESS, PHONE_NUMBER, USERNAME, PASSWORD, TERM, COURSES, ROLE) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            [user.name, user.family, user.gender, user.national_code, user.birthday, user.address, user.phone_number,
             user.username, user.password, user.term, user.courses, user.role])
        self.connection.commit()
        self.disconnect()

    def edit(self, user):
        self.connect()
        self.cursor.execute(
            "UPDATE USER_TBL SET NAME=%s,FAMILY=%s,GENDER=%s,NATIONAL_CODE=%s,BIRTHDATE=%s,ADDRESS=%s,PHONE_NUMBER=%s,PASSWORD=%s,TERM=%s,COURSES=%s,ROLE=%s WHERE ID=%s",
            [user.name, user.family, user.gender, user.national_code, user.birthday, user.address, user.phone_number,
             user.password, user.term, user.courses, user.role, user.user_id])
        self.connection.commit()
        self.disconnect()

    def remove(self, user_id):
        self.connect()
        self.cursor.execute("DELETE FROM USER_TBL WHERE ID=%s",
                            [user_id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("SELECT * FROM USER_TBL")
        user_tuple_list = self.cursor.fetchall()
        self.disconnect()
        if user_tuple_list:
            user_list = []
            for user_tuple in user_tuple_list:
                user = User(user_tuple[1], user_tuple[2], user_tuple[3], user_tuple[4], user_tuple[5], user_tuple[6],
                            user_tuple[7], user_tuple[8], user_tuple[9], user_tuple[10], user_tuple[11])
                user.user_id = user_tuple[0]
                user.role = user_tuple[12]
                user_list.append(user)
            return user_list
        else:
            raise UserNotFoundError()

    def find_by_id(self, user_id):
        self.connect()
        self.cursor.execute("SELECT * FROM USER_TBL WHERE ID=%s",
                            [user_id])
        user_tuple = self.cursor.fetchone()
        self.disconnect()
        if user_tuple:
            user = User(user_tuple[1], user_tuple[2], user_tuple[3], user_tuple[4], user_tuple[5], user_tuple[6],
                        user_tuple[7], user_tuple[8], user_tuple[9], user_tuple[10], user_tuple[11])
            user.user_id = user_tuple[0]
            user.role = user_tuple[12]
            return user
        else:
            raise UserNotFoundError()

    def find_by_family(self, family):
        self.connect()
        self.cursor.execute("SELECT * FROM USER_TBL WHERE FAMILY LIKE %s",
                            [family + "%"])
        user_tuple_list = self.cursor.fetchall()
        self.disconnect()
        if user_tuple_list:
            user_list = []
            for user_tuple in user_tuple_list:
                user = User(user_tuple[1], user_tuple[2], user_tuple[3], user_tuple[4], user_tuple[5], user_tuple[6],
                            user_tuple[7], user_tuple[8], user_tuple[9], user_tuple[10], user_tuple[11])
                user.user_id = user_tuple[0]
                user.role = user_tuple[12]
                user_list.append(user)
            return user_list
        else:
            raise UserNotFoundError()

    def find_by_username(self, username):
        self.connect()
        self.cursor.execute("SELECT * FROM USER_TBL WHERE USERNAME=%s",
                            [username])
        user_tuple = self.cursor.fetchone()
        self.disconnect()
        if user_tuple:
            user = User(user_tuple[1], user_tuple[2], user_tuple[3], user_tuple[4], user_tuple[5], user_tuple[6],
                        user_tuple[7], user_tuple[8], user_tuple[9], user_tuple[10], user_tuple[11])
            user.user_id = user_tuple[0]
            user.role = user_tuple[12]
            return user
        else:
            raise UserNotFoundError()

    def find_by_username_and_password(self, username, password):
        self.connect()
        self.cursor.execute("SELECT * FROM USER_TBL WHERE USERNAME=%s AND PASSWORD=%s",
                            [username, password])
        user_tuple = self.cursor.fetchone()
        self.disconnect()
        if user_tuple:
            user = User(user_tuple[1], user_tuple[2], user_tuple[3], user_tuple[4], user_tuple[5], user_tuple[6],
                        user_tuple[7], user_tuple[8], user_tuple[9], user_tuple[10], user_tuple[11])
            user.user_id = user_tuple[0]
            user.role = user_tuple[12]
            return user
        else:
            raise UserNotFoundError()
