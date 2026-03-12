FROM python:3.12-slim

WORKDIR /pipeline

RUN pip install pandas matplotlib seaborn snakemake nanostat

COPY scripts/ ./scripts/

CMD ["snakemake", "--cores", "1"]
