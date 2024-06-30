# 2024_AlteryxMacros
This a repo of Alteryx Macros which use Python and/or Shell commands to fill gaps which are not addressed by the core Designer product. YMMV.

Development was conducted on Alteryx 2021.4 with AMP disabled. If you use later versions (particuarly 2024.1) you may hit issues. Some macros may require installation of python packages either through CLI in your Alteryx Python VENV or via the install.packages Alteryx Python function. 

CSV_Sniffer is a macro which determines the delimiter on CSV/TSV/other text files. It returns the delimiter and filename - and can be used for downstream processing of files with unknown delimiters. The python script is replicated in the CSV_Sniffer.py file.
