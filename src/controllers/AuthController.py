import functools

from flask import (
    Blueprint, g, request, jsonify
)
from werkzeug.security import check_password_hash, generate_password_hash

from src.services.UserService import UserService


class AuthController:
    def __init__(self) -> None:
        self.userService = UserService()
        pass

    bp = Blueprint('auth', __name__, url_prefix='/auth')

    @bp.route('/register', methods=["POST"])
    def register(self):

        username = request.form['username']
        password = request.form['password']

        if not username:
            return jsonify({'status': 'Username is required.'}), 403
        elif not password:
            return jsonify({'status': 'Password is required.'}), 403

        status = self.userService.register_user(username, password)
        if status:
            return jsonify({'status': f'{status}'}), 403

        return jsonify({'status': 'user registered succesfully'}), 200

    @bp.route('/login', methods=["POST"])
    def login(self):

        username = request.form['username']
        password = request.form['password']

        status = self.userService.login_user(username, password)
        if status:
            return jsonify({'status': f'{status}'}), 403

        return jsonify({'status': 'user logged in succesfully'}), 200

    @bp.route('/logout')
    def logout(self):

        self.userService.logout()

        return jsonify({'status': 'user logged out succesfully'}), 200

    def login_required(view):

        @functools.wraps(view)
        def wrapped_view(**kwargs):
            if g.user is None:
                return jsonify({'status': 'User is not authenticated'}), 403

            return view(**kwargs)

        return wrapped_view

    @bp.before_app_request
    def load_logged_in_user(self):

        self.userService.load_current_user()
