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


## Email to Professor Kılıç

---

**To:** Prof. Dr. Kılıç
**Subject:** QC Results for Barcode77 Sequencing Data

Dear Professor Kılıç,

I have completed the quality control analysis of the sequencing data you provided (Barcode77). I ran an automated QC pipeline on the raw data. This pipeline checked the quality of each read and generated visual summaries to aid interpretation.

The sequencing was performed using Oxford Nanopore technology. The dataset contains 81,011 reads with a total of approximately 84 million base pairs.

Graphs and statistical summaries show that the majority of reads fall between 200–2,000 bp with a median of 547 bp, which is suitable for alignment. The distribution is right-skewed, with a small number of exceptionally long reads (maximum: 686,155 bp) which is not unusual for Nanopore sequencing.

The read length N50 is 1,761 bp, which is below the typical range for high-quality Nanopore runs. If genome assembly be considered in the future, quality filtering will likely improve this value significantly.

A symmetric distribution centered around 53% was observed, which is within the expected biological range.

According to the NanoStat report and as it can be seen in the Quality Distribution Graph, more than half of the reads fall below the Q10 threshold. Only 74 reads (0.1%) exceed the Q20 standard. The median read quality is Q9.85.

While the read lengths are suitable for alignment, given the low quality scores, applying a quality filtering step by removing reads below Q10 would be beneficial before proceeding to alignment. I recommend applying quality filtering first, then proceeding with alignment to a reference genome.

Best regards,
Şüheda Almina Dadak
