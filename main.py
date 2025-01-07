from request.http import HTTP
from whatsapp.auth import AuthTemplate
from whatsapp.headers import DefaultHeaders
from env import WHATSAPP_TOKEN, WHATSAPP_BUSINESS_ID

http_client = HTTP("graph.facebook.com")

customer_number = input("\nDigite o número de quem vai receber o template (5511999999999): ")
template_name   = input("\nDigite o nome do template de autenticação que será enviado (verification_code): ")
temp_token      = input("\nDigite o token temporário que será enviado (J$FpnYnP): ")

body = AuthTemplate(name=template_name, to=customer_number, token=temp_token).body()
headers = DefaultHeaders(authorization=f'Bearer {WHATSAPP_TOKEN}').to_dict()

response = http_client.post(
    f"/v20.0/{WHATSAPP_BUSINESS_ID}/messages", 
    body=body, 
    headers=headers,
)

print(response)