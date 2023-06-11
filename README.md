## Python-automation
A Python automation tool is a powerful software solution that harnesses the capabilities of the Python programming language to automate repetitive tasks and streamline workflows. It provides developers and users with a versatile toolkit to create scripts, programs, and workflows that can perform a wide range of automated actions. <br><br>
## So here is a automation tool which performs two task
**1.Downloading a youtube video to device:-**<br>
To download a YouTube video to your device using Python, you can follow these general steps:
<ol>
<li>Identify the URL: Find the YouTube video you want to download and copy the URL from the browser's address bar.</li>

<li>Install dependencies: You'll need to install a Python library that supports YouTube video downloading, such as pytube. You can use a package manager like pip to install the required libraries.</li>

<li>Create a Python script: Write a Python script that utilizes the pytube library to download the video. You'll typically use the video URL obtained in step 1 to initialize a YouTube object and call the appropriate methods to download the video file.</li>

<li>Execute the script: Run the Python script to start the download process. The video will be saved to your device's local storage in the directory specified in the script or the default location.</li>
</ol>  
**2.Downloading full youtube video playlist to device:-** 
<ol>
  <li>Obtain playlist URL: Find the YouTube playlist you want to download and copy its URL from the browser's address bar. Make sure you have the URL of the entire playlist, not just an individual video within the playlist.</li>

<li>Install necessary dependencies: You'll need to install a Python library that supports YouTube video downloading and playlist handling, such as pytube. Use a package manager like pip to install the required libraries.</li>

<li>Create a Python script: Write a Python script that utilizes the pytube library or another appropriate library to handle playlist downloads. The script should take the playlist URL obtained in step 1 as input and extract the individual video URLs from the playlist.</li>

<li>Download the videos: Iterate through the list of video URLs obtained from the playlist and use the chosen library to download each video one by one. You may need to specify the desired download location or any other preferences within your script.</li>
 <li> Execute the script: Run the Python script, providing the playlist URL as input. The script will start downloading the videos in the playlist, saving them to the specified location on your device.</li>
</ol>  

## Run
```html
git clone https://github.com/annanya-mathur/Python-automation.git
```
```html
pip install -r requirements.txt
```
## Resources and Documentation

Pytube :- https://pytube.io/en/latest/  <br><br>
Sys :- https://docs.python.org/3/library/sys.html  <br><br>
Xml :- https://docs.python.org/3/library/xml.etree.elementtree.html  <br><br>
Os :- https://docs.python.org/3/library/os.html

