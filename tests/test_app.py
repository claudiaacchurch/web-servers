# Tests for your routes go here

# === Example Code Below ===

"""
GET /emoji
"""
def test_get_emoji(web_client):
    response = web_client.get("/emoji")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ":)"

# === End Example Code ===

"""
When: I make a GET request to /
Then: I should get a 200 response
"""
def test_get_wave(web_client):
    # We'll simulate sending a GET request to /wave?name=Dana
    # This returns a response object we can test against.
    response = web_client.get('/wave?name=Dana')

    # Assert that the status code was 200 (OK)
    assert response.status_code == 200

    # Assert that the data returned was the right string
    assert response.data.decode('utf-8') == 'I am waving at Dana'

"""
When: I make a POST request to /submit
And: I send a name and message as body parameters
Then: I should get a 200 response with the right content
"""
def test_post_submit(web_client):
    # We'll simulate sending a POST request to /submit with a name and message
    # This returns a response object we can test against.
    response = web_client.post('/submit', data={'name': 'Dana', 'message': 'Hello'})

    # Assert that the status code was 200 (OK)
    assert response.status_code == 200

    # Assert that the data returned was the right string
    assert response.data.decode('utf-8') == 'Thanks Dana, you sent this message: "Hello"'

def test_get_names_plus_eddie(web_client):
    response = web_client.get('/names?add=Eddie')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Julia, Alice, Karim, Eddie"

def test_get_names_plus_tom(web_client):
    response = web_client.get('/names?add=Tom')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Julia, Alice, Karim, Tom"

def test_get_sorted_names_when_multiple_names_added(web_client):
    response = web_client.get('/names?add=Eddie,Tom')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Alice, Eddie, Julia, Karim, Tom"