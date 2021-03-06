import functools

from flask import (
    Blueprint, g, request, jsonify
)

from src.services.UserService import UserService

__userService = UserService()
bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=["POST"])
def register():
    username = request.form['username']
    password = request.form['password']

    if not username:
        return jsonify({'status': 'Username is required.'}), 403
    elif not password:
        return jsonify({'status': 'Password is required.'}), 403

    status = __userService.registerUser(username, password)
    if status:
        return jsonify({'status': f'{status}'}), 403

    return jsonify({'status': 'user registered succesfully'}), 200


@bp.route('/login', methods=["POST"])
def login():
    username = request.form['username']
    password = request.form['password']

    status = __userService.loginUser(username, password)
    if status:
        return jsonify({'status': f'{status}'}), 403

    return jsonify({'status': 'user logged in succesfully'}), 200


@bp.route('/logout')
def logout():
    __userService.logout()

    return jsonify({'status': 'user logged out succesfully'}), 200


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return jsonify({'status': 'User is not authenticated'}), 403

        return view(**kwargs)

    return wrapped_view


@bp.before_app_request
def load_logged_in_user():
    __userService.loadCurrentUser()
