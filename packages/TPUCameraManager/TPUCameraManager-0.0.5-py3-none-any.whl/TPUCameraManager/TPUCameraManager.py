from . import gstreamer
import threading
import enum
import numpy as np
class CameraManager:
    def __init__(self):
        self.camClasses = []
    def newCam(self,device,streamType,res,fps):
        newCamClass = Cam(device,streamType,res,fps)
        #self.camClasses.append(newCamClass)
        return newCamClass
    def close(self,camClass):
        print(camClass)
        camClass.kill()
        del camClass
    def __len__():
        return len(camClasses)

class Cam:
    def __init__(self,device,streamType,res,fps):
        self.thread = threading.Thread(target=gstreamer.run_pipeline,args=(str(streamType).format(device,res[0],res[1],fps),self.on_buffer))
        self.res = res
        self.streamType = streamType
        self.thread.start()
        self.data = None
        self.newdata = False
        
    def on_buffer(self, data, _):
        self.data = data
        self.newdata = True
    
    def getImage(self):
        if self.streamType is GStreamerPipelines.RGB:
            self.newdata = False
            nparr = np.frombuffer(self.data, dtype=np.uint8)
            image = nparr.reshape(self.res[1], self.res[0], 3)
            return(image)
        else:
            print("Can't return image of H264 stream")
            return(None)

    def kill(self):
        print("killing")
        gstreamer.quit()
        self.thread.join()
    def __bytes__(self):
        self.newdata = False
        return self.data
    def __bool__(self):
        return self.newdata
    
class GStreamerPipelines(enum.Enum):
    H264 = "v4l2src device=/dev/video{0} ! video/x-raw,format=YUY2,width={1},height={2},framerate={3}/1 ! tee name=t t. ! queue max-size-buffers=1 leaky=downstream ! videoconvert ! x264enc speed-preset=ultrafast tune=zerolatency threads=4 key-int-max=5 bitrate=1000 aud=False bframes=1 ! video/x-h264,profile=baseline ! h264parse ! video/x-h264,stream-format=byte-stream,alignment=nal ! appsink name=h264sink emit-signals=True max-buffers=1 drop=False sync=False"
    RGB = "v4l2src device=/dev/video{0} ! video/x-raw,format=YUY2,width={1},height={2},framerate={3}/1 ! tee name=t t. ! queue ! glfilterbin filter=glbox ! video/x-raw,format=RGB,width={1},height={2},framerate={3}/1 ! appsink name=appsink emit-signals=True max-buffers=1 drop=True sync=False"

    def __str__(self):
        return self.value