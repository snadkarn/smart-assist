# Mouse Control
This is my modification of the [original script](https://gist.github.com/willpatera/7908319#file-stream_gaze_coords-py) so you don't need to enable Marker Tracking or define surfaces. You simply need to start the [Coordinates Streaming Server](https://github.com/pupil-labs/pupil/wiki/Pupil-capture#pupil-server) in [Pupil](https://github.com/pupil-labs/pupil/) and run this independent script.

**Note:** Not using Surfaces and Marker Tracking decreases the accuracy of pointer movement. This won't work well enough because `norm_gaze` data is being used instead of your surface gaze data.

You need `PyMouse` and `Xlib` installed:

```
$ sudo pip install pymouse
$ sudo apt-get install python-xlib
```