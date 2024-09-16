#2 - Incluir, consultar e excluir um pedido de compra, sempre com o teste do Status Code 
# e pelo menos 3 testes de campos do retorno.

#1- Biblioteca
import json
import pytest
import requests

#2- Classe

#2.1 - Atributos ou variaveis

store_order = 1
store_petId= 117659801
store_quantity = 1
#store_status = "placed"
url = 'https://petstore.swagger.io/v2/store/order'
headers={'Content-Type': 'application/json'}

#2.2 - Funções / métodos

def test_post_store():
    store=open ('./fixtures/json/store1.json')
    data=json.loads(store.read()) 

    #executa
    response = requests.post(
        url=url,
        headers=headers,
        data=json.dumps(data),
        timeout=5
    )

    #valida
    response_body = response.json()

    assert response.status_code == 200
    assert response_body['id']== store_order
    assert response_body['petId']== store_petId
    assert response_body['quantity']== store_quantity
    assert response_body['status']== 'placed'

def test_get_store():
    
    response=requests.get(
        url=f'{url}/{store_order}',
        headers=headers
    )
    response_body=response.json()
    
    assert response.status_code == 200
    assert response_body['id']==store_order
    assert response_body['petId']==store_petId
    assert response_body['quantity']==store_quantity
    assert response_body['status']=='placed'
    assert response_body['complete']== True

def test_delete_store():
    response = requests.delete(
        url=f'{url}/{store_order}',
        headers=headers
    )
    response_body = response.json()

    assert response.status_code == 200
    assert response_body['code']==200
    assert response_body['type']=='unknown'
    assert response_body['message'] == str(store_order)
