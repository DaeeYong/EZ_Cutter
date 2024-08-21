'''
author : DaeYong Kim
date : 2024-08-13
last_modified : 2024-08-21
'''

import cv2
from EZ_Cutter.DVideo import DVideo
from EZ_Cutter.Editor import subClip, get_xlsx2df, get_video_list
import pandas as pd

xlsx_path = '/Users/ivory/Documents/github/EZ_Cutter/clip_label/label.xlsx'
output_video_path = '/Users/ivory/Documents/github/EZ_Cutter/result/'
video_path = '/Volumes/SAMSUNG/pp01_70/pp1/'

df = get_xlsx2df(xlsx_path, 'Sheet1')

for idx, each_sample in df.iterrows():
        video_name = each_sample['video_name']
        start = each_sample['start']
        end = each_sample['end']
        activity = each_sample['activity']

        start_time = 3600 * start.hour + 60 * start.minute + start.second
        end_time = 3600 * end.hour + 60 * end.minute + end.second

        print(f'[idx: {idx}, video: {video_name}, start: {start_time}, end: {end_time}, acitvity: {activity}]')

        if activity == 'Locomotion':
            print('name: ',video_path + video_name)
            video = DVideo(video_path + video_name)
            subClip(video, output_video_path + video_name[:-4] + '_'+f'{idx  +2}.mp4', start_time, end_time)