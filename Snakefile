configfile: "config.yaml"
SAMPLE = config["sample"]

rule all:
	input:
		"results/stats.csv",
		"figures/qc_distributions.png",
		"figures/summary_stats.txt",
		"results/nanostat_report/NanoStats.txt"

rule run_stats:
	input: 
		f"data/{SAMPLE}.fastq.gz"
	output:
		"results/stats.csv"
	shell:
		"python3 scripts/read_stats.py {input} {output}"

rule run_visualization:
	input:
		"results/stats.csv"
	output:
		"figures/qc_distributions.png",
		"figures/summary_stats.txt"
	shell:
		"python3 scripts/visualize.py {input} figures"

rule run_nanostat:
	input:
		f"data/{SAMPLE}.fastq.gz"
	output:
		"results/nanostat_report/NanoStats.txt"
	shell:
		"NanoStat --fastq {input} --outdir results/nanostat_report --name NanoStats.txt"

