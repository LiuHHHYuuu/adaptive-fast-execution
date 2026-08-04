def parse_user(payload):
    if payload is None:
        return None

    return payload["name"].strip()
