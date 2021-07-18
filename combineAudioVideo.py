import moviepy.editor as mpe

def main():
	videoclipavi = mpe.VideoFileClip("demo_divx.avi")
	videoclip = mpe.VideoFileClip("demo_mjpg.avi")
	audioclip = mpe.AudioFileClip("recorded.wav")

	# final_audio = mpe.CompositeAudioClip([audioclip, videoclip.audio])
	final_clip_avi = videoclipavi.set_audio(audioclip)
	final_clip = videoclip.set_audio(audioclip)

	final_clip_avi.write_videofile("demo_divx_final.mp4")
	final_clip.write_videofile("demo_mjpg_final.mp4")

if __name__ == "__main__":
    main()
