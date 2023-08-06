""" Resolwe module """
from .genapi import DEFAULT_EMAIL, DEFAULT_PASSWD, GenAPI, cache_name, cache_backend

__all__ = ('DEFAULT_EMAIL', 'DEFAULT_PASSWD', 'cache_name', 'cache_backend')


def connect(username, password, url, server_type):
    """ Connect to Resolwe server

    :param username:
    :type username: str

    :param password:
    :type password: str

    :param url:
    :type url: str

    :param server_type: genesis or resolwe
    :type server_type: str

    :return: Instance of GenAPI or ResolweAPI
    """

    if server_type == 'genesis':
        try:
            return GenAPI(username, password, url)
        except Exception as e:
            print(e)
            raise ResolweAuthException(e.args[0]) from e
    else:
        """ Not yet supported """
        pass


class ResolweAuthException(Exception):
    """ A login error occurred. """
