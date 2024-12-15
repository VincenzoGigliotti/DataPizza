import pytest
from my_llm_lib.clients.base import LLMClient, PromptInput

class DummyClient(LLMClient):
    def load(self):
        self.loaded = True
    
    def configure(self, new_config):
        self.config.update(new_config)
    
    def respond(self, prompt_input: PromptInput):
        if not self.loaded:
            raise RuntimeError("Modello non caricato")
        return {"response": f"Dummy response to {prompt_input.prompt} in {prompt_input.context}"}

def test_base_client():
    c = DummyClient(config={"param": 1})
    assert c.config["param"] == 1
    c.load()
    assert c.loaded is True
    c.configure({"param": 2})
    assert c.config["param"] == 2
    input_data = PromptInput(prompt="Hello", context="General context")
    response = c.respond(input_data)
    assert "Dummy response to Hello" in response["response"]
