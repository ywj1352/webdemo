from repository import user



def get_account_by_id(id : int):
    """
    find account by uer
    :param id: user id
    :return: user dict
    """
    one = user.get_account(1)
    if one is None:
        return "this no user"
    else:
        return one.as_dict()
