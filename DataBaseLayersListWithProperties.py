import io
from arcpy import env

# Под кодключению к БД выдаёт список наборов данных, список пространсвенных данных в этих наборах
# Для каждого набора данных считает количество объектов и указывает тип геометрии


# USER_SETTING_1. Путь к подключению
wrk_1 = env.workspace = r'Database Connections\genplan.sde'

# USER_SETTING_2. Куда сохранить лог (результат)
result_text_file  = 'D:\wrk_genplan\LayersExists2.txt'

lst = arcpy.ListDatasets()
idx = 0
for i in lst:
    f = io.open(result_text_file, "a", encoding="1251")
    print(i)
    f.write(u'\n')
    f.write(unicode(i))
    f.write(u'\n')
    
    wrk_2 = env.workspace = lst[idx]
    print(env.workspace)
    lyr_lst = arcpy.ListFeatureClasses()
    for lyr in lyr_lst:
        count_obj = None
        count_obj = arcpy.GetCount_management(lyr)
        desc = arcpy.Describe(lyr)
        geom = str(desc.shapeType)
        f.write(unicode(lyr))
        f.write(u'\t')
        f.write(unicode(count_obj))
        f.write(u'\t')
        f.write(unicode(geom))
        f.write(u'\n')

    f.close()   
    idx +=1
    env.workspace = wrk_1