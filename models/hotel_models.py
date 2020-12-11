from pydantic import BaseModel

class HotelIn(BaseModel):
    #hotelname: str
    ciudad: str
    zona: str

class HotelInU(BaseModel):
    hotelname: str
    ciudad: str
    zona: str
    tarifa_inicial: str

class HotelOut(BaseModel):
    hotelname: str
    estrellas: str
    tipo_habitacion: str
    tarifa_inicial:str
    #ciudad: str
    zona: str
    
