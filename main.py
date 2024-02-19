from flask import Flask, request
from segmenter import Segmenter
from data import Data
import logging
#logging configuration
logging.basicConfig(datefmt='%H:%M:%S',
                    level=logging.DEBUG)


app = Flask(__name__)
	
@app.route('/segmenter-01', methods = ['GET', 'POST'])
def segmenter_defult():
	if request.method == 'POST':
		file_obj = request.files['file']
		f_name = Data(file_obj)
		segmenter = Segmenter()
		result=segmenter.segmenter_default(f_name)
		return result
	if request.method == 'GET':
		info = (
			"""Segmenter is an AMF compononet that segments arguments into propositions.
			This is the default implmentation of a segmenter that uses simple regex.
			It takes xIAF as an input to return xIAF as an output.
			The component can be conected to propositionUnitizer to create argument mining pipeline."""
			)
		return info

	
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5005"), debug=False)	  
