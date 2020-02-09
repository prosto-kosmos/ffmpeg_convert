#перед запуском скачайте библиотеку
#pip install ffmpeg-python

#Установите FFmpeg и добавьте путь к  ffmpeg.exe в переменные среды

import ffmpeg
import os
import time

def convert_avi_to_mp4(avi_file_path, output_name):
    os.popen("ffmpeg -i {inp} {output}".format(inp = avi_file_path, output = output_name))
    #-vcodec libx264 -acodec libvo_aacenc
    return True

def add_sound(avi_file_path, s_file_path):
    os.popen("ffmpeg -i {inp_v} -i {inp_s} input_with_sound.avi".format(inp_v = avi_file_path, inp_s = s_file_path))
    return True


probe = ffmpeg.probe('input.avi')
video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
print(video_stream.keys())

my_file = open("meta.txt", "wt")

my_file.write('Название кодека: '+video_stream['codec_name'] +'\n')
my_file.write('Тип кодека: '+video_stream['codec_type'] +'\n')
my_file.write('Битрэйт: '+video_stream['bit_rate'] +'\n')
my_file.write('Ширина: '+str(video_stream['width']) +'\n')
my_file.write('Высота: '+str(video_stream['height']) +'\n')
my_file.close()

add_sound('input.avi', 'son.wav');
time.sleep(3)
convert_avi_to_mp4('input_with_sound.avi', 'output.mp4');


'''
test_video = ffmpeg.input('input.avi')
audio = test_video.audio
new_test_video = ffmpeg.hflip(test_video)
new_test_video = ffmpeg.output(new_test_video, audio, 'output.avi')
new_test_video = ffmpeg.overwrite_output(new_test_video)

ffmpeg.run(new_test_video)
'''
