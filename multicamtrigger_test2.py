import os
import sys
import time
import PySpin
import numpy as np
from datetime import datetime
from MonkFrames import MonkeyFrames

MONKEY, DURATION, FRAME_RATE = MonkeyFrames()

DATE        = datetime.now().strftime("%Y%m%d")
MONKEY_DATE = '%s_%s' % (MONKEY, DATE)

NUM_IMAGES = 10

# Set camera serial numbers
serial_no = ['18497149','18421571','18421570','18421566','18421573','18497151']
TS_IMAGES   = []  # timestamps for individual acquired images

# Get system
system = PySpin.System.GetInstance()
 
# Get camera list
cam_list = system.GetCameras()

for i in range(len(serial_no)):
    cam = cam_list.GetBySerial(serial_no[i])
    cam.Init()
    cam.TriggerMode.SetValue(PySpin.TriggerMode_Off)
    cam.TriggerSource.SetValue(PySpin.TriggerSource_Line2)
    cam.TriggerMode.SetValue(PySpin.TriggerMode_On)
    cam.AcquisitionMode.SetValue(PySpin.AcquisitionMode_SingleFrame)
    cam.BeginAcquisition()
    # make new directories for each camera if not exist
    dir_this = os.path.join('D:', '\\', MONKEY, MONKEY_DATE, serial_no[i])
    if not os.path.exists(dir_this):
        os.makedirs(dir_this)

for i in range(NUM_IMAGES):
    time_now = datetime.now()
    time_since_midnight = time_now.hour*3600 + time_now.minute*60 + time_now.second + time_now.microsecond/1000000
    TS_IMAGES.append(time_since_midnight)
    for j in range(len(serial_no)):
        serial_this = serial_no[j]
        cam = cam_list.GetBySerial(serial_this)
        filename = '%s-%d.png' % (serial_this, i)
        dir_this = os.path.join('D:', '\\', MONKEY, MONKEY_DATE, serial_this)
        os.chdir(dir_this)
        image_this = cam.GetNextImage()
        image_this.Save(filename)
        image_this.Release()

# save timestamps
TS_IMAGES_save_dir = 'D:\\%s\\%s' % (MONKEY, MONKEY_DATE)
os.chdir(TS_IMAGES_save_dir)
np.save('timestamps' % TS_IMAGES)
    
for i in range(len(serial_no)):
    cam = cam_list.GetBySerial(serial_no[i])
    cam.EndAcquisition()
    cam.DeInit()

# Clear camera list before releasing system
cam_list.Clear()

# Release system instance
system.ReleaseInstance()
    