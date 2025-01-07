from http.client import *
import json

class HTTP:
    def __init__(self, base_url: str):
        self.conn = HTTPSConnection(base_url)

    def get(self, endpoint: str, headers: dict= {}) -> dict:
        conn = self.conn
        conn.request("GET", endpoint, headers=headers)
        data = get_response(conn)
        return decode_reponse(data)
        
    def post(self, endpoint: str, body: dict, headers: dict) -> dict:
        body_json = json.dumps(body)
        print(body_json)
        conn = self.conn
        conn.request("POST", endpoint, body=body_json, headers=headers)
        data = get_response(conn)
        return decode_reponse(data)
        


def get_response(conn: HTTPSConnection)->bytes:
    response = conn.getresponse()
    data = response.read()
    return data

def decode_reponse(data: bytes)-> dict:
    try:
        return json.loads(data.decode("utf-8"))
    except json.JSONDecodeError:
        return {"error": "Invalid JSON response", "data": data.decode("utf-8")}