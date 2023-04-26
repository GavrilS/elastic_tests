"""
File for custom configs for the test.
"""


def get_script_index_configs_test():
    configuration = {
        "settings": {
            "index": {
                "number_of_shards": 1,
                "number_of_replicas": 0
            }
        },
        "mappings": {
            "properties": {
                "host": {
                    "type": "keyword"
                },
                "log": {
                    "type": "nested",
                    "properties": {
                        "level": {
                            "type": "keyword"
                        }
                    }
                },
                "service": {
                    "type": "nested",
                    "properties": {
                        "name": {"type": "keyword"},
                        "environment": {"type": "keyword"},
                        "type": {"type": "keyword"}
                    }
                }
            }
        }
    }

    return configuration
