
import pyaudio
import time
import numpy
import keyboard
import fluidsynth

fs = fluidsynth.Synth()
sfid = fs.sfload("example.sf2")
fs.program_select(0, sfid, 0, 41)

keys = {'1': 48, '2': 49, '3': 50, '4': 51, '5': 52, '6': 53, '7': 54, '8': 55, '9': 56, '0': 57, '-': 58, '=': 59,
        'q': 60, 'w': 61, 'e': 62, 'r': 63, 't': 64, 'y': 65, 'u': 66, 'i': 67, 'o': 68, 'p': 69, '[': 70, ']': 71,
        'a': 72, 's': 73, 'd': 74, 'f': 75, 'g': 76, 'h': 77, 'j': 78, 'k': 79, 'l': 80, ';': 81, "'": 82, 'enter': 83}
pressed_keys = {key: False for key in keys.keys()}


def hook(key):
    if key.event_type == "down":
        if key.name in keys:
            if not pressed_keys[key.name]:
                fs.noteon(0, keys[key.name], 127)
                pressed_keys[key.name] = True

    if key.event_type == "up":
        if key.name in keys:
            fs.noteoff(0, keys[key.name])
            pressed_keys[key.name] = False


keyboard.hook(hook)
keyboard.wait()
WIDTH = 2
CHANNELS = 2
RATE = 44100

p = pyaudio.PyAudio()

def callback(in_data, frame_count, time_info, status):
    s = numpy.append(s, fl.get_samples(44100 * 1))
    return (in_data, pyaudio.paContinue)

stream = p.open(format=p.get_format_from_width(WIDTH),
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                stream_callback=callback)

stream.start_stream()

while stream.is_active():
    time.sleep(1)

stream.stop_stream()
stream.close()

p.terminate()