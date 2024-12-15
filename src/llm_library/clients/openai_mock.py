from .base import LLMClient
from typing import Dict, Any
import time
import logging

class OpenAIMockClient(LLMClient):

    def load(self):
        self.logger.info("OpenAIMockClient: Caricamento...")
        self.loaded = True
        self.logger.info("OpenAIMockClient: Caricato.")

    def configure(self, new_config: Dict[str, Any]):
        self.logger.debug(f"OpenAIMockClient: Aggiornamento configurazione: {new_config}")
        self.config.update(new_config)

    def respond(self, prompt: str) -> str:
        if not self.loaded:
            self.logger.error("OpenAIMockClient: Modello non caricato, impossibile rispondere.")
            raise RuntimeError("Modello non caricato")
        self.logger.info(f"OpenAIMockClient: Generazione risposta per prompt: {prompt}")
        return f"OpenAI mock response to: {prompt}"
