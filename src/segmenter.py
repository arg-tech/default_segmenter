"""This file provides a simple segmenter that splits texts based on regex. 
The default segmenter takes xAIF, segments the texts in each L-node, 
introduces new L-node entries for each of the new segments, and deletes the old L-node entries.
"""

import re
from flask import json
import logging
from src.data import Data,AIF
from src.templates import SegmenterOutput
logging.basicConfig(datefmt='%H:%M:%S',
                    level=logging.DEBUG)

class Segmenter():
	def __init__(self,file_obj):
		self.file_obj = file_obj
		self.f_name = file_obj.filename
		self.file_obj.save(self.f_name)
		file = open(self.f_name,'r')

		
	def get_segments(self, input_text):
		"Simple segementer spliting texts based on regex."
		return re.split("[.!?]",input_text)
	
	def is_valid_json(self):
		''' check if the file is valid json
		'''

		try:
			json.loads(open(self.f_name).read())
		except ValueError as e:			
			return False

		return True
	def is_valid_json_aif(sel,aif_nodes):
		if 'nodes' in aif_nodes and 'locutions' in aif_nodes and 'edges' in aif_nodes:
			return True
		return False
		

	def get_aif(self, format='xAIF'):
		if self.is_valid_json():
			with open(self.f_name) as file:
				data = file.read()
				x_aif = json.loads(data)
				if format == "xAIF":
					return x_aif
				else:
					aif = x_aif.get('AIF')
					return json.dumps(aif)
		else:
			return "Invalid json"

	def segmenter_default(self,):
		"""The default segmenter takes xAIF, segments the texts in each L-nodes,
		introduce new L-node entries for each of the new segements and delete the old L-node entries
		"""
		aif = AIF()


		
		is_json_file = True
		if is_json_file:				
			x_aif = self.get_aif()
			json_dict = x_aif['AIF']
			if self.is_valid_json_aif(json_dict):
				nodes, locutions, edges, participants = json_dict['nodes'], json_dict['locutions'], json_dict['edges'], json_dict.get("participants",[])
				old_nodes = nodes.copy()			
				for nodes_entry in old_nodes:
					node_id = nodes_entry['nodeID']
					node_text = nodes_entry['text']
					type = nodes_entry['type']
					if type == "L":
						segments = self.get_segments(node_text)
						segments = [seg.strip() for seg in segments if len(seg.strip()) > 1]
						if len(segments) > 1:
							for segment in segments:								
								if segment != "":	
									nodes,locutions, edges = self.add_entry(nodes,
												 locutions,
												 edges,
												 participants,
												 node_id,
												 segment)										
							nodes, edges, locutions  = aif.remove_entries(node_id, nodes, edges, locutions)

				return x_aif
			else:
				return("Invalid json-aif")
		else:
			return("Invalid input")
	






  
