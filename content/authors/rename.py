import os 

# change '.md' to '_index.md'
for dir in os.listdir('.'):
    if os.path.isdir(dir):
        name = dir.split('_')
        if len(name)==3:
            newname = "".join(name[1:3])
            newname = newname+"-"+name[0]
            os.rename(dir, newname)
        elif len(name)==2:
            newname = name[1]+"-"+name[0]
            os.rename(dir, newname)