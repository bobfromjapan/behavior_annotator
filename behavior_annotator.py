import napari
from napari_video.napari_video import VideoReaderNP
import numpy as np
import yaml
import codecs
import pandas as pd

with codecs.open("config.yaml", "r", 'utf-8') as yml:
    config = yaml.load(yml, Loader=yaml.SafeLoader)

VIDEO_PATH = config["video_path"]
LABELS = config["labels"]

vr = VideoReaderNP(VIDEO_PATH)
annotations = np.array([LABELS[0]]*len(vr))

# global vars
flag_exist = False
flag_frame = 0

with napari.gui_qt():
    viewer = napari.Viewer()
    image_layer = viewer.add_image(vr, rgb=True)

    @viewer.bind_key('f')
    def set_start_flag(event=None):
        global flag_exist
        global flag_frame

        if flag_exist:
            print('flag already exist!!')
        else:
            flag_frame = image_layer._slice_indices[0]
            flag_exist = True
            print("start flag set to frame:", image_layer._slice_indices[0])

    @viewer.bind_key('1')
    def annotate_A(event=None):
        global flag_exist
        global flag_frame
        if flag_exist:
            if flag_frame > image_layer._slice_indices[0]:
                print("go to the later frame than the start flag.")
                show_globals()
            else:
                print(
                    flag_frame, "to", image_layer._slice_indices[0], "is annotated to ", LABELS[1])
                annotations[flag_frame:image_layer._slice_indices[0]] = LABELS[1]
                flag_exist = False
        else:
            print("need to set the start flag.")

    @viewer.bind_key('2')
    def annotate_B(event=None):
        global flag_exist
        global flag_frame
        if flag_exist:
            if flag_frame > image_layer._slice_indices[0]:
                print("go to the later frame than the start flag.")
                show_globals()
            else:
                print(
                    flag_frame, "to", image_layer._slice_indices[0], "is annotated to ", LABELS[2])
                annotations[flag_frame:image_layer._slice_indices[0]] = LABELS[2]
                flag_exist = False
        else:
            print("need to set the start flag.")

    @viewer.bind_key('3')
    def show_globals(event=None):
        global flag_frame
        global flag_exist
        print("flag:", flag_exist)
        print("pos:", flag_frame)

    @viewer.bind_key('4')
    def delete_flag(event=None):
        global flag_exist
        print("delete_flag!")
        flag_exist = False

    @viewer.bind_key('5')
    def check_label(event=None):
        print(annotations)

    @viewer.bind_key('0')
    def save_label(event=None):
        print("save!")
        pd.DataFrame(annotations).to_csv("annotation.csv")
