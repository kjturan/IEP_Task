                                                    IEP_Task
                                                    
Task: Generating letters, forms and documents prefilled from FHIR records (Word and PDF) 

This package is a simple solution for generating a single, extensive document collecting all relevant patient details from FHIR records. 

- Please check out my short demonstrator for how the system works: https://youtu.be/v8_ohQLqccI

In emergency situations where doctors and nurses require patient details from seveal different documents without the time to manually sift through irrelevant details, gathering the revelant information and displaying it in a clear and efficent manner is key. On that note, I developed a package that was designed with the intent of quickly providing an easily digestible information report for a patient (given his/her UUID). Whether it be in an ambulance, an emergency unit or a doctor's office, this package quickly pulls all relevant information about a patient to speed up the diagnostic process so that doctors and nurses can start acting faster and with greater confidence. 

To accomplish this goal, I designed a simple website UI, which can then be used to access my API. This style makes the program robust and easily implementable to any existing system because of the duality of its nature: 

- The website is for those who simply want to use the program in their office or clinic: they can simply input data in the website’s search bar to get the desired     results in the format they request.

- On the other hand, for more critical situations such as emergency care units, ambulances, and emergency rooms where time is time and patience is limited, the API   can be far more useful. Inputting the user’s UUID is enough to prompt the document download; there are no buttons to press or forms to fill. This makes the API     ideal for remote use in the form of wearable technologies or hand-held id scanners. 

Core Dependencies: The package relies on the FHIR API. Patient data is retrieved over FHIR from a GOSH gateway. Furthermore, the package utilizes Ethan Wood's FHIR Parser and requires LibreOffice to be installed on the users machine in order to convert from Word to PDF file formats; LibreOffice is an office suite, much like Microsoft Office, that comprises programs for word processing. The reason I chose to use LibreOffice is because unlike its competitors, LibreOffice is free and open source, making it easily accesible.

Running the program: Running the program is simple and straightforward: simply running the file 'API.py' is enough. Following,
the message `* Running on http://127.0.0.1:5002/ (Press CTRL+C to quit)` should display on the user's terminal. Clicking 
that link redirect sthe user to the localhost, which can then be used to access my API. This syle makes the program robust and easily implementable to any existing system because of the duality of its nature. 

Using the API: Alternativly, to connect to the API directly, a user can go to the `http://127.0.0.1:5002/patient?uuid=` followed by the requested patients UUID to access the API directly. Following, the API should prompt an automatic download. 
