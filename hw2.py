import random

for length in range(1,11):
	kmer =str(100/float((4**length))) + '%'
	print(kmer)
	print('The probability of getting random kmer for string length {} is {}'.format(length,kmer))
kmer_list =[]
for number in range(5):
	random_number = random.randint(1,10)
	random_kmer = ''
	for dna in range(random_number):
		random_kmer += random.choice('ATCG')
	kmer_list.append(random_kmer)
print(kmer_list)
aligner_file = open('Zmay_chr_9-P-94283818.fa')
aligners = str(aligner_file.readlines())
kmer_in_file = []
for kmer_bool in kmer_list:
	kmer_in_file.append(aligners.find(kmer_bool))
print(kmer_in_file)
