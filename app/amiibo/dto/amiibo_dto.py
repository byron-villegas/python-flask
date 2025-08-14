class AmiiboDto:
    def __init__(self, name, character, image, amiiboSeries, gameSeries):
        self.name = name
        self.character = character
        self.image = image
        self.amiiboSeries = amiiboSeries
        self.gameSeries = gameSeries

    @classmethod
    def from_json(cls, amiibo):
        return cls(
            name=amiibo.get("name"),
            character=amiibo.get("character"),
            image=amiibo.get("image"),
            amiiboSeries=amiibo.get("amiiboSeries"),
            gameSeries=amiibo.get("gameSeries")
        )
    
    def to_dict(self):
        return {
            "name": self.name,
            "character": self.character,
            "image": self.image,
            "amiiboSeries": self.amiiboSeries,
            "gameSeries": self.gameSeries
        }