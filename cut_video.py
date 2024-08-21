'''
author : DaeYong Kim
date : 2024-08-13
last_modified : 2024-08-19
'''

import cv2
from EZ_Cutter import DVideo

video_path = 'C:/Users/admin/Documents/github/EZ_Cutter/video/gait1_front.mp4'

video = DVideo(video_path)

print('*** meta info ***')
print(video.meta)
