import random
import string
import json
from typing import Dict

def generate_unique_id(length : int = 7) -> str:
    characters = string.ascii_letters + string.digits
    unique_id = ''.join(random.choice(characters) for _ in range(length))
    
    return unique_id


def load_database() -> Dict:
    with open('database.json', 'r') as json_file:
        data = json.load(json_file)

    return data

