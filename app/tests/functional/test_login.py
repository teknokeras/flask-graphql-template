import json

def test_login(client):
    email = "root@flask.com"
    password = "flaskiscool"

    mutation = json.dumps(
        {'query':
         '''mutation M {
              	loginUser(email: "'''+email+'''", password: "'''+password+'''") {
                    accessToken
                    refreshToken
              }
            }
       '''
    })
    response = client.post(
        '/graphql',
        data=mutation,
        content_type='application/json'
    )

    content = json.loads(response.data)

    assert content['data'] != ''
    assert content['data']['loginUser'] != ''
    assert content['data']['loginUser']['accessToken'] != ''
    assert content['data']['loginUser']['refreshToken'] != ''
