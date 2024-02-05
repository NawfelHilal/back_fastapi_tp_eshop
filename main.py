from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from datetime import date

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permet à toutes les origines
    allow_credentials=True,
    allow_methods=["*"],  # Permet toutes les méthodes
    allow_headers=["*"],  # Permet tous les headers
)


# Définition du modèle de données
class Product(BaseModel):
    id: int
    marque: str
    modele: str
    prix: int
    imageUrl: str
    description: str
    likes: int
    btnValue: str
    date: date
    isFavorite: bool
    colors: List[str]


# Base de données fictive
products_db = [
    # Produit BMW M3
    {
        "id": 1,
        "marque": "Bmw",
        "modele": "M3",
        "prix": 80000,
        "imageUrl": "https://cdn.automobile-propre.com/uploads/2023/09/BMW-M3.jpg",
        "description": "BMW M3 COMPETITION BERLINE. · Moteur essence hautes performances 6 cylindres en ligne M TwinPower Turbo développant une puissance de 510 ch · Boîte de vitesses ...",
        "likes": 0,
        "btnValue": "Like",
        "date": date(2023, 9, 20),
        "isFavorite": True,
        "colors": ["Noir", "Blanc", "Rouge", "Gris"],
    },
    # Produit Mercedes CLA45s
    {
        "id": 2,
        "marque": "Mercedes",
        "modele": "CLA45s",
        "prix": 65599,
        "imageUrl": "https://www.challenges.fr/assets/img/2019/07/03/cover-r4x3w1000-5d1cd7595a21e-19c0442-058-resultat-jpg.jpg",
        "description": "BMW M3 COMPETITION BERLINE. · Moteur essence hautes performances 6 cylindres en ligne M TwinPower Turbo développant une puissance de 510 ch · Boîte de vitesses ...",
        "likes": 0,
        "btnValue": "Like",
        "date": date(2022, 12, 15),
        "isFavorite": True,
        "colors": ["Noir", "Blanc", "Rouge", "Gris"],
    },
    # Produit AUDI RS6
    {
        "id": 3,
        "marque": "AUDI",
        "modele": "RS6",
        "prix": 88000,
        "imageUrl": "https://www.reezocar.com/raw/autoscout24.it/RZCATSIT54FDBC3F36AE/AUDI-RS6-00.webp",
        "description": "BMW M3 COMPETITION BERLINE. · Moteur essence hautes performances 6 cylindres en ligne M TwinPower Turbo développant une puissance de 510 ch · Boîte de vitesses ...",
        "likes": 0,
        "btnValue": "Like",
        "date": date(2023, 10, 5),
        "isFavorite": False,
        "colors": ["Noir", "Blanc", "Rouge", "Gris"],
    },
    # Produit Mercedes Classe G63
    {
        "id": 4,
        "marque": "Mercedes",
        "modele": "Classe G63",
        "prix": 180000,
        "imageUrl": "https://res.cloudinary.com/dsxfn6o4q/image/upload/c_fill,g_center,h_467,w_624/v1636983788/wkxrrd0gfnmnfw3n5tpm.jpg",
        "description": "BMW M3 COMPETITION BERLINE. · Moteur essence hautes performances 6 cylindres en ligne M TwinPower Turbo développant une puissance de 510 ch · Boîte de vitesses ...",
        "likes": 0,
        "btnValue": "Like",
        "date": date(2023, 10, 5),
        "isFavorite": False,
        "colors": ["Noir", "Blanc", "Rouge", "Gris"],
    },
    # Produit Ford Mustang
    {
        "id": 5,
        "marque": "Ford",
        "modele": "Mustang",
        "prix": 60000,
        "imageUrl": "https://www.largus.fr/images/images/2018-ford-mustang-1.jpg",
        "description": "BMW M3 COMPETITION BERLINE. · Moteur essence hautes performances 6 cylindres en ligne M TwinPower Turbo développant une puissance de 510 ch · Boîte de vitesses ...",
        "likes": 0,
        "btnValue": "Like",
        "date": date(2023, 10, 5),
        "isFavorite": False,
        "colors": ["Noir", "Blanc", "Rouge", "Gris"],
    },
    # Produit Renault Megane 4 RS
    {
        "id": 6,
        "marque": "Renault",
        "modele": "Megane 4 RS",
        "prix": 75000,
        "imageUrl": "https://res.cloudinary.com/dsxfn6o4q/image/upload/c_fill,g_center,h_467,w_624/v1630439206/w8ty0l9aapdd4wb4hqi9.jpg",
        "description": "BMW M3 COMPETITION BERLINE. · Moteur essence hautes performances 6 cylindres en ligne M TwinPower Turbo développant une puissance de 510 ch · Boîte de vitesses ...",
        "likes": 0,
        "btnValue": "Like",
        "date": date(2023, 10, 5),
        "isFavorite": False,
        "colors": ["Noir", "Blanc", "Rouge", "Gris"],
    },
]


@app.get("/products/")
def read_products():
    return products_db


@app.get("/products/{product_id}")
def read_product(product_id: int):
    product = next((p for p in products_db if p["id"] == product_id), None)
    return product or {"error": "Produit non trouvé"}
