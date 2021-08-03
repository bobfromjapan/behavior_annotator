# behavior_annotator
behavior annotator with napari

The simple tool for animal behavior annotation to create a CSV file that looks like this:

```
frame, behavior
1, behaviorA
2, behaviorA
3, behaviorA
4, behaviorA
..., ...
98, behaviorA
99, behaviorA
100, behaviorB
101, behaviorB
102, behaviorB
..., ...
```

![image](https://user-images.githubusercontent.com/65654614/111159552-8ffdb400-85dc-11eb-8f0b-db130fcf6125.png)


## dependencies

`pip install "napari[all]" napari_video pandas`

## how to use

To start, update `config.yaml` and then execute `python behavior_annotator.py`.

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
