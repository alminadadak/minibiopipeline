# Mini-Bioinformatics QC Pipeline

A reproducible quality control pipeline for long-read sequencing data(Oxford Nanopore), built with Snakemake and Docker.

## Requirements

- Docker
- Make

## Usage

### 1. Clone the repository
```bash
git clone https://github.com/alminadadak/minibiopipeline.git
cd minibiopipeline
```

### 2. Add your input file

Place your '.fastq.gz file in the 'data/' directory and update 'config.yaml':
```yaml
sample: "your_sample_name"
```

### 3. Build the Docker image
```bash
make build
```

### 4. Run the pipeline
```bash
make run
```

## Pipeline Steps

1. **NanoStat** — Quality control report specifically designed for long-read data
2. **read_stats.py** — Custom script calculating GC content, read length, and mean quality for each read. Results saved to `results/stats.csv`
3. **visualize.py** — Generates distribution plots and summary statistics. Results saved to `figures/`

## Output Fİles

| File | Description |
|------|-------------|
| `results/stats.csv` | Per-read statistics (GC content, length, quality) |
| `results/nanostat_report/NanoStats.txt` | NanoStat QC report |
| `figures/qc_distributions.png` | Distribution plots |
| `figures/summary_stats.txt` | Summary statistics |

## Run Tests
```bash
make test
```
