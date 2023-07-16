import os
import shutil

for root, dirs, files in os.walk('.', topdown=False):    

    for j in files:
        
        x = root

        if root == '.':             
            x = "minimal_hardcore"          
                            
        source = f"{root}/{j}"

        os.makedirs(f"/home/nick/tech/python/sort_reaper/output_project_dirs/{os.path.basename(x)}", exist_ok=True)

        project_folder_dest = f"/home/nick/tech/python/sort_reaper/output_project_dirs/{os.path.basename(x)}/{j}"                    
                       
        shutil.copyfile(source, project_folder_dest)


    
