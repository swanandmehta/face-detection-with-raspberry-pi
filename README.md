# Face detection with raspberry-pi

### Backstory ###
I have few raspberry pi units laying around for while so I decided to do something with them.
last time I created doorbell from it this time I thought maybe I could do something else first thought which i had in my mind was to create something constructive but then i said I didnt tried out the camera module yet so lets give it a go. which resulted into this repo

### Now What does it do ###
It will run continuously till you kill the application I did not wanted to add code for that
it would get img from webcam or camera module ideally first one Yes I have hardcoded to get first cam registered by system.
process it label it and store it under output frame folder afterward it will wait till folder have at least 60 images
and create short video of it with 5 FPS and once done it will remove all those images from the directory
by default the img are stored under output/frame videos are stored under output/video and cascade is stored under input folder

### How to run it ###
sudo apt-get install libatlas-base-dev (Just needed for PI)
Go to folder where you have cloned the repo
python3 -m venv env //This is if you dont want to mess with your current python installation
env/bin/pip install -r requirements.txt //Installing dependencies like open-cv and stuff
env/bin/python main.py //Run the code
Profit ????

It goes without saying but please run commands dont add comments in the terminal while running them
