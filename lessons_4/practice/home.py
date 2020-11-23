from datetime import date


class Authorization:

    users = []

    def __init__(self, login, password):
        self._login = login
        self._password = password
        self.is_auth = False

    @property
    def login(self):
        return self._login

    @property
    def password(self):
        return self._password

    def check_login(self):
        if Authorization.users:
            list_login = [i['login'] for i in Authorization.users if self.login == i['login']]
            return len(list_login) == 0
        return True

    def check_password(self):
        return any(map(str.isdigit, self.password)) and \
               any(map(str.isalpha, self.password)) and \
               len(self.password) >= 8

    def check_in(self):
        if self.check_login():
            if self.check_password():
                data = {'login': self.login, 'password': self.password, 'is_auth': self.is_auth,
                        'user': self}
                Authorization.users.append(data)
                print(f'Welcome {self.login}, you are registered')
            else:
                print(f'{self.password} must contain more than or equal to 8 characters and numbers')
        else:
            print(f'With this User {self.login} already exists')

    def check_in_new(self, login, password):
        self.__init__(login, password)
        self.check_in()

    def authentication(self, login, password):
        if self.check_login():
            print("You have not registered")
            return
        if self.is_auth:
            print("You are already signed in")
            return
        if self.login == login and self.password == password:
            self.is_auth = True
            list_auth = [i for i in Authorization.users if self.login == i['login']]

            for i in list_auth:
                i['is_auth'] = self.is_auth
            print(f"User {self.login} have successfully signed in")
        else:
            print("Invalid username or password")

    def logout(self):
        if self.is_auth:
            self.is_auth = False
            list_auth = [i for i in Authorization.users if self.login == i['login']]

            for i in list_auth:
                i['is_auth'] = self.is_auth
            print(f"User {self.login} have successfully signed out")
        else:
            print("You are not logged in")


class User(Authorization):

    list_post = []

    def __init__(self, login, password, is_admin):
        super(User, self).__init__(login, password)
        self.is_admin = is_admin
        self.date_created = date.today()

    def check_in_new(self, login, password, is_admin=False):
        if self.is_auth:
            print("You are not logged out")
            return
        self.__init__(login, password, is_admin)
        self.check_in()

    def show_users(self):
        if not self.is_admin:
            print("You are not admin")
            return
        jj = 1
        for i in Authorization.users:
            list_post = [j for j in User.list_post if j.user.login == i["login"]]
            print(f'{jj}. User {i["login"]} '
                  f'date register {i["user"].date_created} '
                  f'{"not have" if len(list_post)==0 else "have" } posts:')
            jj += 1
            for k in list_post:
                print(k.post)


class Post:

    def __init__(self, post, user):
        self.post = post
        self.date_created = date.today()
        self.user = user

    def create_post(self):
        User.list_post.append(self)


if __name__ == "__main__":
    user = User('Vasya', 'fsfsr43fs', False)
    user.check_in()
    user.authentication('Vasya', 'fsfsr43fs')
    user.logout()
    user.check_in_new('Tanya', 'er3eri44', True)
    # # user.logout()
    # user.check_in_new('Vasiliy', 'edceee', False)
    user.authentication('Tanya', 'er3eri44') 
    post = Post('1 pos3t', user)
    post.create_post()
    # user.check_in_new('SDS', '332sddddd', True)

    user.show_users()