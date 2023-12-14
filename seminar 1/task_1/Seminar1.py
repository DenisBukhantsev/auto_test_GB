import yaml
from zeep import Client, Settings
with open('config.yaml', 'r', encoding="utf-8") as f:
    data = yaml.safe_load(f)

settings = Settings(strict= False)
client = Client(wsdl=data.get("path"), settings=settings)

def check_Text(text):

    a = client.service.checkText(text)[0]["s"]
    return a



