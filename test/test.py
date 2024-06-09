#from controller import *
#from controller.exceptions.my_exceptions import DuplicateUsernameError
from controller.user_controller import UserController
#from model.entity import *
#from model.da import *

# raise DuplicateUsernameError()
# Test Passed

UserController.save("aaa",
                    "bbb",
                    "male",
                    "1111111111",
                    "56/78/90",
                    "ccccc",
                    "22222222222",
                    "dddddd",
                    "rrrrrr",
                    "3",
                    "yyyyy",
                    "student")