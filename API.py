import docx
import datetime
from Utils import *
from dateutil.relativedelta import *
from flask import Flask, jsonify, send_from_directory, render_template
from flask_restful import Api, Resource, request
from fhir_parser.fhir import FHIR 

app = Flask(__name__)
api = Api(app)
UPLOAD_DIRECTORY = '/Users/user/Desktop/IEP/'
    
@app.route('/', methods=['GET','POST'])
def home():
    return render_template('index.html')

@app.route('/result', methods = ['POST', 'GET'])
def down():
    if request.method == 'POST':
        form_dict = request.form
        patient = fhir.get_patient(form_dict['Patient UUID'])
        observations = fhir.get_patient_observations(patient.uuid)
        doc_name = write_word(patient,observations)
        if 'pdf' in form_dict.keys():
            convert_to(UPLOAD_DIRECTORY,doc_name,timeout=15)
            doc_name = doc_name.replace('.docx','.pdf')
        return send_from_directory(UPLOAD_DIRECTORY, doc_name, as_attachment=True)

@app.route('/patient', methods = ['POST', 'GET'])
def data():
    patient_uuid = request.args.get('uuid')
    patient = fhir.get_patient(patient_uuid)
    observations = fhir.get_patient_observations(patient_uuid)
    doc_name = write_word(patient,observations)
    # if 'pdf' in form_dict.keys():
    #     convert_to(UPLOAD_DIRECTORY,doc_name,timeout=15)
    #     doc_name = doc_name.replace('.docx','.pdf')
    return send_from_directory(UPLOAD_DIRECTORY, doc_name, as_attachment=True)

if __name__== "__main__":
    app.run(debug=True, port=5002)
