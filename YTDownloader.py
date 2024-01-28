# YouTube Video Downloader

# Advanced Code 

from pytube import YouTube
import tkinter as tk
from tkinter import filedialog  
import time

def download_video(url, save_path) : 
  try:
    yt = YouTube(url)

    streams = yt.streams.filter(progressive=True, file_extension="mp4")
    heighest_res_stream = streams.get_by_resolution(480)

    time.sleep(10)

    heighest_res_stream.download(output_path= save_path)
    print("Video Dowloaded Successfully!")

  except Exception as e: 
    print(e)

def open_file_dialog(): 
  folder = filedialog.askdirectory()
  
  if folder : 
    print(f"Selected Folder: {folder}")
  
  return folder

if __name__ == "__main__" : 
  root = tk.Tk()
  root.withdraw()

  video_url = input("Please Enter A YouTubbe Url: ")
  save_dir = open_file_dialog()

  if save_dir:
    print("Started Download...") 
    download_video(video_url, save_dir)

  else: 
    print("Invalid Save Location.")
