import json

from .utils import get_access_token

def test_all_roles(client):

    query = json.dumps(
        {'query':
         '''query Q {
              allRoles{
                edges{
                  node{
                    id
                    name
                    users{
                      edges{
                        node{
                          id
                          name
                          nickName
                          email
                        }
                      } 
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
    assert content['data']['allRoles'] != ''
    assert content['data']['allRoles']['edges'] != ''

    roles = content['data']['allRoles']['edges']
    assert len(roles) == 1

    for i in range(len(roles)):
      role_node = roles[i]['node']
      assert role_node['name'] == 'ADMINISTRATOR'  

      users = role_node['users']['edges']

      for j in range(len(users)):
        user_node = users[j]['node']
        assert user_node['name'] == 'root'
        assert user_node['nickName'] == 'root'
        assert user_node['email'] == 'root@flask.com'