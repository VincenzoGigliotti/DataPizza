import pytest
from my_llm_lib.clients.anthropic_mock import AnthropicMockClient
from my_llm_lib.clients.base import PromptInput

def test_anthropic_mock_client():
    c = AnthropicMockClient(config={"api_key": "test"})
    input_data = PromptInput(prompt="another prompt", context="important context")
    with pytest.raises(RuntimeError):
        c.respond(input_data)
    c.load()
    response = c.respond(input_data)
    assert "Anthropic mock response to: another prompt with context important context" in response.response
    c.configure({"max_tokens": 100})
    assert c.config["max_tokens"] == 100
