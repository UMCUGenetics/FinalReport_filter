# FinalReport_filter
Software to filter Illumina Genomestudio FinalReport files

### Make virtual python enviroment
```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
deactivate
```

### Make Windows executable 
# Run pyinstaller to convert .py to Windows executable (.exe). Note: this must be done a Windows machine.
# Pyinstaller was run on the SNP-array_data_cruncher server using python v3.7.9 (32bit)
# https://www.python.org/ftp/python/3.7.9/python-3.7.9.exe
```bash
python
pip install pyinstaller
pyinstaller --onefile slice_snparray.py
```
## Executable can be found in folder dist
