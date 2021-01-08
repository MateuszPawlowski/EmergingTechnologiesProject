# EmergingTechnologiesProject - Mateusz Pawlowski(G00361162)
This is our project for Emerging Technologies for 4 Year.For this project we had to create a web service that uses machine learning to make predictions on a data set that we were given called the 'power production'. The goal is to produce a model that will predict wind turbine power, output from wind speed values, as in the data set. Here are the requirements in order to run the app in the Web: 
* Anaconda 3
* Docker Desktop
* Python (version 3)

More information about the project is inside the jupyter notebook.

# How To Run
* Create a folder on your desktop.
* Open up your cmd (Command Prompt) and direct yourslef to that directory.
* Type in git clone https://github.com/MateuszPawlowski/EmergingTechnologiesProject
* Go into the new folder
* Depending on the option, here are the following steps that need to be written into the cmd:
#### Using Docker
* docker build -t web-service .
* docker run -d -p 5000:5000 web-service
* docker images (show how many images are running)
* docker kill (CONTAINER ID) (Kills specific image)
* In your browser type: http://127.0.0.1:5000/
#### No Docker
* set FLASK_APP=WebService.py
* python -m flask run
* In youre browser type: http://127.0.0.1:5000/
