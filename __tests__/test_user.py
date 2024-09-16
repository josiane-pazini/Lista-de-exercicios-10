#1 - Incluir, consultar, alterar e excluir um usuário, sempre com o teste do Status Code 
# e pelo menos 3 testes de campos do retorno.

#1-Bibliotecas
import json
import pytest
import requests

from utils.utils import ler_csv


#2-Classe

#2.1-Atributos ou variaveis

id = 117016598
username = "jo"
firstName = "Usuario"
lastName ="Swagger"
email = "swagger@usuario-edu.com.br"
password = "123456"
phone = "99999999"
userStatus = 1
url = 'https://petstore.swagger.io/v2/user'
headers={'Content-Type': 'application/json'}

#2.2-Funções /métodos

def test_post_user():
   #configura
    user=open('./fixtures/json/user1.json')
    data=json.loads(user.read()) 

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
    assert response_body['code'] ==200
    assert response_body['type'] == 'unknown'
    assert response_body['message'] == str (id)


def test_get_user():
    response=requests.get(
        url=f'{url}/{username}',
        headers=headers
    )

    response_body=response.json()
    assert response.status_code == 200
    assert response_body['id']== id
    assert response_body['username'] == username
    assert response_body['firstName']==firstName
    assert response_body['lastName']== lastName
    assert response_body['email']==email
    assert response_body['password']== password
    assert response_body['phone'] ==phone
    assert response_body['userStatus'] == userStatus

def test_put_user():
    user=open('./fixtures/json/user2.json')
    data = json.loads(user.read())
    username = data['username']

    response=requests.put(
        url=f'{url}/{username}',
        headers=headers,
        data=json.dumps(data),
        timeout=5    
    )

    response_body = response.json()

    assert response.status_code == 200
    assert response_body['code'] ==200
    assert response_body['type'] == 'unknown'
    assert response_body['message']== str(id)

def test_delete_user():

    response = requests.delete(
        url=f'{url}/{username}',
        headers=headers
    )

    response_body = response.json()

    assert response.status_code == 200
    assert response_body['code']==200
    assert response_body['type']=='unknown'
    assert response_body['message'] == username

    #3 - Altere a função Post e Delete da entidade User para que executem os testes a 
    # partir de uma massa com json dinamico

@pytest.mark.parametrize('id,username,firstName,lastName,email,password,phone,userStatus',
                         ler_csv('./fixtures/csv/users.csv'))

def test_post_user_dinamico(id,username,firstName,lastName,email,password,phone,userStatus):

    #configura
    user = {}
    user['id'] = int(id)
    user['username'] = username
    user['firstName']=firstName
    user['lastName']= lastName
    user['email']=email
    user['password']= password
    user['phone']= phone
    user['userStatus']= int(userStatus)

    user = json.dumps(obj=user, indent=4)
    print('\n'+ user)

    #executa 
    response=requests.post(
        url=url,
        headers=headers,
        data=user,
        timeout = 5
     )

    #valida / compara
    response_body = response.json()

    assert response.status_code == 200
    assert response_body['code'] ==200
    assert response_body['type'] == 'unknown'
    assert response_body['message'] == str(id)

@pytest.mark.parametrize('id,username,firstName,lastName,email,password,phone,userStatus',
                         ler_csv('./fixtures/csv/users.csv'))
def test_delete_user_dinamico(id,username,firstName,lastName,email,password,phone,userStatus):

     response = requests.delete(
        url=f'{url}/{username}',
        headers=headers
     )

    # Valida / Compara
     response_body = response.json()

     assert response.status_code == 200
     assert response_body['code'] == 200
     assert response_body ['type'] == 'unknown'
     assert response_body['message'] == username

   # assert response.status_code == 200
   # assert response_body['id'] == int(user_id)
   # assert response_body['username'] == user_username
   # assert response_body['firstName']==user_firstName
   # assert response_body['lastName']== user_lastName
   # assert response_body ['email']==user_email
   # assert response_body['password']== user_password
   # assert response_body['phone']== user_phone
   # assert response_body['userStatus']== int(user_userStatus)