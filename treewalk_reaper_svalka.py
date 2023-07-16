import os
import shutil

for root, dirs, files in os.walk('.', topdown=False): 

    x = root

    if root == '.':             
        x = "minimal_hardcore" 
        
    os.makedirs(f"/home/nick/tech/python/sort_reaper/output_project_dirs/{os.path.basename(x)}", exist_ok=True)

    for j in files:               
                           
        source = f"{root}/{j}"
        
        project_folder_dest = f"/home/nick/tech/python/sort_reaper/output_project_dirs/{os.path.basename(x)}/{j}"                    
                       
        shutil.copyfile(source, project_folder_dest)


    
