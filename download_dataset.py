"""Download and verify TibSenCorpus ciphertext; no password is needed here."""

import argparse
import hashlib
import json
from pathlib import Path
import urllib.request

BASE = "https://raw.githubusercontent.com/cvNXE/TibSenCorpus/main/"


def sha256(path):
    result = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            result.update(block)
    return result.hexdigest()


def download(url, target):
    request = urllib.request.Request(url, headers={"User-Agent": "TibSenCorpus-downloader"})
    temporary = target.with_name(target.name + ".download")
    with urllib.request.urlopen(request, timeout=120) as response, temporary.open("wb") as stream:
        while block := response.read(1024 * 1024):
            stream.write(block)
    temporary.replace(target)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=Path("TibSenCorpus_download"))
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(BASE + "dataset_metadata.json", timeout=60) as response:
        metadata = json.load(response)
    parts = []
    for item in metadata["volumes"]:
        path = args.output_dir / Path(item["path"]).name
        if not path.exists() or sha256(path) != item["sha256"]:
            print("Downloading " + path.name, flush=True)
            download(BASE + item["path"], path)
        if path.stat().st_size != item["bytes"] or sha256(path) != item["sha256"]:
            raise SystemExit("Checksum mismatch: " + path.name)
        parts.append(path)
    archive = args.output_dir / metadata["archive"]
    if not archive.exists() or sha256(archive) != metadata["archive_sha256"]:
        temporary = archive.with_name(archive.name + ".download")
        with temporary.open("wb") as output:
            for part in parts:
                with part.open("rb") as source:
                    while block := source.read(1024 * 1024):
                        output.write(block)
        if sha256(temporary) != metadata["archive_sha256"]:
            raise SystemExit("Joined archive checksum mismatch.")
        temporary.replace(archive)
    print("Verified encrypted archive: " + str(archive.resolve()))
    print("Request the extraction password from cvlina@mail.nwpu.edu.cn.")


if __name__ == "__main__":
    main()
