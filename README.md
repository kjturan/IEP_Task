                                                    IEP_Task
                                                    
Task: Generating letters, forms and documents prefilled from FHIR records (Word and PDF) 

This package is a simple solution for generating a single, extensive document regarding all relevant patient details. 

Designed to quickly provide an easily digestible information report for patients in emergency situations where doctors
and nurses require several different types of patient details without the time to manually sift through irrelevant details.

Dependencies & packages:The package utilizes Ethan Wood's FHIR Parser and requires LibreOffice to be installed on the users 
machine in order to convert from Word to PDF file formats; LibreOffice is an office suite, much like Microsoft Office, that 
comprises programs for word processing. The reason I chose to use LibreOffice is because unlike its competitors, LibreOffice 
is free and open source, making it ideal for use at government hospitals. 

Running the program: Running the program is simple and straightforward. The user will be prompted to provide a patient's 
universally unique identification (UUID), which is a unique identifier for each patient. This also ensures the systems 
security. Following, a short series of concise questions with single character inputs allows for quick access to the 
necissary information. All prompts and inputs are done through terminal commands, making the API robust and easily 
implementable to any existing system.





 

