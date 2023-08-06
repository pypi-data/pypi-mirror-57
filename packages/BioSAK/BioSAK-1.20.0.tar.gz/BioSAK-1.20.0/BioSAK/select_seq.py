#!/usr/bin/env python
from __future__ import division
import os
import argparse
from Bio import SeqIO
from BioSAK.global_functions import time_format
from BioSAK.global_functions import sep_path_basename_ext


select_seq_usage = '''
=================== select_seq example commands ===================

# Extract sequences with provided id in seq_id.txt
BioSAK select_seq -seq ctg.fasta -id seq_id.txt -option 1

# Extract sequences except those in seq_id.txt
BioSAK select_seq -seq ctg.fasta -id seq_id.txt -option 0

# seq_id.txt file format: one id per line

===================================================================
'''

def select_seq(args):

    # read in argument
    seq_file = args['seq']
    id_file = args['id']
    select_option = args['option']

    # define output file name
    seq_file_path, seq_file_basename, seq_file_extension = sep_path_basename_ext(seq_file)
    output_file = '%s/%s_option%s%s' % (seq_file_path, seq_file_basename, select_option, seq_file_extension)

    # get provided id list
    seq_id_list = []
    for seq_id in open(id_file):
        seq_id_list.append(seq_id.strip())

    # extract sequences
    output_file_handle = open(output_file, 'w')
    for seq in SeqIO.parse(seq_file, 'fasta'):
        seq_id = seq.id

        if select_option == 1:
            if seq_id in seq_id_list:
                SeqIO.write(seq, output_file_handle, 'fasta')

        if select_option == 0:
            if seq_id not in seq_id_list:
                SeqIO.write(seq, output_file_handle, 'fasta')

    output_file_handle.close()

    print('Extracted sequences exported to %s' % output_file)


if __name__ == '__main__':

    # initialize the options parser
    parser = argparse.ArgumentParser()

    # arguments for select_seq
    parser.add_argument('-seq',       required=True,            help='sequence file')
    parser.add_argument('-id',        required=True,            help='sequence id file, one id per line')
    parser.add_argument('-option',    required=True, type=int,  help='select option')

    args = vars(parser.parse_args())
    select_seq(args)
