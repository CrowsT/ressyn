def fail(info):
    return {
        "response": "fail",
        "info": info,
    }


def processing(info):
    return {
        "response": "processing",
        "info": info,
    }