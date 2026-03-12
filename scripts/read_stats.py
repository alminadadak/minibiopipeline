import gzip
import csv
import sys
import math
import os

def gcContent(sequence):
	sequence = sequence.upper()
	gc = sequence.count('G') + sequence.count('C')
	return (gc / len(sequence)) * 100

def qualityMean(quality):
	scores = [ord(char) - 33 for char in quality]
	error_rates = [10 ** (-q / 10) for q in scores]
	mean_error = sum(error_rates) / len(error_rates)
	return -10 * math.log10(mean_error)

def qualityMedian(quality):
	scores = sorted([ord(char) - 33 for char in quality])
	n = len(scores)
	if n % 2 == 0:
		return (scores[n//2 - 1] + scores[n//2]) / 2
	return scores[n//2]

def parseFastq(input_file, output_file):
	if not os.path.exists(input_file):
		print(f"Error: Input file not found: {input_file}")
		sys.exit(1)

	output_dir = os.path.dirname(output_file)
	if output_dir and not os.path.exists(output_dir):
		os.makedirs(output_dir)
		print(f"Created output directory: {output_dir}")

	with gzip.open(input_file, 'rt') as f, open(output_file, 'w', newline='') as out:
		writer = csv.writer(out)
		writer.writerow(['read_id', 'read_length', 'gc_content', 'quality_mean', 'quality_median'])
		
		skipped = 0
		while True:
			header = f.readline().strip()
			sequence = f.readline().strip()
			plus = f.readline().strip()
			quality = f.readline().strip()

			if not header:
				break

			if not sequence or len(sequence) == 0:
				skipped += 1
				continue
			
			read_id = header[1:].split()[0]
			length = len(sequence)
			gc = gcContent(sequence)
			qual = qualityMean(quality)
			median_qual = qualityMedian(quality)

			writer.writerow([read_id, length, round(gc, 6), round(qual, 2), round(median_qual, 2)])
	if skipped > 0:
		print("f{skipped} faulty read skipped")

if __name__ == '__main__':
	input_file = sys.argv[1]
	output_file = sys.argv[2]
	parseFastq(input_file, output_file)
	print(f"THE PROCESS IS COMPLETE. HERE ARE THE RESULTS: {output_file}")
