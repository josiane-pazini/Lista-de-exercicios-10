#1-Bibliotecas
import json
import pytest
import requests     # framework de teste da API


#2-Classe

#2.1-Atributos ou variaveis

pet_id = 117659801
pet_name = "Detetive Labrador"
pet_category_id = 1
pet_category_name= "dog"
pet_tag_id = 1
pet_tag_name = "vacinado"
url= 'https://petstore.swagger.io/v2/pet'
headers={'Content-Type': 'application/json'}

#2.2-Funções /métodos
def test_post_pet():
    #configura
    pet=open('./fixtures/json/pet1.json')             #abre o arquivo json 
    data=json.loads(pet.read())                       #pet.read lê o conteudo e carrega como json em uma variavel chamada data
    # dados de saída / resultado esperado estão nos atributos acima das funções
    
    #executa
    response = requests.post(
        url=url,
        headers=headers,                             #cabeçalho
        data=json.dumps(data),                       #descarrega os dados
        timeout=5
    )
    
    #valida
    response_body = response.json()                 #cria uma variavel e carrega a resposta em formato json
    assert response.status_code == 200
    assert response_body['id'] == pet_id
    assert response_body['name'] == pet_name
    assert response_body['category']['name'] ==pet_category_name
    assert response_body['tags'][0]['name'] == pet_tag_name
    
def test_get_pet():
    #Configura
    #Dados de Entrada e Saida/Resultado esperado estão na seção de atributos antes das funções


    #Executa
    response = requests.get(
        # url = url + f'/{pet_id}',        # opção 1= + serve para concatenar e o F para formatar
        url=f'{url}/{pet_id}',             # opção 2= chama o endereço do get/consulta passando o código do animal
        headers=headers
        #não tem corpo/body
    )

    #Valida
    response_body = response.json()                 #cria uma variavel e carrega a resposta em formato json
    
    assert response.status_code == 200
    assert response_body['id'] == pet_id
    assert response_body['name'] == pet_name
    assert response_body['category']['id'] == pet_category_id
    assert response_body['tags'][0]['id'] == pet_tag_id
    assert response_body['status'] == 'available'
    assert response_body['category']['name'] ==pet_category_name
    assert response_body['tags'][0]['name'] == pet_tag_name

def test_put_pet():
    pet = open ('./fixtures/json/pet2.json')
    data = json.loads(pet.read())

    response = requests.put(
        url = url,
        headers = headers,
        data= json.dumps(data),
        timeout=5
    )

    response_body = response.json()

    assert response.status_code == 200
    assert response_body['id'] == pet_id
    assert response_body['name'] == pet_name
    assert response_body['category']['id'] == pet_category_id
    assert response_body['tags'][0]['id'] == pet_tag_id
    assert response_body['category']['name'] ==pet_category_name
    assert response_body['tags'][0]['name'] == pet_tag_name
    assert response_body['status'] == 'sold'

def test_delete_pet():

    response = requests.delete(
        url=f'{url}/{pet_id}',
        headers=headers,
    )

    response_body = response.json()

    assert response.status_code == 200
    assert response_body['code'] ==200
    assert response_body['type'] == 'unknown'
    assert response_body['message'] == str (pet_id)


    
    