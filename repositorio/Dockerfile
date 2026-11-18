FROM python:3.14.0-slim
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    STREAMLIT_SERVER_HEADLESS=true \
    STREAMLIT_BROWSER_GATHER_USAGE_STATS=false
WORKDIR /app
COPY pyproject.toml poetry.lock README.md ./
COPY src ./src
RUN python -m pip install --no-cache-dir poetry==2.5.1 \
    && poetry config virtualenvs.create false \
    && poetry install --only main --no-interaction --no-ansi
COPY Code ./Code
COPY configs ./configs
COPY apps ./apps
COPY tests ./tests
COPY notebooks ./notebooks
COPY scripts ./scripts
COPY Data ./Data
COPY Docs ./Docs
COPY Environment ./Environment
COPY project.json ./project.json
COPY app_streamlit.py pipeline.py ./
COPY .streamlit ./.streamlit
EXPOSE 8501
CMD ["python", "-m", "streamlit", "run", "apps/streamlit_app.py", "--server.address=0.0.0.0", "--server.port=8501"]
