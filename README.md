## Digital Gold
### This is a Python application built with Django and its Object-Relational Mapper that is designed to display trading signals based on a mathematical algorithm. The algorithm determines the ideal time to buy or sell Bitcoin. The application fetches data from the Yahoo Finance API and calculates the current trend direction using a 252-day lookback period which is approximately one year. 

Once the calculations are complete, the results are presented in a user-friendly table format. This application is ideal for traders who are looking to make data-driven decisions when it comes to buying or selling Bitcoin. With the help of the algorithm, the application can analyze large amounts of data and provide recommendations on when to make a move. Additionally, the user-friendly table format makes it easy for traders to understand the data and take appropriate actions.

--------------------------------------------------

### Features:

* By integrating **MailChimp** with our application, we're be able to provide a platform for potential audience to subscribe to our website and receive regular emails. This can be a powerful tool for keeping your audience engaged and informed about your latest offerings. This not only keeps our clients up-to-date with our latest news and offerings, but it also creates a more personal connection with them. This can ultimately lead to more conversions and a stronger relationship. MailChimp is a powerful tool that allows us to easily create and manage email campaigns. 

With its user-friendly interface and extensive features, we can customize our emails and make them more engaging for our audience. This includes adding images, videos, and other multimedia elements that can help to make our emails more visually appealing. Furthermore, MailChimp provides analytics and reports that can help us track the success of our email campaigns. This includes information about open rates, click-through rates, and conversions. By analyzing this data, we can make informed decisions about how to improve our campaigns and better engage with our audience.
* **Technical Analysis Library** is specifically designed for data manipulation in quantitative finance, making it the perfect tool for anyone who needs to analyze and make sense of large sets of financial data. Whether you're a trader, analyst, or investor, this library can help you to quickly and easily analyze trends, identify patterns, and make informed decisions. With Technical Analysis Library, you'll be able to process data faster and more efficiently than ever before. You'll be able to take advantage of a wide range of advanced statistical tools and techniques, including moving averages, relative strength index, and more. Plus, this library is designed to be user-friendly, even for those who may not be technical experts.
* When it comes to accessing historical financial data, it's essential to ensure that you're using a reliable source. One way to do this is by connecting to the Yahoo Finance API using **Pandas Datareader**. This Python library allows you to retrieve financial data from a variety of sources and provides a convenient interface for working with time series data. By using pandas datareader to access the Yahoo Finance API, you can be confident that the data you're working with is accurate and up-to-date. 

This is important because even small errors in financial data can have significant consequences. The pandas datareader library is widely used in the finance industry and has a number of useful features that make it an ideal choice for working with time series data. For example, it supports a wide range of data sources, including Yahoo Finance, Google Finance, and Federal Reserve Economic Data (FRED).
* One of the key tasks of a proficient software developer is to create a user interface that is not only visually appealing but also easy to use. One way to achieve this is through the use of template inheritance mechanism. Template inheritance mechanism involves building a base "skeleton" template that contains all the common elements and defines blocks that child templates can override. This approach saves time by avoiding the need to recreate common elements in each template. With this technique, it is possible to create a consistent and cohesive design for a website or application. Moreover, if there are any updates or changes needed, it can be done easily and quickly as they only need to be made in the base template. In addition, this mechanism can also enhance code readability and maintainability. By having a central location for common elements, it is easier to manage and modify the code.
* As a developer, you may often find yourself working with web forms and databases. One important aspect to consider is the safety of data transfer. Fortunately, Django, a popular web framework, has built-in features that can help ensure the security of your web forms. One such feature is cross-site request forgery (CSRF) protection. CSRF is an attack where a malicious website tricks a user into submitting a request to a different website that the user is logged into. This can lead to unintended actions being performed on the user's behalf. Django's CSRF protection helps prevent this type of attack by adding a hidden CSRF token to each form that is submitted. The token is validated on the server side to ensure that the request was indeed initiated by the user. By taking full advantage of Django's built-in features like CSRF protection, you can help ensure the safe transfer of data from web forms to a database. This can help prevent unauthorized access to sensitive information and protect the integrity of your application.
* Breaking down logic into smaller, manageable parts is crucial to ensuring the success of any project. One way to achieve this is by adding various new Django applications to an existing project. By creating smaller, more focused applications within a larger project, developers can improve code organization, maintainability, and scalability. Each application can handle a specific task or feature of the project, such as user authentication, data management, or payment processing. This approach can also make it easier to debug and test individual parts of the codebase. When adding new applications to an existing Django project, it's important to consider the functionality and purpose of each application. Each application should be responsible for a specific feature or function within the project, making it easier to modify and maintain the codebase in the long run. However, it's important to keep in mind that adding too many applications can also have drawbacks. It can increase the complexity of the codebase and slow down the overall performance of the project. Therefore, it's crucial to strike a balance between breaking down the logic of the project and keeping it manageable.
* One way to achieve clean and maintainable code is by writing as much functionality as possible in Django models or utility files instead of views. Django allows developers to separate their application's logic into three main components: models, views, and templates. While views are responsible for handling user requests and returning responses, models define the structure of the application's data and provide an interface for interacting with it. By writing as much functionality as possible in models or utility files, developers can improve the maintainability and organization of their codebase. This approach helps to keep views lean and focused on their primary responsibilities, improving code readability and making it easier to debug and maintain. Furthermore, writing functionality in models or utility files can also improve the performance of the application. Since models and utility files are loaded only once when the application starts up, the cost of loading and processing is spread out over the lifetime of the application.
* Understanding the importance of keeping sensitive information secure, we always store API keys, database passwords, and other credentials in environment variables. Environment variables are values that can be set in the operating system and accessed by applications. By storing sensitive information in environment variables, developers can keep this information separate from the codebase, reducing the risk of accidental exposure. Storing sensitive information in environment variables also makes it easier to manage and maintain credentials across multiple environments. Rather than hard-coding credentials into the application, environment variables can be set differently for each environment, such as development, staging, and production. This helps to ensure that sensitive information is not accidentally exposed in a non-production environment. However, it's important to keep in mind that environment variables are not a foolproof security measure. They are still vulnerable to potential security breaches if not properly secured or if accessed by unauthorized users. Therefore, it's important to follow best practices for securing sensitive information, such as using strong passwords, limiting access to credentials, and regularly monitoring and auditing access to environment variables. 
* Writing efficient and fast tests is essential for a successful project. In Django, one way to optimize tests is by utilizing the setUp method to handle especially expensive setup operations for all of the tests within a module. The setUp method is a method that is called before each test in a module. It is used to set up any test data or other resources needed for the tests. By using the setUp method to handle expensive setup operations, such as creating database records or generating test data, we can save time and resources in our test suite. Using the setUp method not only saves time, but it also makes our tests more reliable. By setting up the necessary data and resources before each test, we ensure that our tests are always running with the correct environment and data. This helps to prevent false positives or negatives in our test results, which can be time-consuming and frustrating to debug. However, it's important to keep in mind that the setUp method should be used judiciously. While it can be tempting to use the setUp method to handle all setup operations, doing so can actually slow down our tests. This is because the setUp method is called before each test, and if it is too complex or time-consuming, it can add significant overhead to our test suite.
* When it comes to software testing, it's essential to ensure that the code is clean, efficient, and easy to understand. One way to achieve this is by utilizing the 'page object pattern' while conducting extensive selenium tests instead of using raw WebDriver calls. The page object pattern allows for a cleaner codebase by following the DRY (Don't Repeat Yourself) principle, where all ID-locators are in one place. This practice minimizes code duplication and makes maintenance and updates more manageable. Another advantage of the page object pattern is that it sets up an interface between web page elements and tests. This separation helps to avoid the usage of WebDriver APIs in test methods, making the tests more robust and less prone to failure. Additionally, encapsulating the services of web pages, rather than exposing their elements, leads to better test organization and helps to prevent code duplication. Overall, using the page object pattern can help to streamline your selenium testing process and result in a more efficient, effective, and maintainable codebase.

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
