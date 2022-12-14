import json

def create_exceptions(event: dict) -> dict:
    for keys in event:
        if not isinstance(event[keys],(dict, list)):
            event[keys] = None


def fill_nested_dict(event: dict) -> dict:
    if not isinstance(event, dict):
        return None




if __name__ == '__main__':
    with open('sample_request.json', 'r') as f:
        event = json.load(f)

    print(event)
