import cv2

def show_video_meta(video_path:str):

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: 비디오 파일을 열 수 없습니다.")
    else:
        #total_frame_size
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        #fps
        fps = cap.get(cv2.CAP_PROP_FPS)
        #length of video(sec)
        duration = frame_count / fps
        #width x height
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        #codec info
        codec = int(cap.get(cv2.CAP_PROP_FOURCC))
        codec_str = (
            chr((codec & 0xFF)) +
            chr((codec & 0xFF00) >> 8) +
            chr((codec & 0xFF0000) >> 16) +
            chr((codec & 0xFF000000) >> 24)
        )

        #meta data
        print("total frame:", frame_count)
        print("FPS:", fps)
        print("Length of Video:", duration)
        print("video size: {}x{}".format(width, height))
        print("codec:", codec_str)

    cap.release()