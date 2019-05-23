import os
import threading
import argparse

NUM_THREADS = 100
#VIDEO_ROOT = 'drive/Machine_Learning-Deep_Learning/PROGETTO_MACHINE_LEARNING/sample_data/jumping' #'20bn-something-something-v2'         # Downloaded webm videos
#FRAME_ROOT = 'drive/Machine_Learning-Deep_Learning/PROGETTO_MACHINE_LEARNING/sample_data/jumping' #'20bn-something-something-v2-frames'  # Directory for extracted frames


parser = argparse.ArgumentParser(description="extract frames from video")
parser.add_argument('--video_folder', type=str, default='gdrive/My Drive/ML-Progetto/dataset/sport/sport-video/')
parser.add_argument('--frame_folder', type=str, default='gdrive/My Drive/ML-Progetto/dataset/sport/frame-video/')

args = parser.parse_args()

VIDEO_ROOT = '{}'.format(args.video_folder)
FRAME_ROOT = '{}'.format(args.frame_folder)

def split(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]


def extract(video, tmpl='%06d.jpg'):
    #if not os.path.exists(os.path.join(FRAME_ROOT,video[:-4], tmpl):
        os.system(f'ffmpeg -i "{VIDEO_ROOT}"/{video} -vf scale=256:256'
                    f' "{FRAME_ROOT}"/{video[:-4]}/{tmpl}')	# 5 al posto di 4


def target(video_list):
    for video in video_list:
        if not (os.path.exists(os.path.join(FRAME_ROOT, video[:-4]))):
            os.makedirs(os.path.join(FRAME_ROOT, video[:-4]))	# 5 al posto di 4
            extract(video)


if not os.path.exists(VIDEO_ROOT):
    raise ValueError('Please download videos and set VIDEO_ROOT variable.')
if not os.path.exists(FRAME_ROOT):
    os.makedirs(FRAME_ROOT)

video_list = os.listdir(VIDEO_ROOT)
splits = list(split(video_list, NUM_THREADS))

threads = []
for i, split in enumerate(splits):
    thread = threading.Thread(target=target, args=(split,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
