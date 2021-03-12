# behavior_annotator
behavior annotator with napari

## dependencies

`pip install "napari[all]" napari_video`

## how to use

1. Press 'F' key on the frame that a behavior starts to set the start flag.

2. Play the video until a behavior ends.

3. Press '1' or '2' key to put the annotations into array.

repeat 1-3, and when all the annotations are done, press '0' key to save the CSV.

other option keys:

- '3' key: show position of start flag

- '4' key: delete wrong start flag

- '5' key: print annotations array

## references
napari contributors (2019). napari: a multi-dimensional image viewer for python. doi:10.5281/zenodo.3555620

https://github.com/janclemenslab/napari-video
