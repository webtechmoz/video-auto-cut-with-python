import moviepy.editor as mp
import numpy as np
from PIL import Image
import os

def detect_silence(audio_clip, threshold=0.01, chunk_size=0.1):
    """
    Detecta partes silenciosas do clipe de áudio.
    """
    fps = 22050
    chunk_length = int(chunk_size * fps)  # tamanho do chunk em samples
    duration = audio_clip.duration
    non_silent_parts = []

    for start_time in np.arange(0, duration, chunk_size):
        end_time = min(start_time + chunk_size, duration)
        audio_chunk = audio_clip.subclip(start_time, end_time).to_soundarray(fps=fps)
        volume = np.max(np.abs(audio_chunk))
        
        if volume > threshold:
            non_silent_parts.append((start_time, end_time))

    return non_silent_parts

def custom_resize(clip, newsize):
    """
    Redimensiona um clipe de vídeo usando PIL sem usar o atributo 'ANTIALIAS'.
    """
    def resize_frame(frame):
        img = Image.fromarray(frame)
        return np.array(img.resize(newsize[::-1], Image.LANCZOS))
    
    return clip.fl_image(resize_frame)

def cut_video_on_silence(video_path, output_path, image_path= '', silence_threshold=0.01, chunk_size=0.1):
    """
    Corta o vídeo para remover partes silenciosas.
    """
    video = mp.VideoFileClip(video_path)
    audio = video.audio

    non_silent_times = detect_silence(audio, threshold=silence_threshold, chunk_size=chunk_size)
    
    if not non_silent_times:
        print("Nenhuma parte não silenciosa detectada.")
        return

    clips = []
    for start, end in non_silent_times:
        if start < video.duration and end <= video.duration:
            clips.append(video.subclip(start, end))
    
    if image_path != '':
        image = mp.ImageClip(img=image_path, duration=5)
        clips.append(image)
    
    if clips:
        final_clip = mp.concatenate_videoclips(clips)
        final_clip = final_clip.set_fps(30)
        final_clip = custom_resize(final_clip, (1920, 1080))

        final_clip.write_videofile(
            output_path,
            codec='libx264',
            audio_codec='aac',
            audio_bitrate='384k',
            audio_fps=48000,
            preset='medium',
            threads=4,
            ffmpeg_params=[
                '-ac', '2',
                '-aspect', '16:9'
            ]
        )
        
    else:
        print("Nenhum clipe válido encontrado.")


if __name__ == '__main__':
    
    try:
        os.system('cls')
        videofile: str = input('Cole aqui o endereço do video (incluindo a extensão): ')
        imagefile: str = input('Cole o endereço da imagem (se necessário): ')
        nomefinal: str = input('Digite o nome do ficheiro final (incluindo a extensão): ')

        os.system('cls')
        
        cut_video_on_silence(video_path= videofile, image_path= imagefile, output_path= nomefinal, silence_threshold=0.01, chunk_size=0.1)
        
    except Exception as e:
        os.system('cls')
        print(e)