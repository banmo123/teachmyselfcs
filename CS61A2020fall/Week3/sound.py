from wave import open
from struct import Struct #以wav文件需要的形式编码整型
from math import floor

frame_rate = 11025 #帧率，每秒有多少个声波函数对应的值

def encode(x):
    """encode float x between -1 and 1 as two bytes"""
    i = int(16384 * x)
    return Struct('h').pack(i)

def play(sampler, name = 'song.wav', seconds = 2):
    """Write the output of a sampler function as a wav file"""
    out = open(name, 'wb')
    out.setnchannels(1)
    out.setsampwidth(2)
    out.setframerate(frame_rate)
    t = 0
    while t < seconds * frame_rate:
        sample = sampler(t)
        out.writeframes(encode(sample))
        t = t + 1
    out.close()

def tri(frequency, amplitude = 0.3):
    """A continuous triangle wave"""
    period = frame_rate // frequency #一个周期里要取多少个点
    def sampler(t):
        saw_wave = t / period - floor(t / period +0.5)
        tri_wave = 2 * abs(2 * saw_wave) - 1
        return amplitude * tri_wave
    return sampler

c_freq, e_freq, g_freq = 261.63, 329.63, 392.00
def both(f, g):
    return lambda t: f(t) + g(t)

def note(f, start, end, fade = 0.01):
    def sampler(t):
        seconds = t / frame_rate
        if seconds < start or seconds > end:
            return 0
        elif seconds < start + fade:
            return (seconds - start) / fade * f(t)
        elif seconds > end - fade:
            return (end - seconds) / fade * f(t)
        else:
            return f(t)
    return sampler

def mario_at(octave):
    c, e = tri(octave * c_freq), tri(octave * e_freq)
    g, low_g = tri(octave * g_freq), tri(octave * g_freq * 0.5)
    return mario(c, e, g, low_g)
# play(both(note(c, 0, 1/4), note(e, 1/2, 1)))

def mario(c, e, g, low_g):
    z = 0
    song = note(e, z ,z + 1/8)
    z += 1/8
    song = both(song, note(e, z ,z + 1/8))
    z += 1/4
    song = both(song, note(e, z ,z + 1/8))
    z += 1/4
    song = both(song, note(c, z ,z + 1/8))
    z += 1/8
    song = both(song, note(e, z ,z + 1/8))
    z += 1/4
    song = both(song, note(g, z ,z + 1/4))
    z += 1/2
    song = both(song, note(low_g, z ,z + 1/8))
    z += 1/2
    return song

play(both(mario_at(1), mario_at(0.5)))