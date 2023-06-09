from datetime import datetime
from argparse import ArgumentParser
from elasticsearch import Elasticsearch, helpers
import get_configs as gc


def main():
    client = set_connection(elk_host, elk_key)
    index_exists = check_index('script-logs', client)
    print("Index exists result:\n", index_exists)
    if not index_exists:
        index_created = create_index('script-logs', client)
        print('Result of index creation:\n', index_created)
    # exit()
    sample_log = {}
    logs = []
    if 'info' in log_type:
        for i in range(0, 5):
            sample_log = create_info_log()
            logs.append(sample_log)
    else:
        sample_log = create_error_log()
        logs.append(sample_log)

    send_to_elastic(client, logs)


def send_to_elastic(client, payload):
    result = helpers.bulk(client, gen_data(payload))
    print('Result from the bulk index is\n', result)


def gen_data(payload):
    for item in payload:
        yield item


def create_info_log(log_type='INFO', index='script-logs'):
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
        },
        '_index': index
    }
    return sample_log


def create_error_log(log_type='ERROR', index='script-logs'):
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
        },
        '_index': index
    }
    return sample_log


def create_index(index_name, client):
    configs = gc.get_script_index_configs_test()
    response = client.indices.create(
        index="script-logs",
        settings=configs['settings'],
        mappings=configs['mappings']
    )
    return response


def check_index(index_name, client):
    result = client.indices.exists(index=index_name)
    return result


def set_connection(elastic_host, elastic_key=None):
    if elastic_key:
        client = Elasticsearch([elastic_host], api_key=elastic_key)
    else:
        client = Elasticsearch(elastic_host)
    return client


if __name__ == '__main__':
    parser = ArgumentParser(description='Script for elk setup jobs.')
    parser.add_argument('--elk_host', default='http://elasticsearch:9200',
                        help='The elasticsearch url used for the connection.')
    parser.add_argument('--elk_key', default=None,
                        help='The key used for authenticaion if required.')
    parser.add_argument(
        '--log_type', choices=['info', 'error'], default='info')
    args = parser.parse_args()
    elk_host = args.elk_host
    elk_key = args.elk_key
    log_type = args.log_type
    main()
