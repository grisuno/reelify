#!/usr/bin/env python3
# _*_ coding: utf8 _*_
"""
app.py

Autor: Gris Iscomeback
Correo electrónico: grisiscomeback[at]gmail[dot]com
Fecha de creación: xx/xx/xxxx
Licencia: GPL v3

Descripción:  
"""
import cv2
import numpy as np
from moviepy.editor import VideoFileClip, concatenate_videoclips
import os

def crop_and_resize_clip(clip, left_half=True):
    width, height = clip.w, clip.h
    
    crop_width = width // 2
    x1 = 0 if left_half else crop_width
    x2 = crop_width if left_half else width
    
    cropped_clip = clip.crop(x1=x1, y1=0, x2=x2, y2=height)
    
    new_height = int(crop_width * (16/9))
    
    if new_height > height:
        new_width = int(height * (9/16))
        resized_clip = cropped_clip.resize(width=new_width)
        final_clip = resized_clip.crop(x_center=new_width/2, y_center=height/2, width=new_width, height=height)
    else:
        resized_clip = cropped_clip.resize(height=new_height)
        final_clip = resized_clip.crop(x_center=crop_width/2, y_center=new_height/2, width=crop_width, height=new_height)
    
    return final_clip

def create_short_videos(input_path, output_prefix, durations=[30, 59, 179]):
    clip = VideoFileClip(input_path)
    total_duration = clip.duration
    
    segment_duration = total_duration / 10
    segments = [clip.subclip(i*segment_duration, (i+1)*segment_duration) for i in range(10)]
    
    for duration in durations:
        num_segments = min(10, max(1, int(duration / segment_duration)))
        output_segments = segments[:num_segments]
        
        if sum(c.duration for c in output_segments) < duration:
            
            last_segment = output_segments[-1]
            remaining_time = duration - sum(c.duration for c in output_segments)
            looped_segment = last_segment.loop(duration=remaining_time)
            output_segments.append(looped_segment)
        
        final_clip = concatenate_videoclips(output_segments)
        final_clip = final_clip.subclip(0, duration)  
        
        cropped_clip = crop_and_resize_clip(final_clip)
        
        output_path = f"{output_prefix}_{duration}s.mp4"
        cropped_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")
        
        cropped_clip.close()
    
    clip.close()

def list_and_select_video():
    video_files = [f for f in os.listdir() if f.endswith(('.mp4', '.mkv'))]
    if not video_files:
        print("No se encontraron archivos MP4 o MKV en el directorio.")
        return None
        
    print("Archivos de video encontrados:")
    for i, file in enumerate(video_files):
        print(f"{i+1}. {file}")
    
    while True:
        try:
            file_index = int(input("Selecciona el número del archivo que deseas procesar: ")) - 1
            if 0 <= file_index < len(video_files):
                return video_files[file_index]
            else:
                print("Número fuera de rango. Inténtalo de nuevo.")
        except ValueError:
            print("Entrada no válida. Introduce un número.")

def main():
    input_video = list_and_select_video()
    
    if input_video:
        output_prefix = f"{os.path.splitext(input_video)[0]}_short"
        create_short_videos(input_video, output_prefix)
        print(f"Los videos cortos han sido creados y guardados con el prefijo {output_prefix}")

if __name__ == "__main__":
    main()
