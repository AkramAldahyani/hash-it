# hash-it

A simple Python CLI tool that computes MD5, SHA-1, SHA-256, and SHA-512 hashes for any file.

## Usage

```bash
python main.py <file>
```

Defaults to `file.txt` if no argument is given.

## Example

```
$ python main.py file.txt
Hashes for: file.txt
--------------------------------------------------
MD5       : bcf86e5e12e37883f964902639aa0555
SHA-1     : 29e7c8f11e25585f4c79b08c79f43dce07f08213
SHA-256   : 8ca4855efd9c7af131706cf4779aebdb5f932465228432542fce9b8f85caf7a4
SHA-512   : 78b3586dc5b7bf5fde41efa68d3f14dd684d62b0325e38c85ff0396e2010e37c...
```

## Requirements

Python 3.9+ — no external dependencies.
