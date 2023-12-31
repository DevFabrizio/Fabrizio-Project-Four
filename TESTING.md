# Testing the Project

This is the file dedicated to the tests ran against the project to validate and confirm the functionalities added. The tables in this file were used to continually check the code written in order to implement the functionalities required by the project goals. 

### Validation 

This is the table used to check the validity of the code and various django templates during the development of the project.

| Table of Validation | Pass | Fail | Errors                                                                                                                                                                                                                                                                 |
|---------------------|------|------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CSS                 | Yes  |      |                                                                                                                                                                                                                                                                        |
| HTML                |      | yes  | After correction of some minor mistakes all the errors attributed to the various templates are due to the use of the django template language                                                                                                                          |
| JavaScript          | Yes  |      |                                                                                                                                                                                                                                                                        |
| Python              |      | Yes  | The error only error is located in the settings.py file. This is due to a value being too long.  When the value is reformatted to fit the pyhton linter standards it interrupts the Heroku build process for deployment. Hence my decision to maintain it as an error. |

### Manual Testing

This is the comprehensive table to replicate the manual testing of the website's functionalities.

| Test case | Test Description                                 |   | Steps to Reproduce                                                                                                                     | Expected Result                                                                                                           | Note                                                                                      |
|-----------|--------------------------------------------------|---|----------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| 001       | Ability to browse the website pages              |   | Once landed on the main page the user clicks on any of the links in the nav-bar.                                                       | When the user clicks on any of the links on the in the website, they get redirected to the chosen page.                   |                                                                                           |
| 002       | Ability to register to the website               |   | Pass Test 001, click on the "Signup" link, fill the form and submit                                                                    | The website subscription is submitted to the backend.                                                                     | The info in the form will be registred in the database                                    |
| 003       | Ability to Log in                                |   | Pass test 002, click on the "Log-in" link, fill the form with the account info and click the submit button                             | The user gets logged in and redirected to the home page                                                                   | Once logged in the  username will be displayed in the nav-bar                             |
| 004       | Ability to Log out                               |   | Pass test 002 and 003, click on the "Log-out" link in the nav-bar and confirm the decision by clicking the "sign-out" button           | The user gets logged out and is redirected to the home page                                                               |                                                                                           |
| 005       | Ability to book a table as a non registered user |   | Click the "Book a Table" link in the nav bar, fill the form with the info for your booking, submit the booking                         | A new reservations without a  paired user is stored in the backend and the user is notified of the  successful submission | The booking will be stored in the database                                                |
| 006       | Ability to book a table as a logged in user      |   | Pass test 002 and 003, click on the "book a table" link in the nav bar, fill the form with the info for your reservation and submit it | A new reservation with a paired user is stored in the database and the user is notified of the successful submission      | The booking will be stored in the database and the user will get a confirmation message   |
| 007       | Ability to view the reservations                 |   | Pass tests 002 003 006, click on "My reservations" link in the nav bar.                                                                | The logged in user is redirected to the  page where all the reservations made by  the user are shown                      | Functionality reserved for logged in users                                                |
| 008       | Ability to edit the reservation                  |   | Pass tests 002 003 006 007, click on the "Edit" button Modify the form with the corrections and submit                                 | The reservations is updated with the new  information submitted by the user and a  success message is shown.              | The new reservation will substitute the old one in the database                           |
| 009       | Ability to delete the reservation                |   | Pass tests 002 003 006 007, click on the "Delete" button. Confirm deletion by clicking on the "Delete" button again.                   | The selected reservation is deleted and a successful deletion message is shown                                            | The reservation will be deleted from the database                                         |
| 010       | Ability to access the maps section               |   | Once on the main page, click the GPS icon which functions  as a link in the footer                                                     | The user is redirected to the maps page                                                                                   |                                                                                           |
| 011       | Ability to access the website as an admin        |   | Pass tests 001 003                                                                                                                     | The admin is granted access to the website and the username is shown in green on the  nav-bar                             | The admin account has to be granted by the superuser who has the original admin privilege |
| 012       | Ability to see all the reservations as an admin  |   | Pass tests 011 003 007                                                                                                                 | The admin access the reservations page and all the reservations made are shown                                            |                                                                                           |
| 013       | Ability to edit the reservations as an admin     |   | Pass tests 011 012 008                                                                                                                 | The reservation modified by the admin is submitted to the backend and a success message is shown                          |                                                                                           |
| 014       | Ability to delete the reservations as an admin   |   | Pass tests 011 012 009                                                                                                                 | The selected reservation is deleted from  the backend and a success message is shown                                      |                                                                                           |
| 015       | Verify confirmations message JS effect           |   | Pass tests 005 or 006, observe the success message disappear after the set time.                                                       | The success message disappears after 3 seconds on the screen                                                              | This is the only JS test                                                                  |


### Google DevTools Lighthouse reports

The following table contains the results for the lighthouse reports for all html templates in mobile and desktop size

| Lighthouse Report               | Performance | Accessibility | Best Practices | SEO |   |   |   |
|---------------------------------|-------------|---------------|----------------|-----|---|---|---|
| Main Page (mobile)              | 69          | 100           | 83             | 92  |   |   |   |
| Main Page (desktop)             | 75          | 100           | 83             | 90  |   |   |   |
| Reservations Page (mobile)      | 71          | 98            | 92             | 91  |   |   |   |
| Reservations Page (desktop)     | 86          | 98            | 92             | 89  |   |   |   |
| User Bookings Page (mobile)     | 69          | 91            | 83             | 92  |   |   |   |
| User Bookings Page (desktop)    | 91          | 91            | 83             | 90  |   |   |   |
| Logout Page (mobile)            | 63          | 100           | 83             | 92  |   |   |   |
| Logout Page (desktop)           | 97          | 100           | 83             | 90  |   |   |   |
| Login Page (mobile)             | 43          | 100           | 83             | 92  |   |   |   |
| Login Page (desktop)            | 98          | 100           | 83             | 90  |   |   |   |
| Signup Page (mobile)            | 64          | 100           | 83             | 92  |   |   |   |
| Signup Page (desktop)           | 84          | 100           | 83             | 90  |   |   |   |
| Booking Page (mobile)           | 69          | 91            | 83             | 92  |   |   |   |
| Booking Page (desktop)          | 95          | 91            | 83             | 90  |   |   |   |
| Maps Page (mobile)              | 61          | 97            | 83             | 91  |   |   |   |
| Maps Page (desktop)             | 91          | 97            | 83             | 89  |   |   |   |
| Confirm Delete Page (mobile)    | 71          | 100           | 92             | 91  |   |   |   |
| Confirm Delete Page (desktop)   | 97          | 100           | 92             | 89  |   |   |   |
| Edit Reservation Page (mobile)  | 73          | 100           | 92             | 91  |   |   |   |
| Edit Reservation Page (desktop) | 89          | 100           | 92             | 89  |   |   |   |
