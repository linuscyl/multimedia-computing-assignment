import moviepy.editor as mpe

videoclipavi = mpe.VideoFileClip("001.avi")
# videoclip = mpe.VideoFileClip("001s.mp4")
audioclip = mpe.AudioFileClip("recorded.wav")

# final_audio = mpe.CompositeAudioClip([audioclip, videoclip.audio])
final_clip_avi = videoclipavi.set_audio(audioclip)
# final_clip = videoclip.set_audio(audioclip)

final_clip_avi.write_videofile("finalAVI.avi")
# final_clip.write_videofile("final_mp4.mp4")

