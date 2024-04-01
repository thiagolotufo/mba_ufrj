import json
import requests


def get_restaurants():
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.get('http://localhost:5000/api/restaurants', headers=headers)
    if response.status_code != 200:
        return "Error in request get_restaurants"

    return response.json()


def get_restaurants_by_id(restaurant_id):
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.get(
        'http://localhost:5000/api/restaurants/{}'.format(restaurant_id), headers=headers)
    if response.status_code != 200:
        return "Error in request get_restaurants_by_id"

    return response.json()

def get_restaurants_by_city(city_name):
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.get(
        'http://localhost:5000/api/restaurants?city={}'.format(city_name), headers=headers)
    if response.status_code != 200:
        return "Error in request get_restaurants_by_city"

    return response.json()    


def create_restaurant(data):
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(
        'http://localhost:5000/api/restaurants', data=data, headers=headers)
    if response.status_code != 201:
        return "Error in request create_restaurant"
    

    return response.json()


def edit_restaurant(data, restaurant_id):
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.put('http://localhost:5000/api/restaurants/{}'.format(restaurant_id), data=data, headers=headers)
    if response.status_code != 200:
        return "Error in request edit_restaurant"

    return response.json()


def delete_restaurant(restaurant_id):
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.delete(
        'http://localhost:5000/api/restaurants/{}'.format(restaurant_id), headers=headers)
    if response.status_code != 204:
        return "Error in request delete_restaurant"

    return "Restaurante deletado com sucesso!"


if __name__ == '__main__':
    data = {}
    restaurant = {}
    address = {}
    option = "9"

    while option != "0":
        print("Digite a opção desejada: \n1 - Listar restaurantes\n2 - Listar restaurante por ID"+
            "\n3 - Listar restaurantes por nome de cidade\n4 - Criar um novo restaurante\n5 - Editar um restaurante\n6 - Excluir um restaurante\n0 - Sair")
        option = input()
        if option == "1":
            data = get_restaurants()
        elif option == "2":
            id = input("Digite o ID: ")
            data = get_restaurants_by_id(id)
        elif option == "3":
            city = input("Digite o nome da cidade: ")
            data = get_restaurants_by_city(city)            
        elif option == "4":
            restaurant["name"] = input("Digite o nome do restaurante: ")
            restaurant["url"] = input("Digite o endereço do site do restaurante: ")
            restaurant["menu"] = input("Digite o menu do restaurante: ")
            restaurant["telephone"] = input("Digite o telefone: ")
            restaurant["priceRange"] = input("Digite o range de preço: ")
            address["postalCode"] = input("Digite o CEP: ")
            address["streetAddress"] = input("Digite o nome da rua: ")
            address["addressLocality"] = input("Digite o bairro: ")
            address["addressRegion"] = input("Digite a região: ")
            address["addressCountry"] = input("Digite o país: ")
            restaurant["address"] = address
            data = create_restaurant(json.dumps(restaurant))
        elif option == "5":
            id = input("Digite o ID: ")
            restaurant["name"] = input("Digite o nome do restaurante: ")
            restaurant["url"] = input("Digite o endereço do site do restaurante: ")
            restaurant["menu"] = input("Digite o menu do restaurante: ")
            restaurant["telephone"] = input("Digite o telefone: ")
            restaurant["priceRange"] = input("Digite o range de preço: ")
            address["postalCode"] = input("Digite o CEP: ")
            address["streetAddress"] = input("Digite o nome da rua: ")
            address["addressLocality"] = input("Digite o bairro: ")
            address["addressRegion"] = input("Digite a região: ")
            address["addressCountry"] = input("Digite o país: ")
            restaurant["address"] = address
            data = edit_restaurant(json.dumps(restaurant), id)
        elif option == "6":
            id = input("Digite o ID a ser deletado: ")
            data = delete_restaurant(id)
        
        print(data)
