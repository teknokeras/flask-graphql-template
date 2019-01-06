import json

try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode

def test_login(client):
    query = json.dumps(
        {'query':
         '''mutation M {
              	loginUser(email: "root@flask.com", password: "flaskiscool") {
                    accessToken
                    refreshToken
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
    assert content['data']['loginUser'] != ''
    assert content['data']['loginUser']['accessToken'] != ''
    assert content['data']['loginUser']['refreshToken'] != ''
