# PDF to CSV 

Create a single CSV by extracting (multi-page) table from input PDF.

## Quickstart

Tested on Ubuntu 22.04.4 LTS (jammy) with Python 3.10.12 virtualenv

```sh
sudo apt install ghostscript python3-tk ffmpeg libsm6 libxext6 virtualenv
virtualenv venv
source venv/bin/activate
pip install ghostscript camelot-py
python ./pdf2csv.py <input-file.pdf> [output-file.csv]
deactivate
```

## Notes

Uses camelot-py to extract tables from PDF, this relies on ghostscript and
tkinter which rely on a few other dependencies.
