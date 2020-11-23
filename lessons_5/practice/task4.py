from datetime import date
import shelve


class Authorization:
 
    FILE = 'users'

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
        with shelve.open(Authorization.FILE) as db:
            return db.get(self.login, None) 

    def check_password(self):
        return any(map(str.isdigit, self.password)) and \
               any(map(str.isalpha, self.password)) and \
               len(self.password) >= 8

    def check_in(self): 
        if self.check_login()==None:
            if self.check_password():
                data = {'login': self.login, 'password': self.password, 'is_auth': self.is_auth,
                        'user': self} 
                with shelve.open(Authorization.FILE) as db:
                    db[self.login] = data
                print(f'Welcome {self.login}, you are registered')
            else:
                print(f'{self.password} must contain more than or equal to 8 characters and numbers')
        else:
            print(f'With this User {self.login} already exists')

    def check_in_new(self, login, password):
        self.__init__(login, password)
        self.check_in()

    def authentication(self, login, password):
        data = self.check_login()
        if data==None:
            print("You have not registered")
            return
        if self.is_auth:
            print("You are already signed in")
            return
        if self.login == login and self.password == password:
            self.is_auth = True 
            data['is_auth'] = self.is_auth
            data['user'] = self
            with shelve.open(Authorization.FILE) as db:
                db[self.login] = data 
            print(f"User {self.login} have successfully signed in")
        else:
            print("Invalid username or password")

    def logout(self):
        if self.is_auth:
            self.is_auth = False
            data = self.check_login()
            data['is_auth'] = self.is_auth
            data['user'] = self
            with shelve.open(Authorization.FILE) as db:
                db[self.login] = data 
            print(f"User {self.login} have successfully signed out")
        else:
            print("You are not logged in")


class User(Authorization): 

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

        with shelve.open(Authorization.FILE) as db: 
            jj = 1
            for login in db:
                data = db.get(login, None) 
                list_post = data.get('posts', [])
                print(f'{jj}. User {data["login"]} '
                f'date register {data["user"].date_created} '
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
        data = self.user.check_login()
        if data.get('posts') == None:
            data['posts'] = [self]
        else:
            data['posts'].append(self)
 
        with shelve.open(Authorization.FILE) as db:
            db[self.user.login] = data  


if __name__ == "__main__":
    user = User('Vasya', 'fsfsr43fs', False)
    user.check_in() 
    user.authentication('Vasya', 'fsfsr43fs')
    user.logout() 
    user.check_in_new('Tanya', 'er3eri44', True)
    # # # user.logout()
    # # user.check_in_new('Vasiliy', 'edceee', False)
    user.authentication('Tanya', 'er3eri44') 
    post = Post('1 post', user)
    post.create_post()
    post = Post('2 post', user)
    post.create_post() 
    user.logout() 
    user.check_in_new('Vasya', 'fsfsr43fs', True)
   
    user.authentication('Vasya', 'fsfsr43fs')
    print(user.login)
    post = Post('3 post', user)
    post.create_post()

    user.show_users()