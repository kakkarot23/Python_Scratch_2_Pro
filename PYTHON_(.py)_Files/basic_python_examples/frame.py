import cv2
import os
import tkinter as tk
from tkinter import filedialog

def videos_to_frames(input_folder, output_dir, target_fps=10):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # List all video files in the folder
    video_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.mp4', '.avi', '.mov', '.mkv'))]

    frame_id = 0  # global frame counter across all videos

    for video_file in video_files:
        video_path = os.path.join(input_folder, video_file)
        print(f"Processing {video_path} ...")

        cap = cv2.VideoCapture(video_path)
        video_fps = cap.get(cv2.CAP_PROP_FPS)
        if video_fps == 0:
            print(f"⚠️ Skipping {video_file}, could not read FPS")
            continue

        frame_interval = int(round(video_fps / target_fps))
        count = 0

        while True:
            success, frame = cap.read()
            if not success:
                break

            if count % frame_interval == 0:
                frame_filename = os.path.join(output_dir, f"frame_{frame_id:06d}.jpg")
                cv2.imwrite(frame_filename, frame)
                print(f"Saved {frame_filename}")
                frame_id += 1

            count += 1

        cap.release()
        print(f"Finished {video_file}")

    print(f"✅ Done! Extracted {frame_id} frames from {len(video_files)} videos.")

# =========================
# MAIN SCRIPT
# =========================
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide tkinter main window

    # Ask user to select input folder
    input_folder = filedialog.askdirectory(title="Select Folder Containing Videos")
    if not input_folder:
        print("No folder selected. Exiting...")
        exit()

    # Ask user to select output folder
    output_folder = filedialog.askdirectory(title="Select Output Folder to Save Frames")
    if not output_folder:
        print("No output folder selected. Exiting...")
        exit()

    videos_to_frames(input_folder, output_folder, target_fps=10)
