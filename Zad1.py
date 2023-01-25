import logging
from sys import argv


def logs():
    level = logging.DEBUG
    levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
    
    if len(argv) == 2 and argv[1].upper() not in levels:
        print("Invalid argument, choose from: DEBUG, INFO, WARNING, ERROR or CRITICAL")
    elif len(argv) != 2:
        print("There should be one command-line argument")
    else:
        if argv[1].upper() == levels[0]:
            level = logging.DEBUG
        elif argv[1].upper() == levels[1]:
            level = logging.INFO
        elif argv[1].upper() == levels[2]:
            level = logging.WARINIG
        elif argv[1].upper() == levels[3]:
            level = logging.ERROR
        else:
            level = logging.CRITICAL
    
    logging.basicConfig(level=level, format="%(asctime)s / %(message)s")
    
    # Space for logs declaration
