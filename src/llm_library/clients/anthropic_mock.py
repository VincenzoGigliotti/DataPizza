from .base import LLMClient
from typing import Dict, Any
import time
import logging

class AnthropicMockClient(LLMClient):

    def load(self):
        self.logger.info("AnthropicMockClient: Caricamento...")
        self.loaded = True
        self.logger.info("AnthropicMockClient: Caricato.")

    def configure(self, new_config: Dict[str, Any]):
        self.logger.debug(f"AnthropicMockClient: Aggiornamento configurazione: {new_config}")
        self.config.update(new_config)

    def respond(self, prompt: str) -> str:
        if not self.loaded:
            self.logger.error("AnthropicMockClient: Modello non caricato, impossibile rispondere.")
            raise RuntimeError("Modello non caricato")
        self.logger.info(f"AnthropicMockClient: Generazione risposta per prompt: {prompt}")
        return f"Anthropic mock response to: {prompt}"
