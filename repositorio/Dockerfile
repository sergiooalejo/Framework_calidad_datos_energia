FROM python:3.14-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    STREAMLIT_SERVER_HEADLESS=true \
    STREAMLIT_BROWSER_GATHER_USAGE_STATS=false

WORKDIR /app

COPY Environment/requirements-streamlit.txt Environment/requirements-streamlit.txt
RUN python -m pip install --no-cache-dir -r Environment/requirements-streamlit.txt

COPY pyproject.toml README.md ./
COPY Code ./Code
RUN python -m pip install --no-cache-dir -e .

COPY Outputs ./Outputs
COPY app_streamlit.py pipeline.py ./
COPY .streamlit ./.streamlit

EXPOSE 8501
CMD ["streamlit", "run", "app_streamlit.py", "--server.address=0.0.0.0", "--server.port=8501"]

