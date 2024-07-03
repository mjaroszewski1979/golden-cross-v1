## Digital Gold

### This is a Python application built with Django and its Object-Relational Mapper that is designed to display trading signals based on a mathematical algorithm. The algorithm determines the ideal time to buy or sell Bitcoin. The application fetches data from the Yahoo Finance API and calculates the current trend direction using a 252-day lookback period which is approximately one year. 

#### Once the calculations are complete, the results are presented in a user-friendly table format. This application is ideal for traders who are looking to make data-driven decisions when it comes to buying or selling Bitcoin. With the help of the algorithm, the application can analyze large amounts of data and provide recommendations on when to make a move. Additionally, the user-friendly table format makes it easy for traders to understand the data and take appropriate actions.


### Features:

* Data Fetching: Retrieves financial data from Yahoo Finance API.
* Algorithmic Analysis: Analyzes data to determine buy/sell signals.
* User-Friendly Interface: Displays results in a table format for easy interpretation.
* Email Notifications: Integrates with MailChimp for subscription and email alerts.


### Installation

1. Clone the repository:
  ```bash
  git clone https://github.com/mjaroszewski1979/golden-cross-v1.git
  cd golden-cross-v1
  ```
2. Create a virtual environment:
  ```bash
  python3 -m venv env
  source env/bin/activate
  ```
3. Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```
4. Set up environment variables:
   Create a .env file and add your API keys and other configurations:
  ```
  MAILCHIMP_API_KEY=<your-api-key>
  MAILCHIMP_DATA_CENTER=<data-center>
  MAILCHIMP_EMAIL_LIST_ID=<email-list-id>
  ```
5. Apply migrations and start the server:
  ```bash
  python manage.py migrate
  python manage.py runserver
  ```

### Usage
Access the application: Open your browser and go to http://127.0.0.1:8000/.
View Trading Signals: The application will display trading signals based on the fetched data.

### Testing

1. Run unit tests:
   ```bash
   python manage.py test
   ```
2. Run Selenium tests:
   ```bash
   coverage run -p manage.py test tests_selenium
   ```
3. Run unit tests:
   ```bash
   coverage combine
   coverage html
   ```

### Code Coverage:
* Selenium and unit tests combined

```
coverage run -p manage.py test gold && coverage run -p manage.py test tests_selenium && coverage combine && coverage html

```

<img src="https://github.com/mjaroszewski1979/golden-cross-v1/blob/main/cov_report.png">


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

### Technologies Used
* Django: Web framework for building the application.
* Selenium: For automated browser testing.
* Yahoo Finance API: For fetching financial data.
* MailChimp API: For email notifications.
* Docker: Containerization of the application.

### Contributing
* Fork the repository.
* Create a new branch (git checkout -b feature-branch).
* Make your changes and commit them (git commit -m 'Add new feature').
* Push to the branch (git push origin feature-branch).
* Open a pull request.

### Contact
For questions or feedback, please contact [mjaroszewski1979.](https://github.com/mjaroszewski1979)

-------------------------------------------


![caption](https://github.com/mjaroszewski1979/golden-cross-v1/blob/main/dg_mockup.png)
  
  Live | Code | Docker | Technologies
  ---- | ---- | ------ | ------------
  [<img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/pyan1.png">](http://taurustrading.pythonanywhere.com/) | [<img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/github_g.png">](https://github.com/mjaroszewski1979/golden-cross-v1) | [<img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/docker_g.png">](https://hub.docker.com/r/maciej1245/digital-gold) | <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/python_g.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/django_g.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/pandas.png"> <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/html_g.png"> <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/css_g.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/htmlup.png"> &nbsp; &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/js1.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/chimp.png"> 
