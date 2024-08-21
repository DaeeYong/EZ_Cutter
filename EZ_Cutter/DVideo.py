import cv2

class DVideo:
    def __init__(self, video_path):
        self.cap = cv2.VideoCapture(video_path)
        self.meta = {'total_frame': 0, 'fps' : 0, 'duration' : 0, 'width' : 0, 'height' : 0, 'codec' : 0, 'codec_str': 0}
        self._get_meta()

    def _get_meta(self):
        frame_cnt = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        print('frame_cnt: ',frame_cnt)
        #fps
        fps = self.cap.get(cv2.CAP_PROP_FPS)
        #length of video(sec)
        duration = round(frame_cnt / fps)
        #width x height
        width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        #codec info
        codec = int(self.cap.get(cv2.CAP_PROP_FOURCC))
        codec_str = (
            chr((codec & 0xFF)) +
            chr((codec & 0xFF00) >> 8) +
            chr((codec & 0xFF0000) >> 16) +
            chr((codec & 0xFF000000) >> 24)
        )
        
        self.meta['total_frame'] = frame_cnt
        self.meta['fps'] = fps
        self.meta['duration'] = duration
        self.meta['width'] = width
        self.meta['height'] = height
        self.meta['codec'] = codec
        self.meta['codec_str'] = codec_str