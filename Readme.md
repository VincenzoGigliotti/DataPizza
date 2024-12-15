# my-llm-lib

**Versione:** 0.2.0

## Requisiti

- Python 3.11 (o compatibile)
- `pip` per installare le dipendenze
- (Opzionale) Docker, se si desidera testare all'interno di un container

## Setup del Progetto

1. Clonare il repository:
   ```bash
   git clone <URL_DEL_REPOSITORY>
   cd my-llm-lib

2. Installare le dipendenze:
pip install -r requirements.txt


Test local:
pytest --maxfail=1 --disable-warnings -v tests

Test Docker:
docker build -t my-llm-lib-test .
docker run --rm my-llm-lib-test
