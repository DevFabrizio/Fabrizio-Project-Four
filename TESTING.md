# Testing the Project

This is the file dedicated to the tests ran agianst the project to validate and confirm the functionalities added. The tables in this file were used to continually check the code written in order to implement the functionalities required by the project goals. 

### Validation 

This is the table used to check the validity of the code and various django templates during the development of the project.

| Table of Validation | Pass | Fail | Errors                                                                                                                                                                                                                                                                 |
|---------------------|------|------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CSS                 | Yes  |      |                                                                                                                                                                                                                                                                        |
| HTML                |      | yes  | After correction of some minor mistakes all the errors attributed to the various templates are due to the use of the django template language                                                                                                                          |
| JavaScript          | Yes  |      |                                                                                                                                                                                                                                                                        |
| Python              |      | Yes  | The error only error is located in the settings.py file. This is due to a value being too long.  When the value is reformatted to fit the pyhton linter standards it interrupts the Heroku build process for deployment. Hence my decision to maintain it as an error. |

### Manual Testing