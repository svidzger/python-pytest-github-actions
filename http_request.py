import urllib.request
import json
from typing import Dict


def get_json_data() -> Dict[str, str]:
    with urllib.request.urlopen('https://raw.githubusercontent.com/theikkila/postinumerot/master/postcode_map_light.json') as response:
        data = response.read()
    return json.loads(data)