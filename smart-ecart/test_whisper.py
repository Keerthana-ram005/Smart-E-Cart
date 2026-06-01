import sys
sys.path.append('backend')
from services.whisper_service import transcribe_audio
import os

test_audio = 'test.wav'
if not os.path.exists(test_audio):
    # create a dummy wav file with 1 sec of silence using ffmpeg
    import subprocess
    subprocess.run(['ffmpeg', '-y', '-f', 'lavfi', '-i', 'anullsrc=r=16000:cl=mono', '-t', '1', test_audio], stderr=subprocess.DEVNULL)

print('Testing whisper...')
res = transcribe_audio(test_audio)
print('TRANSCRIPT:', repr(res))
