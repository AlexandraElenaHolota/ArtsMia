from dataclasses import dataclass

from model.artObjects import ArtObject


@dataclass
class Connessioni:
    v1 : ArtObject
    v2 : ArtObject
    peso : int

    def __str__(self):
        return f'Arco: {self.v1.object_id} - {self.v2.object_name} - peso: {self.peso}'

