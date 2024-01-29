import os
import re
from arcpy import env

# 26.01.2024
# ����������� ��-��� ������� ArcGIS
# ��������� jpg ����� �� ����� � ������� ��������� ������� ������� (����� � ������)
# ��������� �� ������. ���� ���� ���������, �� ������ ���������� �� ���.
# ����� ��� � ���������� �������� � LOG_AFS_load.txt
# ���� �� ��� �� ������ ��������� ��������� ��� ��� ����� ������������� ��������,
# �� ��������� ����������� ��� �� ���������� �������� � �������� ������ ��������� jpg

# USER_SETTING_1  ���� � ������ jpg
env.workspace = r'D:\data\afs\jpg\2023'

# USER_SETTING_2   ���� � �������� �������. ����� ���� ��� � ���������  gdb, ��� � � ������� ��
#afs_set_db = r'Database Connections\AFS2023.sde\AFS2023.DBO.AFS_2023'
afs_set_db = r'D:\data\afs\AFS_2023.gdb\orto_2023'


def read_previos_log(log_file):
    loaded_lst=[]
    if os.path.isfile(log_file):
        f = open(log_file, "r")
        for x in f:
            if re.findall('success', x):
                jpg = x.split('\t')[0]
                print(jpg+' was loaded in previos session')
                loaded_lst.append(jpg)
        f.close()
    return loaded_lst
    
    
os.chdir(env.workspace)
log_file  = r'D:\data\afs\_LOG_AFS_load.txt' 
loaded_lst = read_previos_log(log_file)

r_lst  = arcpy.ListRasters('*.jpg')
loaded = 0
not_loaded = 0
for rastr in r_lst:
    log = open(log_file, 'a')
    if rastr in loaded_lst:
        continue
    print(rastr+' will load')
    arcpy.RasterToGeodatabase_conversion(Input_Rasters=env.workspace+'\\'+rastr, Output_Geodatabase=afs_set_db, Configuration_Keyword="")
    loaded += 1
    log.write(rastr)
    log.write('\tsuccess\n')
    log.close()

env.workspace = afs_set_db
#itog_loaded  = arcpy.ListDatasets() 
#print('Total in DATASET: '+str(len(itog_loaded)))       
print('Total was loaded successfull: '+str(loaded))
print('Total was NOT loaded: '+str(not_loaded))
print('Finish')        