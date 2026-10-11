# Gemini-screen-bridge
Are you done with using AI in linux platforms try Gemini-Screen Bridge for instant solutions for your poblems appearing on your screen answers are just a hotkey away. Gemini Screen Bridge will fill the gap between taking A screenshot and uploading to any AI platform. It uses Gemini 3.5 Flash lite for the answers. The interactive python UI will help you to dig more about the solution in one click. Users can claim their free API from google ai studio and use this tool seemlessly. No account frustration or anything. Just setup the tool and set your hotkey and dive into this tool .press the hotkey get the answer ,dig the answer and save  your time .

#Installing dependencies 

sudo apt update

sudo apt install scort python3-tk

python3-pip

#Navigate to the gemini screen bridge folder

cd/Gemini-screen-bridge

#Create virtual environment for python

python3 m venv venv

#Activate the virtual environment

Source venv/bin/activate

#install the requirements  

pip install-r requirements.txt

#Users are recquired to use their personal gemini API key . To get ur free gemini API log in to google ai studio . And generate and copy you API and paste it into your run.sh file using text editor in the part where Enter your API is given and save your changes

#make your file executable

chmod +x run.sh

#users can run the apllication using 

./run.sh


Now for a hassle free running create a shortcut in keyboard using the below command as the command for shortcut(change the path to actual location)

/path to/gemini-sticky-bridge/run.sh 
