from pytube import YouTube
from sys import argv
import xml.etree.ElementTree as ET
import os

link = argv[1]
yt = YouTube(link)

print("Title: ", yt.title)

print("View: ", yt.views)



yd = yt.streams.get_highest_resolution()

# ADD VIDEO TO FOLDER 
yd.download('./YTfolder')

caption = yt.captions.get_by_language_code('en')
try:
    #print(yt.captions)
    print(caption.xml_captions)
    #print(caption.xml_captions.generate_srt_captions())
except:
    print("This video has no captions")

# PRINT CAPTIONS

try:
    xml_captions = caption.xml_captions
    if xml_captions:
        root = ET.fromstring(xml_captions)
        
        # Iterate over each <p> tag and extract the text
        for p in root.iter('p'):
            caption_text = p.text
            print(caption_text)
    else:
        print("No XML captions found for this video")
except:
    print("This video has no captions")



# SAVE CAPTIONS TO FILE

try:
    xml_captions = caption.xml_captions
    if xml_captions:
        root = ET.fromstring(xml_captions)

        # Extract the video name
        video_name = yt.title.replace('/', '_')  # Replace any '/' in the video title

        # Create the folder path
        folder_path = "./Captions"
        os.makedirs(folder_path, exist_ok=True)

        # Create the file path
        file_name = f"{video_name}_captions.txt"
        file_path = os.path.join(folder_path, file_name)

        # Open the file for writing
        with open(file_path, 'w', encoding='utf-8') as file:
            # Iterate over each <p> tag and extract the text
            for p in root.iter('p'):
                caption_text = p.text
                file.write(caption_text + '\n')

        print(f"Caption text saved to {file_path}")
    else:
        print("No XML captions found for this video")
except:
    print("This video has no captions")
