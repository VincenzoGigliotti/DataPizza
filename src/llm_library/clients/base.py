import abc
import logging
from typing import Any, Dict
from pydantic import BaseModel, Field

class PromptInput(BaseModel):
    prompt: str = Field(..., description="Richiesta")
    context: str = Field(..., description="Contesto obbligatorio")

class ResponseOutput(BaseModel):
    response: str = Field(..., description="Risposta")

class LLMClient(abc.ABC):

    def __init__(self, config: Dict[str, Any], logger: logging.Logger = None):
        self.config = config
        self.logger = logger or logging.getLogger(__name__)
        self.loaded = False

    @abc.abstractmethod
    def load(self):
        pass

    @abc.abstractmethod
    def configure(self, new_config: Dict[str, Any]):
        pass

    @abc.abstractmethod
    def respond(self, prompt_input: PromptInput) -> ResponseOutput:
        pass
