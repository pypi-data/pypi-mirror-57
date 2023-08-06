import requests
from start_up import URLS, AUTH


async def check_response(resp, topic=None):
    status = resp.status_code
    if status != 200:
        print(f"{topic or ''}request not successful: {status} - {resp.reason}")
    return resp
