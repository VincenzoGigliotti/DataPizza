import pytest
from my_llm_lib.clients.base import LLMClient

class DummyClient(LLMClient):
    def load(self):
        self.loaded = True
    
    def configure(self, new_config):
        self.config.update(new_config)
    
    def respond(self, prompt: str) -> str:
        if not self.loaded:
            raise RuntimeError("Modello non caricato")
        return "Dummy response"

def test_base_client():
    c = DummyClient(config={"param": 1})
    assert c.config["param"] == 1
    c.load()
    assert c.loaded is True
    c.configure({"param": 2})
    assert c.config["param"] == 2
    response = c.respond("Hello")
    assert response == "Dummy response"
