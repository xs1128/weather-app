# Weather Web App

## Local Setup
> [!NOTE]
> Have Python installed on your local device. <br/>
> Please follow the steps strictly.

### Install and Open
1. Download the project **`ZIP file`** by clicking the green **`<> Code ▼`** button.
2. Extract the project_name.zip folder to your desired file path/directory.
3. Open the extracted folder using an [IDE]() or text editor ([Visual Studio Code]() recommended).
### Run and Host
1. Open the terminal and make sure you are on `...\weather_app>` (I am on powershell terminal)
2. Create a virtual environment using the command:
```
python -m venv env
```
3. Install required packages using the command:
```
pip install -r requirements.txt
```
4. Move into the `weather_project` directory using the command:
```
cd weather_project
```
- You should be in `...\weather_app/weather_project>` by now

5. Run the server on localhost using the command:
```
python manage.py runserver
```

## Website
> [!IMPORTANT]
> The website will be active until **`Saturday 03 August 2024`**. <br/>
> If a website activation request, anything is wrong or can be improved, feel free to contact me.

>[!NOTE]
> No setup is needed

Click this [link](https://xs1128.pythonanywhere.com/) to direct to my weather app page.

### Setting up your own web weather app:
1. Find a web hosting service.
2. Follow the host's guidelines to set up the server live.

> [!Tip]
> I am using PythonAnywhere's free plan to host the website.
> If you are using this web hosting service, this video ([link](https://www.youtube.com/watch?v=xtnUwvjOThg&t=993s)) may help you set up the website.

## Credits
Language: [Python](https://www.python.org/), HTML (Standard Markup) <br/>
Frameworks: [Django](https://www.djangoproject.com/) <br/>
Web templating engine: [Jinja](https://jinja.palletsprojects.com/en/3.1.x/) <br/>
Weather Data Source: [Weather API](https://www.weatherapi.com/) <br/>
Packages used: [here](./requirements.txt)
