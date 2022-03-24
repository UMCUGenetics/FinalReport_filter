#! /usr/bin/env python3

import argparse
import glob


def slice_file(input_file, chromosomes):
    write_file = open("{}_sliced.txt".format(input_file[:-4]), "w")
    input_lines = open(input_file, "r")
    chrom_list = chromosomes.split(",")

    """ Write all lines until Data section """
    line = input_lines.readline()
    while line.rstrip() != '[Data]':
        write_file.write(line)
        line = input_lines.readline()
    write_file.write(line)  # Print [Data] line

    """ Index header line for chromosome column, and write header"""
    header = input_lines.readline()
    chromosome_index = header.split("\t").index("Chr")
    write_file.write(header)

    """ Write all variant lines are on chromosomes of interest"""
    for line in input_lines:
        splitline = line.rstrip().split("\t")
        if splitline[chromosome_index] in chrom_list:
            write_file.write(line)

    write_file.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_file', help='Full path to input file (Final report)')
    parser.add_argument(
        '--chromosomes',
        default="13,18,21,X,Y,XY",
        help='comma seperated chromosomes to be kept in file. (default= 13,18,21,X,Y,XY)'
    )
    parser.set_defaults(func=slice_file)
    args = parser.parse_args()
    if not args.input_file:
        for input_file in glob.glob("*FinalReport.txt"):
            args.func(input_file, args.chromosomes)
    else:
        args.func(args.input_file, args.chromosomes)
