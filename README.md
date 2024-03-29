# rPiManagerDjango

TODO:

 - Add functionality from original project:
     - Dashboards - Display simple stats  i.e. rPIs checked out, rPIs that haven't communicated in 24 hours
     - rPI settings
     - Upload SSH keys for remote access
 - Add error handling
 - Add comments
 - Add Tests
 - Refactor code as I learn new techniques
 - Ready for deployment
     - Add support for hosting files on Amazon S3 bucket



I first made this project using ASP.net core in 2019.  I pretty much haven't used .net since then so I thought I would recreate it in Django.  I'm still new to Django so the code can be crude at times.  I plan on cleaning the code once I have the major features implemented.

I had the idea to display a dashboard in a medical laboratory to display analytics such as long turn around times or specimens that are waiting for verification.  I would provide the hardware to display the dashboard using Raspberry Pis.  This would help me manage them.  The core is a basic CRUD app for the Pis and locations.  You could then deploy the Pis to different locations.  Once deployed, the Pis would check in via script and download any changes that were pending, a new URL to display for example.  You could also connect to the Pi to perform maintenance.  I accomplished this via a reverse proxy.  It worked, but could have been better implemented.  The scripts have been lost to time but I plan on recreating them once the web app is ready.

While the original ASP.net app was functionally complete, this one is far from it.  I have many features left to build.  It is one of those projects where I have no use for the app but its helping me build my Django skills.  

To run the app:

Create your virtual environment (optional, but recommended):

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
