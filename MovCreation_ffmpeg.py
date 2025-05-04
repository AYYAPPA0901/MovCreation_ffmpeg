import os
import subprocess
import maya.cmds as cmds

def create_mov_from_exr(exr_folder, output_mov, framerate=24):

    if not os.path.exists(exr_folder):
        print(f"EXR folder '{exr_folder}' does not exist.")
        return

    ffmpeg_command = [
        'ffmpeg', # ffmpeg command exe path
        '-framerate', str(framerate),
        '-i', os.path.join(exr_folder, '%04d.exr'),
        '-c:v', 'prores',
        '-profile:v', '0',
        output_mov
    ]

    print("Running command:", ' '.join(ffmpeg_command))

    try:
        subprocess.run(ffmpeg_command, check=True)
        print(f"Successfully created MOV file: {output_mov}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")


exr_folder = ""   # Add EXR PATH
output_mov = ""  # Add Mov Path Where Mov Need To Generate
create_mov_from_exr(exr_folder, output_mov)