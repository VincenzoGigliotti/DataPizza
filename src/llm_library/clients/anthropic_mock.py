from .base import LLMClient, PromptInput, ResponseOutput
from typing import Dict, Any
import time
import logging

class AnthropicMockClient(LLMClient):
    def load(self):
        self.logger.info("AnthropicMockClient: Caricamento...")
        time.sleep(0.1)
        self.loaded = True
        self.logger.info("AnthropicMockClient: Caricato.")

    def configure(self, new_config: Dict[str, Any]):
        self.logger.debug(f"AnthropicMockClient: Aggiornamento configurazione: {new_config}")
        self.config.update(new_config)

    def respond(self, prompt_input: PromptInput) -> ResponseOutput:
        if not self.loaded:
            self.logger.error("AnthropicMockClient: Modello non caricato.")
            raise RuntimeError("Modello non caricato")

        self.logger.info(f"AnthropicMockClient: {prompt_input.prompt}")
        response_text = f"Anthropic mock response to: {prompt_input.prompt} with context {prompt_input.context}"
        return ResponseOutput(response=response_text)
