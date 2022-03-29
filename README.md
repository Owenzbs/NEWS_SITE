# NEWS_SITE

You'll need to have Docker installed. It's available on Windows, macOS and most distros of Linux. If you're new to Docker and want to learn it in detail check out the additional resources links near the bottom of this README.



Clone this repo anywhere you want and move into the directory:
git clone https://github.com/Owenzbs/NEWS_SITE.git

Build everything:

On the command line, within this directory, do this to build the image and start the container:

 docker-compose build
 
If that's successful you can then start it up. This will start up the database and web server, and display the Django runserver logs:

 docker-compose up
 
Open http://0.0.0.0:8000 in your browser.
