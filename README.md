## Python-automation
A Python automation tool is a powerful software solution that harnesses the capabilities of the Python programming language to automate repetitive tasks and streamline workflows. It provides developers and users with a versatile toolkit to create scripts, programs, and workflows that can perform a wide range of automated actions. <br><br>
## So here is a automation tool which performs two task
**1.Downloading a youtube video to device:-**<br>
To download a YouTube video to your device using Python, you can follow these general steps:
<ol>
<li><b>Identify the URL:</b> Find the YouTube video you want to download and copy the URL from the browser's address bar.</li>

<li><b>Install dependencies: </b>You'll need to install a Python library that supports YouTube video downloading, such as pytube. You can use a package manager like pip to install the required libraries.</li>

<li><b>Create a Python script:</b> Write a Python script that utilizes the pytube library to download the video. You'll typically use the video URL obtained in step 1 to initialize a YouTube object and call the appropriate methods to download the video file.</li>

<li><b>Execute the script:</b> Run the Python script to start the download process. The video will be saved to your device's local storage in the directory specified in the script or the default location.</li>
</ol>  

<br><br>
**2.Downloading full youtube video playlist to device:-** 
<ol>
  <li><b>Obtain playlist URL:</b> Find the YouTube playlist you want to download and copy its URL from the browser's address bar. Make sure you have the URL of the entire playlist, not just an individual video within the playlist.</li>

<li><b>Install necessary dependencies: </b>You'll need to install a Python library that supports YouTube video downloading and playlist handling, such as pytube. Use a package manager like pip to install the required libraries.</li>

<li><b>Create a Python script:</b> Write a Python script that utilizes the pytube library or another appropriate library to handle playlist downloads. The script should take the playlist URL obtained in step 1 as input and extract the individual video URLs from the playlist.</li>

<li><b>Download the videos:</b> Iterate through the list of video URLs obtained from the playlist and use the chosen library to download each video one by one. You may need to specify the desired download location or any other preferences within your script.</li>
 <li> <b>Execute the script:</b> Run the Python script, providing the playlist URL as input. The script will start downloading the videos in the playlist, saving them to the specified location on your device.</li>
</ol>  

## Steps to run the task

<ol>
  <li><b>Cloning git repo</b></li> 
  
 Cloning a Git repository refers to creating a local copy of an existing remote repository. This allows you to have the entire repository's history, branches, and files on your local machine for easier collaboration, development, and version control.


  
```html
git clone https://github.com/annanya-mathur/Python-automation.git
```
  
   <li><b>Installing dependencies </b></li> 
  A requirements.txt file is a text file commonly used in Python projects to specify the dependencies or packages required for the project to run properly. It typically lists the names and version constraints of the required packages.<br>

Here's an example structure of a requirements.txt file:
package1==1.2.3 <br>
package2>=2.0.0,<3.0.0 <br>
package3==4.5.*<br>

  
```html
pip install -r requirements.txt
```
  
   <li><b>To download single video</b></li> 
  
```html
python auto.py <youtube_url>
```
  
 For eg:- python auto.py https://www.youtube.com/watch?v=a_qW-DnN1k0
   <li><b>To download whole playlist</b></li> 
  
```html
python playlist.py <youtube_url>
```
  
  For eg:- python playlist.py https://www.youtube.com/watch?v=a_qW-DnN1k0
  </ol>  
  
## Resources and Documentation

Pytube :- https://pytube.io/en/latest/  <br><br>
Sys :- https://docs.python.org/3/library/sys.html  <br><br>
Xml :- https://docs.python.org/3/library/xml.etree.elementtree.html  <br><br>
Os :- https://docs.python.org/3/library/os.html

