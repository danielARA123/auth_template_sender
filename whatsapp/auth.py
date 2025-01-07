class AuthTemplate:
    def __init__(self, name: str, to: str, token: str):
        self.name = name
        self.to = to
        self.token = token
    def body(self)->dict:
        return {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": self.to,
        "type": "template",
        "template": {
            "name": self.name,
            "language": {
            "code": "pt_BR"
            },
            "components": [
            {
                "type": "body",
                "parameters": [
                {
                    "type": "text",
                    "text": self.token
                }
                ]
            },
            {
                "type": "button",
                "sub_type": "url",
                "index": "0",
                "parameters": [
                {
                    "type": "text",
                    "text": self.token
                }
                ]
            }
            ]
        }
}
        