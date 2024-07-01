#################################
# List all non-standard packages to be imported by your 
# script here (only missing packages will be installed)
from ayx import Package
#Package.installPackages(['pandas','numpy'])


#################################
from ayx import Alteryx
import pandas as pd
import zipfile


AlteryxDF=Alteryx.read("#1")


def get_zipfiles(file_path: str):
    zip = zipfile.ZipFile(file_path)
    # list available files in the container
    listofFiles=zip.namelist()
    zipDict=[]
    for file in listofFiles:
        fileDict={
            "Full Path": file_path,
            "Compressed File": file
        }
        zipDict.append(fileDict)
    newAlteryxDF=pd.DataFrame(zipDict)
    Alteryx.write(newAlteryxDF,1)
    return zipDict
    
    
AlteryxDF = AlteryxDF.reset_index()  # make sure indexes pair with number of rows
full_list=[]
i=0
DFlength=len(AlteryxDF)-1
while i <= DFlength:
    full_list.append(get_zipfiles(AlteryxDF.loc[i,'Full Path']))
    i= i+1




#################################
