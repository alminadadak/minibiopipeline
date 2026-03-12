import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '.'))

from read_stats import gcContent, qualityMean, qualityMedian
import math

def test_gc_content():
	assert gcContent("ATGC") == 50.0, "ATGC should be 50% GC"
	assert gcContent("GGGG") == 100.0, "GGGG should be 100% GC"
	assert gcContent("AAAA") == 0.0, "AAAA should be 0% GC"
	assert gcContent("atgc") == 50.0, "Lowercase should also work out"
	print("gcContent tests passed")

def test_quality_mean():
	quality = "IIII" 
	result = qualityMean(quality)
	assert abs(result - 40.0) < 0.01, f"IIII should be Q40, got {result}"
	print("qualityMean tests passed")

def test_quality_median():
	quality = "IIII" 
	result = qualityMedian(quality)
	assert result == 40.0, f"IIII median should be 40,got {result}"
	print("qualityMedian tests passed")

def test_edge_cases():
	try:
		gcContent("")
	except ZeroDivisionError:
		print("Empty string raised ZeroDivisionError")

	assert gcContent("NNNN") == 0.0, "Should be 0% GC"

	assert qualityMedian("I") == 40.0, "Single char median should be 40"

	print("Edge case tests passed")

if __name__ == '__main__':
	test_gc_content()
	test_quality_mean()
	test_quality_median()
	test_edge_cases()
	print("\nAll tests passed!")

