from argparse import ArgumentParser
from elasticsearch import Elasticsearch


def main():
    pass


def create_index(index_name, client):
    pass


def check_index(index_name, client):
    result = client.indices.get(index=index_name)
    return result


def set_connection(elastic_host):
    client = Elasticsearch(elastic_host)
    return client


if __name__ == '__main__':
    parser = ArgumentParser(description='Script for elk setup jobs.')
    parser.add_argument('--elk_host', required=True,
                        help='The elasticsearch url used for the connection.')
    parser.add_argument('--elk_key', required=False,
                        help='The key used for authenticaion if required.')
    args = parser.parse_args()
    elk_host = args.elk_host
    elk_key = args.elk_key
    main()
