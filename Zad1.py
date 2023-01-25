import logging
from sys import argv


def logs(*args):
    levels = {"DEBUG": logging.DEBUG, "INFO": logging.INFO, "WARNING": logging.WARNING, "ERROR": logging.ERROR, "CRITICAL": logging.CRITICAL}
    try:
        level = levels.get(argv[1].upper(), None)
    except IndexError:
        raise KeyError("No command-line argument")

    if len(argv) > 2:
        raise KeyError("There can only be one command-line argument")

    if argv[1].upper() not in levels.keys():
        raise KeyError("Invalid argument, try DEBUG, INFO, WARNING, ERROR or CRITICAL")

    logging.basicConfig(level=level, format="%(asctime)s / %(funcName)s / %(message)s")

    # Space for logs declaration

    # Sample usage:
    # for a in args:
        # logging.info(a)