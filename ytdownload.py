import streamlit as st
import yt_dlp
import os

# Streamlit UI
st.title("🎥 Video Downloader")
st.write("Download videos from YouTube and other websites using PyTube and yt-dlp.")

# User Input
video_url = st.text_input("Enter Video URL:")

# Choose Download Method
#download_method = st.radio("Choose Download Method:", ("PyTube (YouTube)", "yt-dlp (All Sites)"))

download_folder = "downloads"
os.makedirs(download_folder, exist_ok=True)

if st.button("Download Video"):
    if video_url:
        print("Downloading")
        try:
                ydl_opts = {
                    "outtmpl": os.path.join(download_folder, "%(title)s.%(ext)s"),
                    "format": "best",
                }
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info_dict = ydl.extract_info(video_url, download=True)
                    filename = ydl.prepare_filename(info_dict)
                st.success(f"✅ Download Complete: {filename}")
                st.video(filename)  # Show video preview
        except Exception as e:
                st.error(f"❌ Error: {e}")
    else:
        st.warning("⚠️ Please enter a valid video URL.")
