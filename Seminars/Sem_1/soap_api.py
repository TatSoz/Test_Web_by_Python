from zeep import Client, Settings
import yaml

with open('config.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)
    wsdl = data['wsdl']

settings = Settings(strict=False)
client = Client(wsdl=wsdl, settings=settings)


def check_text(text: str) -> list[str]:
    resp =client.service.checkText(text)
    return resp[0]['s']

