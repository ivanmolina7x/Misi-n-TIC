from typing import  Dict
from pydantic import BaseModel

class HotelsInDB(BaseModel):
    hotelname: str
    estrellas: str
    tipo_habitacion: str
    tarifa_inicial:str
    ciudad: str
    zona: str
    
database_hotels = Dict[str, HotelsInDB]

database_hotels = {
    "Bogotá": HotelsInDB(**{"hotelname":"Tequendama", 
                            "estrellas":"4",
                            "tarifa_inicial":"250.000 COP",
                            "tipo_habitacion":"Doble",
                            "ciudad":"Bogotá", 
                            "zona":"Centro"}),
    "Bogotá1": HotelsInDB(**{"hotelname":"Hotel NoTeVayas", 
                            "estrellas":"1",
                            "tarifa_inicial":"15.000 COP",
                            "tipo_habitacion":"Cama individual",
                            "ciudad":"Bogotá", 
                            "zona":"Sur"}),
    "Bogotá2": HotelsInDB(**{"hotelname":"Hotel aquiTeQuedas", 
                            "estrellas":"4",
                            "tarifa_inicial":"40.000 COP",
                            "tipo_habitacion":"sencilla",
                            "ciudad":"Bogotá", 
                            "zona":"Centro"}),
    "Bogotá3": HotelsInDB(**{"hotelname":"Decameron", 
                            "estrellas":"5",
                            "tarifa_inicial":"850.000 COP",
                            "tipo_habitacion":"Doble",
                            "ciudad":"Bogotá", 
                            "zona":"Norte"}),
    "Bogotá4": HotelsInDB(**{"hotelname":"Camaleon", 
                            "estrellas":"5",
                            "tarifa_inicial":"350.000 COP",
                            "tipo_habitacion":"Sencilla",
                            "ciudad":"Bogotá", 
                            "zona":"Centro"}),
}

def get_hotel(hotelname: str):
    if hotelname in database_hotels.keys():
        return database_hotels[hotelname]
    else: 
        return None
    
    
def update_hotel(hotel_in_db: HotelsInDB):
    database_hotels[hotel_in_db.hotelname] = hotel_in_db
    return hotel_in_db
