import random

def calculate_poss():
	#calculate the possibility for random kmer to be in a file
	for length in range(1,11):
		kmer =str(100/float((4**length))) + '%'
		print(kmer)
		print('The probability of getting random kmer for string length {} is {}'.format(length,kmer))

def kmer_process():
	#Make random kmer and process whether kmer is in the file or not using my own algorithm
	calculate_poss()
	kmer_list = generate_random_kmer()
	aligners = open_file()
	kmer_in_file = create_kmerlist(kmer_list,aligners)
	kmer_dict = create_dict(kmer_in_file)
	for kmer in kmer_dict.values():
		print(kmer)

def generate_random_kmer():
	kmer_list =[]
	for number in range(1,11):
		count = 0
		for kmers in range(5):
			count += 1
			random_kmer = ''
			for dna in range(number):
				if number == 1 and count == 5:
					break
				random_kmer += random.choice('ATCG')
			kmer_list.append(random_kmer)
	return kmer_list

def open_file():
	aligner_file = open('Zmay_chr_9-P-94283818.fa')
	aligners = aligner_file.readlines()
	aligner_file.close()
	return aligners

def create_kmerlist(kmer_list, aligners):
	#identifies whether kmer is in the aligners file, if it is, then put True next to it. If not in the file, put False next to it.
	kmer_in_file = []
	kmer_true = []
	for kmer_bool in kmer_list:
		for aligner in aligners:
			if kmer_bool in aligner:
				kmer_temp = []
				kmer_temp.append(kmer_bool)
				kmer_temp.append(True)
				kmer_in_file.append(kmer_temp)
				kmer_true.append(kmer_bool)
				break
	for kmer_bool in kmer_list:
		if kmer_bool not in kmer_true:
			kmer_temp = []
			kmer_temp.append(kmer_bool)
			kmer_temp.append(False)
			kmer_in_file.append(kmer_temp)
	for empty in kmer_in_file:
		if empty[0] == '':
			kmer_in_file.remove(empty)
	return kmer_in_file

def create_dict(kmer_in_file):
	#create dictionary to print out nicer
	blank_dict = {}
	for kmer_final in kmer_in_file:
		kmer_len =len(kmer_final[0])
		if kmer_len in blank_dict.keys():
			if kmer_final[1] == True:
				blank_dict[kmer_len].append( 'The kmer length ' + str(kmer_len)+ ', kmer ' + kmer_final[0] + ' is in a file')
			elif kmer_final[1] == False:
				blank_dict[kmer_len].append( ('The kmer length ' + str(kmer_len) +', kmer '+ kmer_final[0] + ' is not in a file'))
		else:
			if kmer_final[1] == True:
				blank_dict[kmer_len] =['The kmer length '  + str(kmer_len) + ', kmer ' + kmer_final[0] + ' is in a file']
			elif kmer_final[1] == False:
				blank_dict[kmer_len] =['The kmer length ' + str(kmer_len) + ', kmer ' + kmer_final[0] + ' is not in a file']
	return blank_dict

kmer_process()
