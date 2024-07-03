## Project Requirements Document for Digital Gold

### Unit Tests

Requirement | Condition | Expected Outcome | Test Case
----------- | --------- | ---------------- | ---------
The application must correctly resolve the URL for the index view. | When the reverse('index') function is called. | The resolved URL should map to the index view function. | test_index_url_is_resolved
The application must correctly resolve the URL for the success view. | When the reverse('success') function is called. | The resolved URL should map to the success view function. | test_success_url_is_resolved
The index view must handle GET requests correctly. | When a GET request is made to the index URL. | The response should have a status code of 200, use the index.html template, and include a non-null bitcoin context variable. The response must contain the text 'Digital Gold Home'. | test_index_get
The index view must handle POST requests correctly. | When a POST request with valid data is made to the index URL. | The response should have a status code of 200 and contain the text 'Digital Gold Success'. The response must include the message 'Thank you for your email.' | test_index_post
The success view must handle GET requests correctly. | When a GET request is made to the success URL. | The response should have a status code of 200 and use the success.html template. The response must contain the text 'Digital Gold Success'. | test_success_get
The application must handle non-existent URLs correctly. | When a GET request is made to a non-existent URL. | The response should have a status code of 404 and use the 404.html template. The response must contain the text 'Digital Gold Page not found'. | test_handler404
The Bitcoin model must correctly persist and retrieve data from the database. | When a new Bitcoin instance is created and saved. | The model should correctly store and retrieve properties including dema, ema, ht, kama, sar, sma, trima, wma, and date_added. The total count of Bitcoin objects in the database should reflect the new addition. The string representation of the Bitcoin object should match the title. | test_bitcoin_model

### Selenium Tests

Requirement | Condition | Expected Outcome | Test Case
----------- | --------- | ---------------- | ---------
The homepage must have the title "Digital Gold Home". | When the index page is accessed. | The title should contain "Digital Gold Home". | is_title_matches
The index page must display the correct heading. | When the index page is accessed. | The heading should contain "DIGITAL GOLD". | is_index_heading_displayed_correctly
The intro link must navigate to the correct section. | When the intro link is clicked. | The intro heading should contain "BITCOIN IS A DECENTRALIZED". | is_intro_link_works
The intro section must close and return to the index heading when the close button is clicked. | When the intro close button is clicked. | The heading should revert to "DIGITAL GOLD". | is_intro_close_button_works
The signals link must navigate to the correct section. | When the signals link is clicked. | The signals heading should contain "BTC/USD TECHNICAL SIGNALS". | is_signals_link_works
The signals section must close and return to the index heading when the close button is clicked. | When the signals close button is clicked. | The heading should revert to "DIGITAL GOLD". | is_signals_close_button_works
The about link must navigate to the correct section. | When the about link is clicked. | The about heading should contain "TECHNICAL ANALYSIS IS A RESEARCH". | is_about_link_works
The about section must close and return to the index heading when the close button is clicked. | When the about close button is clicked. | The heading should revert to "DIGITAL GOLD". | is_about_close_button_works
The contact link must navigate to the correct section. | When the contact link is clicked. | The subscribe paragraph should contain "Subscribe to our CryptoStrategy eNewsletter". | is_contact_link_works
The subscribe form must accept email input and display a success message upon submission. | When an email is entered and the form is submitted. | The success message should contain "Thank you for your email." | is_subscribe_form_works

