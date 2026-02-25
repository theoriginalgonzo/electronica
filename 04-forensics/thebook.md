# The book

## Prepping the container:

singularity build $CONTAINERS/volatility3.sif docker://sk4la/volatility3
alias vol3="singularity exec $CONTAINERS/volatility3.sif volatility3"

## Opening the file

```cd ~/Downloads```

If it’s compressed:

```xz -d memdump.mem.xz```

Verify:

```ls -lh memdump.mem```
```file memdump.mem```

You should see:

Size ≈ 1GB

Windows Event Trace Log (this is expected for this challenge)


You do NOT “start” the container like Docker.

Instead, you run commands through it using your alias:

```vol3 -f memdump.mem windows.info.Info```

If your memory file is in another directory, use full path:

```vol3 -f /home/hanzipepper/Downloads/memdump.mem windows.info.Info```


## The question was: What OS was this dump taken from?

Look for:

Major/Minor version

Build number

OS name

## Get Computer Name & Username

Run:

```vol3 -f memdump.mem windows.envars.Envars```

Look for:

COMPUTERNAME 

USERNAME 

Paths like C:\Users\username\

## Find the Suspicious File

Scan all file objects:

```vol3 -f memdump.mem windows.filescan.FileScan```

Now filter for the username you found:

```vol3 -f memdump.mem windows.filescan.FileScan | grep <username>```

You are looking for:

A suspicious document

Copy the virtual address (starts with 0xe000...)

## Full filepath of file of interest

## Extract the File

Create output folder:

```mkdir output```

Now dump the file:

```vol3 -f memdump.mem -o ./output windows.dumpfiles.DumpFiles --virtaddr 0xe000XXXX```

Replace 0xe000XXXX with the actual address.

Two files will appear in output/.

## Open the SQLite Database

The dumped file is a SQLite DB.

Check it with:

```file output/*```

Open it with:

```sqlite3 output/<filename>```

Inside sqlite:

```.tables```
```SELECT * FROM users;```

## Find the real name of "cloud".


## Real name of cloud

Exit sqlite with:

```.exit```

## Extract Password Hashes

Run:

```vol3 -f memdump.mem windows.registry.hashdump.Hashdump```

If you get a Crypto error:

Inside your host machine (not container):

```pip3 install pycryptodome```

Then re-run hashdump.

You’ll see NTLM hashes like:

username:RID:LMHASH:NTHASH:::

## Copy the NT hash.

Crack the Password

You can use:

John the Ripper

Hashcat

For John:

```john --format=NT hash.txt```

Password

If you STILL get the “Unsatisfied requirement kernel.layer_name” error inside Singularity, then we debug that separately — but this container usually works correctly.
