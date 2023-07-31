from flask import current_app


def get_user_name():
    """
    get config user name
    :return: config user name  in yaml
    """
    return current_app.config['user']['name']

def get_password():
    """
    get config user name
    :return: config user name  in yaml
    """
    return current_app.config['user']['password']
