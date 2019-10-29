

import os
import re
import xlrd

loc = ("cmu-mocap-index-spreadsheet.xls") 

wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
  
for i in range(sheet.nrows):
    match = re.search(r'^([0-9]+)_([0-9]+)$', sheet.cell_value(i, 0))
    if (match == None):
        print("no number found")
    else:
        folder_name = match.group(1)
        file_name = match.group(0)
        raw_animation_name = str(sheet.cell_value(i, 1))
        fixed_animation_name = re.sub(r'[^a-zA-Z0-9]', '_', raw_animation_name)
        print(match.group(0) + " " + match.group(1) + " " + match.group(2) + " " + fixed_animation_name)
        full_file_name = folder_name + "/" + file_name + ".fbx"
        new_file_name = folder_name + "/" + file_name + "_" + fixed_animation_name + ".fbx"
        if os.path.isfile(full_file_name):
            print("found file " + full_file_name + "; rename to: " + new_file_name)
            os.rename(full_file_name, new_file_name)
        else:
            print("could not find file " + full_file_name)