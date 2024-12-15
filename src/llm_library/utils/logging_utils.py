from llm_library.clients.openai_mock import OpenAIMockClient

def test_openai_client_response():
    client = OpenAIMockClient()
    client.configure(api_key="test_key")
    response = client.send_request("Hello, OpenAI!")
    assert response == {"response": "Mock response for prompt: 'Hello, OpenAI!'"}
