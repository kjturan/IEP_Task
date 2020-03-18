import sys
import subprocess
import re
import docx
from Utils import *
from datetime import datetime
from dateutil.relativedelta import *
from tkinter import *
from flask import Flask
from flask_restful import Api, Resource
from fhir_parser.fhir import FHIR 

fhir = FHIR()
loop = True
while loop:
    patient_UUID = input('Patient UUID: ')
    try:
        patient = fhir.get_patient(patient_UUID)
    except:
        print('Unable to find patient with UUID ' + patient_UUID)
        continue
    observations = fhir.get_patient_observations(patient.uuid)
    docx_name = write_word(patient,observations)
    print('Patient details written to \'' + docx_name + '\'')
    selection = input('Would you like a PDF copy? (Y/N) ')
    if selection == 'P':
        convert_to('/Users/user/Desktop/IEP',docx_name,timeout=15)
        print('Patient details written to \'' + doc_name_gen(patient) + '.pdf\'') 
    cont = input('Do you wish to continue with another patient? (Y/N) ')
    if cont == 'N':
        break

#'8f789d0b-3145-4cf2-8504-13159edaa747'