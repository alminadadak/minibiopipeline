import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import io
import os

def summary(df):
	
	print("\n===== STATISTICAL SUMMARY =====")
	
	for col in ['read_length', 'gc_content', 'quality_mean']:
		print(f"\n{col.upper()}:")
		print(f"mean	: {df[col].mean():.2f}")
		print(f"median	: {df[col].median():.2f}")
		print(f"min	: {df[col].min():.2f}")
		print(f"max	: {df[col].max():.2f}")
		print(f"std	: {df[col].std():.2f}")

	print("\n===== ADDITIONAL STATISTICS =====")
	
	total_bases = df['read_length'].sum()
	print(f"\nTotal base	: {total_bases:,} bp({total_bases/1e9:.2f} Gbp)")

	q20 = df[df['quality_mean'] >= 20]
	print(f"Q20+ Read	: {len(q20):,} / {len(df):,} ({len(q20)/len(df)*100:.1f}%)")

	lengths = sorted(df['read_length'].tolist(), reverse=True)
	cumsum = 0
	n50 = 0
	half = total_bases / 2
	for l in lengths:
		cumsum += l
		if cumsum >= half:
			n50 = l
			break
	print(f"N50          : {n50:,} bp")

	print("\n===== QUALITY THRESHOLDS =====")
	for threshold in [5, 10, 15, 20]:
		above = df[df['quality_mean'] >= threshold]
		print(f">Q{threshold:<2}: {len(above):>6,} / {len(df):,} ({len(above)/len(df)*100:.1f}%)")

	print("\n===== FILTERING IMPACT =====")
	below_q10 = df[df['quality_mean'] < 10]
	above_q10 = df[df['quality_mean'] >= 10]
	print(f"Q10 below - median length: {below_q10['read_length'].median():.0f} bp  ({len(below_q10):,} reads)")
	print(f"Q10 above - median length: {above_q10['read_length'].median():.0f} bp  ({len(above_q10):,} reads)")


def plotDistributions(df, output_dir):
	fig, axes = plt.subplots(2, 2, figsize=(14, 10))
	fig.suptitle('Barcode77 - Read Quality Control', fontsize=16)
    
	df_filtered = df[df['read_length'] < df['read_length'].quantile(0.99)]
    
    
	sns.histplot(df['read_length'], bins=50, ax=axes[0][0], color='steelblue')
	axes[0][0].set_title('Read Length Distribution (Full)')
	axes[0][0].set_xlabel('Read Length (bp)')
	axes[0][0].set_ylabel('Count')
    
    
	sns.histplot(df_filtered['read_length'], bins=50, ax=axes[0][1], color='steelblue')
	axes[0][1].set_title('Read Length Distribution (99th percentile)')
	axes[0][1].set_xlabel('Read Length (bp)')
	axes[0][1].set_ylabel('Count')
    
    
	sns.histplot(df['gc_content'], bins=50, ax=axes[1][0], color='seagreen')
	axes[1][0].set_title('GC Content Distribution')
	axes[1][0].set_xlabel('GC Content (%)')
	axes[1][0].set_ylabel('Count')
    
    
	sns.histplot(df['quality_mean'], bins=50, ax=axes[1][1], color='coral')
	axes[1][1].axvline(x=20, color='red', linestyle='--', linewidth=1.5, label='Q20 thereshold')
	axes[1][1].legend()
	axes[1][1].set_title('Mean Read Quality Distribution')
	axes[1][1].set_xlabel('Mean Quality Score (Phred)')
	axes[1][1].set_ylabel('Count')
    
	plt.tight_layout()
	plt.savefig(f"{output_dir}/qc_distributions.png", dpi=150)
	print(f"PLot saved: {output_dir}/qc_distributions.png")

if __name__ == '__main__':
	input_csv = sys.argv[1]
	output_dir = sys.argv[2]

	if not os.path.exists(input_csv):
		print(f"Error: CSV file not found: {input_csv}")
		sys.exit(1)

	df = pd.read_csv(input_csv)
	expected_cols = ['read_id', 'read_length', 'gc_content', 'quality_mean', 'quality_median']
	for col in expected_cols:
		if col not in df.columns:
			print(f"Error:Missing column: {col}")
			sys.exit(1)

	print(f"{len(df)} reads loaded.")

	buffer = io.StringIO()
	sys.stdout = buffer

	summary(df)

	sys.stdout = sys.__stdout__
	summary_text = buffer.getvalue()

	print(summary_text)

	with open(f"{output_dir}/summary_stats.txt", 'w') as f:
		f.write(summary_text)
	print(f"Statistics saved: {output_dir}/summary_stats.txt")

	plotDistributions(df, output_dir)

	print("\nAll Done!")



