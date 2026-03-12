run:
	docker run --rm \
		-v $(PWD)/data:/pipeline/data \
		-v $(PWD)/results:/pipeline/results \
		-v $(PWD)/figures:/pipeline/figures \
		-v $(PWD)/Snakefile:/pipeline/Snakefile \
		-v $(PWD)/config.yaml:/pipeline/config.yaml \
		biopipeline

build:
	docker build -t biopipeline .

clean:
	rm -f results/stats.csv figures/*

test:
	python3 scripts/test_scripts.py
