                                                    IEP_Task
                                                    
Task: Generating letters, forms and documents prefilled from FHIR records (Word and PDF) 

This package is a simple solution for generating a single, extensive document regarding all relevant patient details. 

Designed to quickly provide an easily digestible information report for patients in emergency situations where doctors
and nurses require several different types of patient details without the time to manually sift through irrelevant details.

Dependencies & packages:The package utilizes Ethan Wood's FHIR Parser and requires LibreOffice to be installed on the users 
machine in order to convert from Word to PDF file formats; LibreOffice is an office suite, much like Microsoft Office, that 
comprises programs for word processing. The reason I chose to use LibreOffice is because unlike its competitors, LibreOffice 
is free and open source, making it ideal for use at government hospitals. 

Running the program: Running the program is simple and straightforward: simply running the file 'API.py' is enough. Following,
the message '* Running on http://127.0.0.1:5002/ (Press CTRL+C to quit)' should display on the user's terminal. Clicking on 
that link will redirect the user to my website UI, which can then be used to access my API. This syle makes the program robust and easily implementable to any existing system because of the duality of its nature. 

Using the website: In order to ease usability, I chose to develop both a local-host and an API. Users are initially automatically directed to the website, where they can directly input a user's universally unique identification (UUID) and generate either Word or PDF documents through a simply user interface. Clicking either button will prompt an automatic download.

Using the API: Alternativly, to connect the API, a user can go to the 'http://127.0.0.1:5002/patient?uuid=' followed by the requested patients UUID to access the API directly. Following, the API should prompt an automatic download. 
