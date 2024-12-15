import pytest
from my_llm_lib.clients.anthropic_mock import AnthropicMockClient

def test_anthropic_mock_client():
    c = AnthropicMockClient(config={"api_key": "test"})
    with pytest.raises(RuntimeError):
        c.respond("another prompt")
    c.load()
    response = c.respond("another prompt")
    assert "Anthropic mock response to: another prompt" in response
    c.configure({"max_tokens": 100})
    assert c.config["max_tokens"] == 100
