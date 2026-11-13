FROM python:3.14-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    STREAMLIT_SERVER_HEADLESS=true \
    STREAMLIT_BROWSER_GATHER_USAGE_STATS=false

WORKDIR /app

COPY pyproject.toml poetry.lock README.md ./
COPY Code ./Code
RUN python -m pip install --no-cache-dir poetry==2.4.1 \
    && poetry config virtualenvs.create false \
    && poetry install --only main --no-interaction --no-ansi

COPY Outputs ./Outputs
COPY app_streamlit.py pipeline.py ./
COPY .streamlit ./.streamlit

EXPOSE 8501
CMD ["streamlit", "run", "app_streamlit.py", "--server.address=0.0.0.0", "--server.port=8501"]

