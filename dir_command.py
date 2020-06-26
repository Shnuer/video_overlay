import subprocess
import os

def get_absolute_file_path(file_name):
    return os.path.normpath(f'{os.getcwd()}/{file_name}')


def execute_ffprobe(cmd):
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    output = proc.communicate()
    return eval(output[0])

def execute_ffmpeg(cmd):
    subprocess.run(cmd)

def get_video_file_duration(file_name):
    return execute_ffprobe(f"ffprobe -v error "
                           f"-show_entries format=duration "
                           f"-of default=noprint_wrappers=1:nokey=1 "
                           f"{get_absolute_file_path(file_name)}")

def get_duration_video_in_seconds(file_name):
    return get_video_file_duration(file_name)

def overlay_sub_to_video(input_video_file_name, output_video_file_name, file_name_subtitle):
    
    execute_ffmpeg(f"ffmpeg -i {get_absolute_file_path(input_video_file_name)} "
                    f"-vcodec libx264 -vf subtitles={file_name_subtitle} "
                    f"{get_absolute_file_path(output_video_file_name)} -y")