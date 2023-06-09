from itertools import product
import os
import sys
import pandas
import numpy

filename = sys.argv[1]
k=int(sys.argv[2])
base = 'ATCG'
kmers = list(product(base, repeat=k))

def sample_formulation(seq,k,kmers):
    for i in range(len(kmers)):
        kmers[i] = ''.join(kmers[i])

    kmer_in_seq = []
    for i in range(len(seq)-k+1):
        kmer = seq[i:i+k]
        kmer_in_seq.append(kmer)

    count = []
    for i in kmers: 
        count.append(kmer_in_seq.count(i))
        
    feature_vector = [c/len(kmer_in_seq) for c in count]
    return feature_vector

with open(filename) as f:
	lines = f.readlines()
seq = []
for i in range(len(lines)):
	if i % 2 == 1:
		seq.append(lines[i].strip().upper())

feature_vectors = []
for j in seq:
	feature_vectors.append(sample_formulation(j,k,kmers))
	
filename = filename.split('.')
feature_vectors = pandas.DataFrame(feature_vectors)
feature_vectors.to_csv(filename[0]+"_"+str(k)+'mer'+'.csv', index=False, header = False)