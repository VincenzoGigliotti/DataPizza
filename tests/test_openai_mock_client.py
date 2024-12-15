import pytest
from my_llm_lib.clients.openai_mock import OpenAIMockClient

def test_openai_mock_client():
    c = OpenAIMockClient(config={"api_key": "test"})
    with pytest.raises(RuntimeError):
        c.respond("test prompt")
    c.load()
    response = c.respond("test prompt")
    assert "OpenAI mock response to: test prompt" in response
    c.configure({"temperature": 0.7})
    assert c.config["temperature"] == 0.7
