import requests


def get_restaurants():
    response = requests.get('http://localhost:5000/api/restaurants')
    if response.status_code != 200:
        return "Error in request get_restaurants"

    return response.json()


def get_restaurants_by_id(restaurant_id):
    response = requests.get(
        'http://localhost:5000/api/restaurants/{}'.format(restaurant_id))
    if response.status_code != 200:
        return "Error in request get_restaurants_by_id"

    return response.json()


def create_restaurant(data):
    response = requests.post(
        'http://localhost:5000/api/restaurants', data=data)
    if response.status_code != 200:
        return "Error in request create_restaurant"

    return response.json()


def edit_restaurant(data):
    response = requests.put('http://localhost:5000/api/restaurants', data=data)
    if response.status_code != 200:
        return "Error in request edit_restaurant"

    return response.json()


def delete_restaurant(restaurant_id):
    response = requests.delete(
        'http://localhost:5000/api/restaurants/{}'.format(restaurant_id))
    if response.status_code != 200:
        return "Error in request delete_restaurant"

    return response.json()


if __name__ == '__main__':
    restaurant = {}

    address = {
        "postalCode": "",
        "addressLocality": "",
        "addressRegion": "",
        "addressCountry": ""
    }

    option = "9"

    while option != "0":
        print("Digite a opção desejada: \n1 - Listar restaurantes\n2 - Listar restaurante por ID\n3 - Criar um novo restaurante\n4 - Editar um restaurante\n5 - Excluir um restaurante\n0 - Sair")
        option = input()

        if option == "1":
            data = get_restaurants()
            break
        elif option == "2":
            id = input("Digite o ID: ")
            data = get_restaurants_by_id(id)
            break
        elif option == "3":
            restaurant["name"] = input("Digite o nome do restaurante: ")
            restaurant["url"] = input("Digite o endereço do site do restaurante: ")
            restaurant["menu"] = input("Digite o menu do restaurante: ")
            restaurant["telephone"] = input("Digite o telefone: ")
            restaurant["priceRange"] = input("Digite o range de preço: ")
            address["postalCode"] = input("Digite o CEP: ")
            address["addressLocality"] = input("Digite endereço: ")
            address["addressRegion"] = input("Digite a região: ")
            address["addressCountry"] = input("Digite o país: ")
            restaurant["address"] = address
            data = create_restaurant(restaurant)
            break
        elif option == "4":
            restaurant["name"] = input("Digite o nome do restaurante: ")
            restaurant["url"] = input("Digite o endereço do site do restaurante: ")
            restaurant["menu"] = input("Digite o menu do restaurante: ")
            restaurant["telephone"] = input("Digite o telefone: ")
            restaurant["priceRange"] = input("Digite o range de preço: ")
            address["postalCode"] = input("Digite o CEP: ")
            address["addressLocality"] = input("Digite endereço: ")
            address["addressRegion"] = input("Digite a região: ")
            address["addressCountry"] = input("Digite o país: ")
            restaurant["address"] = address
            data = edit_restaurant(restaurant)
            break
        elif option == "5":
            id = input("Digite o ID a ser deletado: ")
            data = delete_restaurant(id)
            break
