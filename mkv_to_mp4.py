from moviepy.editor import VideoFileClip

# Specifica il percorso del file MKV di input e del file MP4 di output
input_file = r'C:\Users\DDCori\personal\Video\vokoscreenNG-2024-10-17_11-30-44 - call per pipeline RMS - Luca Riccardo.mkv'
output_file = r'C:\Users\DDCori\personal\Video\vokoscreenNG-2024-10-17_11-30-44 - call per pipeline RMS - Luca Riccardo.mp4'

# Carica il file MKV e lo salva come MP4
try:
    clip = VideoFileClip(input_file)
    clip.write_videofile(output_file, codec="libx264")
    print(f"Conversione completata: {output_file}")
except Exception as e:
    print(f"Errore durante la conversione: {e}")
