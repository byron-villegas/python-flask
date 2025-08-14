from app.amiibo import client


def get_amiibos():
    amiibos = client.find_amiibos_by_serie("Super Smash Bros")

    return amiibos