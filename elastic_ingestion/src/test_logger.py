from datetime import date, datetime
# import os.path
# from os import path
import pathlib
from argparse import ArgumentParser
import json


LOGGER_DIR = 'logger/'

parser = ArgumentParser(description='A simple script for creating test logs.')
parser.add_argument('--log_type', choices=['info', 'error'], default='info')
args = parser.parse_args()
log_type = args.log_type


def main():
    today = date.today()

    # file_exists = check_for_current_file(today)
    try:
        file = open(LOGGER_DIR + str(today) + '.json', 'a+')
        sample_log = {}
        if 'info' in log_type:
            sample_log = create_info_log()
        else:
            sample_log = create_error_log()

        file.write(json.dumps(sample_log))
        file.write("\n")
        file.close()
    except Exception as e:
        print("Error executing the script ", str(e))


def check_for_current_file(today):
    file = pathlib.Path(LOGGER_DIR + str(today) + '.json')
    return file.exists()


def create_info_log():
    now = datetime.now().isoformat()
    message = 'This is a sample log for testing. No errors!'
    service = {
        'name': 'log_tester',
        'type': 'logger',
        'environment': 'test'
    }
    sample_log = {
        'timestamp': now,
        'message': message,
        'service': service,
        'log': {
            'level': log_type
        }
    }
    return sample_log


def create_error_log():
    now = datetime.now().isoformat()
    message = 'This is a sample log for testing with errors!'
    service = {
        'name': 'log_tester',
        'type': 'logger',
        'environment': 'test'
    }
    sample_log = {
        'timestamp': now,
        'message': message,
        'service': service,
        'log': {
            'level': log_type
        }
    }
    return sample_log


if __name__ == '__main__':
    main()
