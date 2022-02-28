from functools import wraps
import json
from unittest.mock import patch


def patch_obj_with_json(obj, attr, fixture):
    def outer(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            patcher = patch.object(obj, attr)
            mocked = patcher.start()
            with open(fixture, "rb") as f:
                mocked.return_value = json.load(f)
                func(*args, mocked, **kwargs)
                patcher.stop()
        return wrapper
    
    return outer