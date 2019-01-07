import json

from .utils import get_access_token

def test_all_users(client):

    query = json.dumps(
        {'query':
         '''query Q {
              allUsers{
                edges{
                  node{
                    id
                    name 
                    nickName
                    email
                    role{
                      id
                      name
                    }
                  }
                }
              }
            }
       '''
    })
    response = client.post(
        '/graphql',
        data=query,
        content_type='application/json'
    )

    content = json.loads(response.data)

    assert content['data'] != ''
    assert content['data']['allUsers'] != ''
    assert content['data']['allUsers']['edges'] != ''

    users = content['data']['allUsers']['edges']
    assert len(users) == 1

    assert users[0]['node'] != ''

    user = users[0]['node']
    assert user['name'] == 'root'
    assert user['nickName'] == 'root'
    assert user['email'] == 'root@flask.com'
