# 🐳 Dockerize Python Script

## Description
This project demonstrates how to turn a regular .py file into a Docker container in just 10 minutes, which can run on any system without installing Python or dependencies.
The script asks for a city from the user and displays a short weather forecast from wttr.in
.
Uses the requests library.
The container isolates the script, making it portable and easy to run.

## 🗂️ Project Structure
```commandline
dockerize-python/
│
├── app.py              # Python script for weather forecast
├── requirements.txt    # Python dependencies
└── Dockerfile          # Docker instructions

```

## 🐍 Installation and Run (Without Docker)
* Install Python 3.x 
* Install dependencies:
```bash 
   pip install -r requirements.txt 
```
* Run the script:
```bash 
   python app.py 
```

## 🐳 Docker — Build and Run
* Build the Docker image:
```commandline
   docker build -t python-weather .
```
* Run the Docker container:
```commandline
   docker run -it python-weather
```
* The -it flag allows interactive input for the city.
* Example output:
```commandline
   Enter city: London
   London: ☀️ +15°C
```

