# Yolo_mark
**Windows** & **Linux** GUI for marking bounded boxes of objects in images

* To compile on **Windows** open `yolo_mark.sln` in MSVS2013/2015, compile it **x64 & Release**. Change paths in `yolo_mark.sln` to the OpenCV 2.x/3.x installed on your computer:

    * (right click on project) -> properties -> C/C++ -> General -> Additional Include Directories: `C:\opencv_3.0\opencv\build\include;`
        
    * (right click on project) -> properties -> Linker -> General -> Additional Library Directories: `C:\opencv_3.0\opencv\build\x64\vc14\lib;`

* To compile on **Linux** type in console 3 commands:
    ```
    cmake .
    make
    ```

* To run on **Windows**:
    ```
    yolo_mark.exe data/img data/labels data/train.txt data/obj.names
    ```

* To run on **Linux**:
    ```
    ./yolo_mark data/img data/labels data/train.txt data/obj.names
    ```

Supported both: OpenCV 2.x and OpenCV 3.x

--------

Arguments:
  * `data/img` - directory containing all images
  * `data/labels` - empty directory where all the labels will be saved
  * `data/train.txt` - path to file where all paths to the images will be saved.
  * `data/obj.names` - files with names of objects. The objects names should be in seperate lines.

#### How to get frames from videofile:

To get frames from videofile (save each N frame, in example N=10), you can use this command:
* on Windows: `yolo_mark.exe data/img cap_video test.mp4 10`
* on Linux: `./yolo_mark data/img cap_video test.mp4 10`

Directory `data/img` and `data/labels` should be created before this. Also on Windows, the file `opencv_ffmpeg340_64.dll` from `opencv\build\bin` should be placed near with `yolo_mark.exe`.

As a result, many frames will be collected in the directory `data/img`. Then you can label them manually using such command: 
* on Windows: `yolo_mark.exe data/img data/labels data/train.txt data/obj.names`
* on Linux: `./yolo_mark data/img data/labels data/train.txt data/obj.names`

#### How to create validation set

To create validation (test) set use script `test_set_creator.py` as described below:
  ```
  ./scripts/test_set_creator.py data/img data precentage
  ```
where:
  `data/img` - path to directory with images.
  `data' - path to directory where list will be saved.
  `percentage` - integer number that represents percentage of validation images from whole dataset.

----

![Image of Yolo_mark](https://habrastorage.org/files/229/f06/277/229f06277fcc49279342b7edfabbb47a.jpg)

