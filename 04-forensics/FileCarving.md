File carving is a digital forensic technique used to
get information out of files that have been combined
with the goal of hiding information.

First you will want to identify what kind of file you
are working with. Using the `file <file name>` command
on an image file will show you the file type, along 
with resolution, color data, and other things.

Once you have identified the file type, use a program
like Binwalk. Binwalk will preform file carving
techniques like reading magic bytes to tell where one
file begins and another ends. Once the files are found,
they can then be taken apart again and read individually

To start use `binwalk <file name>`. This will show you
the flies that are inside of your composite file which
can then be extracted using `binwalk --extract <file 
name>`. The extracted files will be placed in a new
directory.

Using binwalk like this you should be able to answer
questions like these ones about the file `green_file
.bin`.

1. This file initially looks like something green, what's the file format of this green file?

Using `file green_file.bin` we can see that this binary
file contains a png. We also rename the file to `green_
file.png` for the next command.

2. How many files can be extracted from the binary blob?

After using `binwalk green_file.png` we can see 6 files
are inside of the green file. 5 pngs and 1 gzip.

3. What is the hidden flag in the file

Using `binwalk --extract --dd “png:png” green_file.png`
we can extract all the files from the png. The files are
extracted to a tar archive inside the directory `_green
_file.png.extracted`. Use `tar xvf CAB` to unpack the
archive so we can access the `flags` directory and read
`flags.txt` to get the answer of "SKY-RWCI-4291".
