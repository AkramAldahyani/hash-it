import argparse
import hashlib
import sys


def hash_file(file_path):
    hashes = {
        "MD5": hashlib.md5(),
        "SHA-1": hashlib.sha1(),
        "SHA-256": hashlib.sha256(),
        "SHA-512": hashlib.sha512(),
    }

    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                for h in hashes.values():
                    h.update(chunk)
    except FileNotFoundError:
        print(f"Error: file not found: {file_path}", file=sys.stderr)
        sys.exit(1)
    except OSError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    print(f"Hashes for: {file_path}\n" + "-" * 50)
    for name, h in hashes.items():
        print(f"{name:<10}: {h.hexdigest()}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Compute common hashes for a file.")
    parser.add_argument("file", nargs="?", default="file.txt",
                        help="path to the file (default: file.txt)")
    args = parser.parse_args()
    hash_file(args.file)
