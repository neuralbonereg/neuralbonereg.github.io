import os
import subprocess

input_root = "videos_new"             # root folder with videos and subfolders
output_root = "videos_compressed" # folder to save compressed videos

# Walk through all directories and files
for dirpath, dirnames, filenames in os.walk(input_root):
    # Compute the corresponding output directory
    relative_path = os.path.relpath(dirpath, input_root)
    output_dir = os.path.join(output_root, relative_path)
    os.makedirs(output_dir, exist_ok=True)

    for filename in filenames:
        if filename.lower().endswith((".mp4", ".mov", ".avi", ".mkv")):
            input_path = os.path.join(dirpath, filename)
            output_path = os.path.join(output_dir, filename)

            # FFmpeg compression command
            command = [
                "ffmpeg",
                "-i", input_path,
                "-vcodec", "libx264",
                "-crf", "35",
                "-preset", "fast",
                "-acodec", "aac",
                "-b:v", "2M",
                "-vf", "scale=-2:480",
                output_path
            ]

            print(f"Compressing {input_path} → {output_path}")
            subprocess.run(command, check=True)

print("All videos in folder and subfolders compressed!")