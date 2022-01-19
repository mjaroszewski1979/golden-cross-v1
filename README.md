## Digital Gold
### This is a Python application powered by Django and its Object-Relational Mapper to show trading signals based on mathematical algorithm, that indicates it is a good time to buy or sell Bitcoin. After fetching data from Yahoo Finance API and calculating current trend direction using 252 days lookback period - approximately 1 year - the results will be displayed in form of a table. 

--------------------------------------------------

### Features:
* Integrating MailChimp API with the application to provide a platform to receive emails from the audience who subscribes to our website
* Utilizing Technical Analysis Library for efficient process of data manipulation widely used in quantitative finance
* Connecting to Yahoo Finance API using pandas datareader to ensure the highest quality when importing historical time series
* Working with template inheritance mechanism to build a base “skeleton” template that contains all the common elements and defines blocks that child templates can override
* Taking full advantage of Django's built-in features like cross-site request forgery protection to ensure safe data transfer in web forms to a database
* Breaking logic into smaller parts by adding various new Django applications to an existing project 
* Writing as much functionality as possible in models or utility files instead of views 
* Storing app’s secure credentials in environment variables

--------------------------------------------------

### Code Coverage:
* Selenium and unit tests combined

```
coverage run -p manage.py test gold && coverage run -p manage.py test tests_selenium && coverage combine && coverage html

```

<img src="https://github.com/mjaroszewski1979/golden-cross-v1/blob/main/cov_report.png">

------------------------------------------------

### Docker info:
* Pull an image from my Docker Hub - click on the icon below
* Create and start a container 
* Pass environment variables to your container
  * with the -e flag or using .env file

```
docker run -p 8000:8000 -e MAILCHIMP_API_KEY="<your api key>" -e MAILCHIMP_DATA_CENTER="<the last 4 characters of your api key e.g. us20>" -e MAILCHIMP_EMAIL_LIST_ID="<your audience id>" <imagename>

```
```
docker run -p 8000:8000 --env-file .env <imagename>

```

--------------------------------------------------


![caption](https://github.com/mjaroszewski1979/golden-cross-v1/blob/main/dg_mockup.png)
  
  Live | Code | Docker | Technologies
  ---- | ---- | ------ | ------------
  [<img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/pyan1.png">](http://taurustrading.pythonanywhere.com/) | [<img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/github_g.png">](https://github.com/mjaroszewski1979/golden-cross-v1) | [<img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/docker_g.png">](https://hub.docker.com/r/maciej1245/digital-gold) | <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/python_g.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/django_g.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/pandas.png"> <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/html_g.png"> <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/css_g.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/htmlup.png"> &nbsp; &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/js1.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/chimp.png"> 
