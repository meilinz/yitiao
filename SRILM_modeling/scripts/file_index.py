
import glob
import os
out_filename = "../filelists/file_index"
if os.path.exists(out_filename):
    os.remove(out_filename)
read_files = glob.glob("../filelists/filelist_0*")
with open(out_filename, "w") as outfile:
    for filename in read_files:
        with open(filename) as infile:
            for line in infile:
                small_file = line.strip()
                small_file_short = (line.split('.')[-3]).split('/')[-1]
                number_of_lines = sum(1 for line in open(small_file))
                outfile.write('{},{},{},{}\n'.format(line.strip(), small_file_short, filename, number_of_lines))

with open("../filelists/file_index", "r") as file_in:
	filedata = file_in.read()

filedata = filedata.replace('../filelists/filelist', 'file')

with open("../filelists/file_index", "w") as file_out:
	file_out.write(filedata)