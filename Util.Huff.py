from huff import CodHuff
import sys

path = "sample.txt"

h = CodHuff(path)

output_path = h.compress()
print("Compressed file path: " + output_path)
