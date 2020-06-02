import os
import io
import json
import numpy as np
import argparse

from os import listdir
from os.path import isfile, join
from detect import detectText, pandasRead

RESOURCES_PATH = "resources"
OUTPUT_PATH = 'output'


def save_as_table(output_file, df):
    df.to_excel(output_file + '.xlsx')


def save_as_plain_text(output_file, df):
    np.savetxt(output_file + '.txt', df.values, fmt='%s')


def main(args):
    files = [f for f in listdir(RESOURCES_PATH) if isfile(join(RESOURCES_PATH, f))]
    for file in files:
        texts = detectText(os.path.join(RESOURCES_PATH, file))
        output_file = os.path.join(OUTPUT_PATH, file.split('.')[0])
        df = pandasRead(texts)
        if args.table:
            save_as_table(output_file, df)
        if args.text:
            save_as_plain_text(output_file, df)


parser = argparse.ArgumentParser(description='Detecting text script')
parser.add_argument("--text", type=bool, const=True, nargs='?', default=True,
                    help="Saving in plain text format")
parser.add_argument("--table", type=bool, const=True, nargs='?', default=False,
                    help="Saving in table format")
args = parser.parse_args()

main(args)
