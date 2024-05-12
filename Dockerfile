FROM python:alpine AS install

WORKDIR /server
COPY requirements.txt .
RUN pip install --no-cache-dir --requirement=requirements.txt
COPY src/*.py .
COPY src/routes/*.py routes/

FROM install AS database

COPY data.json .
RUN python init.py

FROM install AS prod

COPY --from=database /server/database.db .

EXPOSE 8000
ENTRYPOINT ["uvicorn", "main:app"]
CMD ["--host=0.0.0.0"]
