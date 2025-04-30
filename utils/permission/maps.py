import requests

def obter_lat_lon(endereco):
    url = "https://nominatim.openstreetmap.org/search"
    parametros = {
        'q': endereco,
        'format': 'json',
        'addressdetails': 1,
        'limit': 1,
        'countrycodes': 'br'  # Foca no Brasil
    }

    resposta = requests.get(url, params=parametros, headers={'User-Agent': 'PythonApp'})
    
    if resposta.status_code == 200 and resposta.json():
        dados = resposta.json()[0]
        return float(dados['lat']), float(dados['lon'])
    else:
        return None

# Exemplo de uso
rua = "Rua 14 de Julho"
numero = "1000"
cidade = "Campo Grande"
estado = "MS"
pais = "Brasil"

endereco_completo = f"{rua}, {numero}, {cidade}, {estado}, {pais}"
coordenadas = obter_lat_lon(endereco_completo)

if coordenadas:
    print(f"Latitude: {coordenadas[0]}, Longitude: {coordenadas[1]}")
else:
    print("Endereço não encontrado.")