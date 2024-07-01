# 2024_AlteryxMacros
This a repo of Alteryx Macros which use Python and/or Shell commands to fill gaps which are not addressed by the core Designer product. YMMV.

Development was conducted on Alteryx 2021.4 with AMP disabled. If you use later versions (particuarly 2024.1) you may hit issues. Some macros may require installation of python packages either through CLI in your Alteryx Python VENV or via the install.packages Alteryx Python function. 

CSV_Sniffer is a macro which determines the delimiter on CSV/TSV/other text files. It returns the delimiter and filename - and can be used for downstream processing of files with unknown delimiters. The python script is replicated in the CSV_Sniffer.py file.

zipfile_extractor returns the full list of files in a compressed archive. It is a standard macro and returns the path inside the .zip file for each compressed file.

Excel Template Sheet Copier is designed for use in conjunction with Blob based templates or other pre-formated Excle sheets. It requires:
1) Path to an Excel file.
2) Template Sheet (the sheet with the original formatting you are looking to replicate)
3) New Sheet names (the copies of the original template sheet)
4) openpyxl - it will try to install this if you do not have openpyxl - but if Python cannot import openpyxl you will not be able to run this. I recommend running in admin-mode if you have never installed openpyxl in your Python venv.

WARNING - I saw some weird behavior where it created duplicate sheets (a blank sheet for every correct sheet) and have added code to remove the blanksheet (which uses the f'{newCopy}1' syntax. IF YOU HAVE A SHEET IN YOUR EXCEL FILE WITH THE SAME NAMING CONVENTION AS YOUR NEWSHEET +1 - IT WILL DELETE IT.
