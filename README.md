﻿# rPiManagerDjango

I first made this project using ASP.net core in 2019.  I pretty much haven't used .net since then so I thought I would recreate it in Django.

I had the idea to display a dashboard in a medical laboratory to display analytics such as long turn around times or specimens that are waiting for verification.  I would provide the hardware to display the dashboard using Raspberry Pis.  This would help me manage them.  The core is a basic CRUD app for the Pis and locations.  You coud then deploy the Pis to different locations.  Once deployed, the Pis would check in via script and download any changes that were pending, a new URL to display for example.  You could also connect to the Pi to perform maintenance.  I accomplished this via a reverse proxy.  It woked, but could have been better implemented.  The scripts have been lost to time but I plan on recreating them once the web app is ready.

While the original ASP.net app was functionally complete, this one is far from it.  I have many features left to build.  It is one of those projects where I have no use for the app but its helping me build my Django skills.  

To run the app:

Create your virtual envrionment (optional, but recommended):

```
mkvirtialenv rpmanager
```

Install the dependencies:

```
pip install -r requirements.txt
```

Run the server:

```
py manage.py runserver
```
