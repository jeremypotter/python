import os

DIRECTORY = "/Users/francispotter/DropBox/Camera Uploads"

for filename in os.listdir(DIRECTORY):
    print filename
    if not filename.startswith('.'):
        full_path = os.path.join(DIRECTORY,filename)
        print full_path
        if os.path.isfile(full_path):
            os.system('open "' + full_path + '"')
            raw_input()
        
