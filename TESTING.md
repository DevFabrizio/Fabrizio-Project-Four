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

| Test case | Test Description                                 | Pass / Fail  | Steps to Reproduce                                                                                                                     | Error | Note                                                                                      |
|-----------|--------------------------------------------------|--------------|----------------------------------------------------------------------------------------------------------------------------------------|-------|-------------------------------------------------------------------------------------------|
| 001       | Ability to browse the website pages              | Pass         | Once landed on the main page the user clicks on any of the links in the nav-bar and gets redirected to the selected page               |       |                                                                                           |
| 002       | Ability to register to the website               | Pass         | Pass Test 001, click on the "Signup" link, fill the form and submit                                                                    |       | The info in the form will be registred in the database                                    |
| 003       | Ability to Log in                                | Pass         | Pass test 002, click on the "Log-in" link, fill the form with the account info and click the submit button                             |       | Once logged in the  username will be displayed in the nav-bar                             |
| 004       | Ability to Log out                               | Pass         | Pass test 002 and 003, click on the "Log-out" link in the nav-bar and confirm the decision by clicking the "sign-out" button           |       |                                                                                           |
| 005       | Ability to book a table as a non registered user | Pass         | Click the "Book a Table" link in the nav bar, fill the form with the info for your booking, submit the booking                         |       | The booking will be stored in the database                                                |
| 006       | Ability to book a table as a logged in user      | Pass         | Pass test 002 and 003, click on the "book a table" link in the nav bar, fill the form with the info for your reservation and submit it |       | The booking will be stored in the database and the user will get a confirmation message   |
| 007       | Ability to view the reservations                 | Pass         | Pass tests 002 003 006, click on "My reservations" link in the nav bar.                                                                |       | Functionality reserved for logged in users                                                |
| 008       | Ability to edit the reservation                  | Pass         | Pass tests 002 003 006 007, click on the "Edit" button Modify the form with the corrections and submit                                 |       | The new reservation will substitute the old one in the database                           |
| 009       | Ability to delete the reservation                | Pass         | Pass tests 002 003 006 007, click on the "Delete" button. Confirm deletion by clicking on the "Delete" button again.                   |       | The reservation will be deleted from the database                                         |
| 010       | Ability to access the maps section               | Pass         | Once on the main page, click the GPS icon which functions  as a link in the footer                                                     |       |                                                                                           |
| 011       | Ability to access the website as an admin        | Pass         | Pass tests 001 003                                                                                                                     |       | The admin account has to be granted by the superuser who has the original admin privilege |
| 012       | Ability to see all the reservations as an admin  | Pass         | Pass tests 011 003 007                                                                                                                 |       |                                                                                           |
| 013       | Ability to edit the reservations as an admin     | Pass         | Pass tests 011 012 008                                                                                                                 |       |                                                                                           |
| 014       | Ability to delete the reservations as an admin   | Pass         | Pass tests 011 012 009                                                                                                                 |       |                                                                                           |
| 015       | Verify confirmations message JS effect           | Pass         | Pass tests 005 or 006, observe the success message disappear after the set time.                                                       |       | This is the only JS test                                                                  |

### Google DevTools Lighthouse reports

The following table contains the results for the lighthouse reports for all html templates in mobile and desktop size

| Lighthouse Report               | Performance | Accessibility | Best Practices | SEO |   |   |   |
|---------------------------------|-------------|---------------|----------------|-----|---|---|---|
| Main Page (mobile)              | 34          | 100           | 83             | 92  |   |   |   |
| Main Page (desktop)             | 69          | 100           | 83             | 90  |   |   |   |
| Reservations Page (mobile)      | 71          | 98            | 92             | 91  |   |   |   |
| Reservations Page (desktop)     | 86          | 98            | 92             | 89  |   |   |   |
| User Bookings Page (mobile)     | 71          | 90            | 92             | 91  |   |   |   |
| User Bookings Page (desktop)    | 98          | 90            | 92             | 89  |   |   |   |
| Logout Page (mobile)            | 77          | 100           | 92             | 91  |   |   |   |
| Logout Page (desktop)           | 97          | 100           | 92             | 89  |   |   |   |
| Login Page (mobile)             | 64          | 100           | 92             | 91  |   |   |   |
| Login Page (desktop)            | 95          | 100           | 92             | 89  |   |   |   |
| Signup Page (mobile)            | 72          | 100           | 92             | 91  |   |   |   |
| Signup Page (desktop)           | 97          | 100           | 92             | 89  |   |   |   |
| Booking Page (mobile)           | 74          | 90            | 92             | 91  |   |   |   |
| Booking Page (desktop)          | 98          | 90            | 92             | 89  |   |   |   |
| Maps Page (mobile)              | 61          | 97            | 83             | 91  |   |   |   |
| Maps Page (desktop)             | 91          | 97            | 83             | 89  |   |   |   |
| Confirm Delete Page (mobile)    | 71          | 100           | 92             | 91  |   |   |   |
| Confirm Delete Page (desktop)   | 97          | 100           | 92             | 89  |   |   |   |
| Edit Reservation Page (mobile)  | 73          | 100           | 92             | 91  |   |   |   |
| Edit Reservation Page (desktop) | 89          | 100           | 92             | 89  |   |   |   |