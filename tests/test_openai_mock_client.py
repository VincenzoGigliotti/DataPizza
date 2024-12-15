import pytest
from my_llm_lib.clients.openai_mock import OpenAIMockClient
from my_llm_lib.clients.base import PromptInput

def test_openai_mock_client():
    c = OpenAIMockClient(config={"api_key": "test"})
    input_data = PromptInput(prompt="test prompt", context="test context")
    with pytest.raises(RuntimeError):
        c.respond(input_data)
    c.load()
    response = c.respond(input_data)
    assert "OpenAI mock response to: test prompt with context test context" in response.response
    c.configure({"temperature": 0.7})
    assert c.config["temperature"] == 0.7
