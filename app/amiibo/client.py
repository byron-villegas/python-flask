import requests

from app.amiibo.dto.amiibo_dto import AmiiboDto

def find_amiibos_by_serie(serie):
    url = f"https://www.amiiboapi.com/api/amiibo/?series={serie}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    amiibo_list = data.get('amiibo', [])
    
    amiibos = [AmiiboDto.from_json(amiibo).to_dict() for amiibo in amiibo_list]

    return amiibos

def find_amiibo_by_name(name):
    url = f"https://www.amiiboapi.com/api/amiibo/?name={name}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    amiibo_data = data.get('amiibo', {})
    amiibo_dto = AmiiboDto.from_json(amiibo_data)
    return amiibo_dto