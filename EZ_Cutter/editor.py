import cv2
import pandas as pd
import EZ_Cutter.DVideo
import os

def subClip(video, output_video_path, start_time, end_time):
    fps = video.meta['fps']
    start_frame = int(start_time * fps)
    end_frame = int(end_time * fps)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (video.meta['width'], video.meta['height']))

    video.cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

    for frame_number in range(start_frame, end_frame + 1):
        ret, frame = video.cap.read()
        if not ret:
            break
        out.write(frame)

    out.release()

def get_xlsx2df(xlsx_path, sheet_name):
    df = pd.read_excel(xlsx_path, sheet_name)

    return df

def get_video_list(folder_path):    
    all_files = os.listdir(folder_path)

    extensions = ['.mp4', '.MP4']
    mp4_files = [f for f in all_files if any(f.endswith(ext) for ext in extensions)]
    
    return mp4_files

def processing_video_clipper(video:EZ_Cutter.DVideo, output_video_path, xlsx_path:str, Sheet_name:str,
                                target_activity='Locomotion'):
    
    df = get_xlsx2df(xlsx_path, Sheet_name)
    
    for idx, each_sample in df.iterrows():
        video_name = each_sample['video_name']
        start = each_sample['start']
        end = each_sample['end']
        activity = each_sample['activity']

        start_time = 3600 * start.hour + 60 * start.minute + start.second
        end_time = 3600 * end.hour + 60 * end.minute + end.second

        #print(f'[idx: {idx}, video: {video_name}, start: {start_time}, end: {end_time}, acitvity: {activity}]')

        if activity == target_activity:
            print(f'[idx: {idx}, video: {video_name}, start: {start_time}, end: {end_time}, acitvity: {activity}]')
            subClip(video, output_video_path + f'{idx  +2}.mp4', start_time, end_time)