from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from scipy.interpolate import interp1d

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volume.GetMute()
print(volume.GetMasterVolumeLevel())
volume.GetVolumeRange()
m = interp1d([1,100],[-61.0,-0.0])
print(m(1))
volume.SetMasterVolumeLevel(-59.4, None)