from .base import LLMClient, PromptInput, ResponseOutput
from typing import Dict, Any
import time
import logging

class OpenAIMockClient(LLMClient):
    def load(self):
        self.logger.info("OpenAIMockClient: Caricamento...")
        time.sleep(0.1)
        self.loaded = True
        self.logger.info("OpenAIMockClient: Caricato.")

    def configure(self, new_config: Dict[str, Any]):
        self.logger.debug(f"OpenAIMockClient: Aggiornamento configurazione: {new_config}")
        self.config.update(new_config)

    def respond(self, prompt_input: PromptInput) -> ResponseOutput:
        if not self.loaded:
            self.logger.error("OpenAIMockClient: Modello non caricato.")
            raise RuntimeError("Modello non caricato")

        self.logger.info(f"OpenAIMockClient: {prompt_input.prompt}")
        response_text = f"OpenAI mock response to: {prompt_input.prompt} with context {prompt_input.context}"
        return ResponseOutput(response=response_text)
