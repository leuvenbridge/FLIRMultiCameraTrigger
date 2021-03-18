import PySpin
 
# Set camera serial numbers
serial_1 = '18497149'
serial_2 = '18421571'
serial_3 = '18421570'
 
# Get system
system = PySpin.System.GetInstance()
 
# Get camera list
cam_list = system.GetCameras()
 
# Get cameras by serial
cam_1 = cam_list.GetBySerial(serial_1)
cam_2 = cam_list.GetBySerial(serial_2)
cam_3 = cam_list.GetBySerial(serial_3)
 
# Initialize cameras
cam_1.Init()
cam_2.Init()
cam_3.Init()

# Set up primary camera trigger
cam_1.TriggerMode.SetValue(PySpin.TriggerMode_Off)
cam_1.TriggerSource.SetValue(PySpin.TriggerSource_Line2)
#cam_1.TriggerOverlap.SetValue(PySpin.TriggerOverlap_ReadOut)
cam_1.TriggerMode.SetValue(PySpin.TriggerMode_On)

# Set up secondary camera trigger
cam_2.TriggerMode.SetValue(PySpin.TriggerMode_Off)
cam_2.TriggerSource.SetValue(PySpin.TriggerSource_Line2)
#cam_2.TriggerOverlap.SetValue(PySpin.TriggerOverlap_ReadOut)
cam_2.TriggerMode.SetValue(PySpin.TriggerMode_On)
 
# Set up secondary camera trigger
cam_3.TriggerMode.SetValue(PySpin.TriggerMode_Off)
cam_3.TriggerSource.SetValue(PySpin.TriggerSource_Line2)
#cam_3.TriggerOverlap.SetValue(PySpin.TriggerOverlap_ReadOut)
cam_3.TriggerMode.SetValue(PySpin.TriggerMode_On)

# Set acquisition mode to acquire a single frame, this ensures acquired images are sync'd since camera 2 and 3 are setup to be triggered
cam_1.AcquisitionMode.SetValue(PySpin.AcquisitionMode_SingleFrame)
cam_2.AcquisitionMode.SetValue(PySpin.AcquisitionMode_SingleFrame)
cam_3.AcquisitionMode.SetValue(PySpin.AcquisitionMode_SingleFrame)
 
# Start acquisition; note that secondary cameras have to be started first so acquisition of primary camera triggers secondary cameras.
cam_2.BeginAcquisition()
cam_3.BeginAcquisition()
cam_1.BeginAcquisition()
 
# Acquire images
image_1 = cam_1.GetNextImage()
image_2 = cam_2.GetNextImage()
image_3 = cam_3.GetNextImage()
 
# Save images
image_1.Save('cam_1.png')
image_2.Save('cam_2.png')
image_3.Save('cam_3.png')
 
# Release images
image_1.Release()
image_2.Release()
image_3.Release()
 
# end acquisition
cam_1.EndAcquisition()
cam_2.EndAcquisition()
cam_3.EndAcquisition()