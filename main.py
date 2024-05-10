from flask import Flask, request
from prometheus_flask_exporter import PrometheusMetrics

from src.segmenter import Segmenter
from src.data import Data
from src.utility import handle_errors

import logging
logging.basicConfig(datefmt='%H:%M:%S',
                    level=logging.DEBUG)

app = Flask(__name__)
metrics = PrometheusMetrics(app)
	
@app.route('/segmenter-01', methods = ['GET', 'POST'])
@metrics.summary('requests_by_status', 'Request latencies by status',
                 labels={'status': lambda r: r.status_code})
@metrics.histogram('requests_by_status_and_path', 'Request latencies by status and path',
                   labels={'status': lambda r: r.status_code, 'path': lambda: request.path})
@handle_errors  
def segmenter_defult():
	if request.method == 'POST':
		file_obj = request.files['file']
		segmenter = Segmenter(file_obj)
		result=segmenter.segmenter_default()
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
