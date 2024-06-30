# List all non-standard packages to be imported by your 
# script here (only missing packages will be installed)
from ayx import Package
#Package.installPackages(['pandas','numpy'])


#################################
from ayx import Alteryx
import pandas as pd
import csv

AlteryxDF=Alteryx.read("#1")


def get_delimiter(file_path: str) -&gt; str:
    with open(file_path, 'r') as csvfile:
        delimiter = str(csv.Sniffer().sniff(csvfile.read()).delimiter)
        return delimiter

AlteryxDF = AlteryxDF.reset_index()  # make sure indexes pair with number of rows

delimiter=[]

i=0
DFlength=len(AlteryxDF)-1
while i &lt;= DFlength:
    delimiter.append(get_delimiter(AlteryxDF.loc[i,'Full Path']))
    i= i+1


AlteryxDF['delimiter']=delimiter

Alteryx.write(AlteryxDF,1)
