# merge csv files and add the file name as a new column to the final csv
import glob, os

out_filename = "../classifier_noun_pairs_sogoucs2008.csv"
if os.path.exists(out_filename):
    os.remove(out_filename)

read_files = glob.glob("../classifier_noun_pairs/*.csv")
with open(out_filename, "w") as outfile:
    for filename in read_files:
        with open(filename) as infile:
            for line in infile:
            	outfile.write('{},{}\n'.format(line.strip(), '.'.join(filename.split('/')[-1:])))
                #outfile.write('{},{}\n'.format(line.strip(), '.'.join(filename.split('.')[4:])))
                # 4 is used to keep the filename short (e.g., 1580805.csv)
                # delete [4:] will give full path

print("DONE!")