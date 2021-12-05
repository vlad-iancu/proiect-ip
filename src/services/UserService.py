from flask import session, g
from werkzeug.security import check_password_hash
from src.repositories.UserRepository import UserRepository


class UserService:
    def __init__(self) -> None:
        self.userRepository = UserRepository()
        pass

    def register_user(self, username, password):
        if self.userRepository.add(username, password) == -1:
            return f'User {username} is already registered.'

        return 0

    def login_user(self, username, password):
        user = self.userRepository.get_by_username(username)

        if user is None:
            return 'Username not found'
        elif not check_password_hash(user['password'], password):
            return 'Password is incorrect'

        session.clear()
        session['user_id'] = user['id']

        return 0

    def logout():
        session.clear()

    def load_current_user(self):
        user_id = session.get('user_id')

        if user_id is None:
            g.user = None
        else:
            g.user = self.userRepository.get_by_id(user_id)
