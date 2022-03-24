import os 

# change '.md' to '_index.md'
for dir in os.listdir('.'):
    if os.path.isdir(dir):
        for file in os.listdir(dir):
            if '.md' in file:
                os.rename(os.path.join(dir,file), os.path.join(dir,'_index.md'))

# change hanzi to english name
from pypinyin import lazy_pinyin
for dir in os.listdir('.'):
    if os.path.isdir(dir):
        os.rename(dir, '_'.join(lazy_pinyin(dir.split('/')[-1])))

# change jpg name to "avatar.jpg", please ensure that the name of image don't contain "chinese characters"
import cv2
for dir in os.listdir('.'):
    if os.path.isdir(dir):
        for file in os.listdir(dir):
            if '.jpg' in file or '.jpeg' in file:
                os.rename(os.path.join(dir,file), os.path.join(dir,'avatar.jpg'))
                os.remove(os.path.join(dir,file))
            elif '.png' in file:
                img = cv2.imread(os.path.join(dir,file))
                cv2.imwrite(os.path.join(dir,'avatar.jpg'),img)
                os.remove(os.path.join(dir,file))