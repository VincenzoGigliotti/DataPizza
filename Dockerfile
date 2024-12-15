FROM python:3.11-slim

WORKDIR /app

COPY my_llm_lib/ my_llm_lib/
COPY tests/ tests/
COPY requirements.txt .
COPY setup.py .

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install .

CMD ["pytest", "--maxfail=1", "--disable-warnings", "-v", "tests"]
