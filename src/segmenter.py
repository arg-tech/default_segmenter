"""This file provides a simple segmenter that splits texts based on regex. 
The default segmenter takes xAIF, segments the texts in each L-node, 
introduces new L-node entries for each of the new segments, and deletes the old L-node entries.
"""

import re
from flask import json
import logging
from data import Data,AIF
from templates import SegmenterOutput
logging.basicConfig(datefmt='%H:%M:%S',
                    level=logging.DEBUG)

class Segmenter():
	def __init__(self) -> None:
		pass 
		
	def get_segments(self, input_text):
		"Simple segementer spliting texts based on regex."
		return re.split("[.!?]",input_text)

	def segmenter_default(self, file_obj):
		"""The default segmenter takes xAIF, segments the texts in each L-nodes,
		introduce new L-node entries for each of the new segements and delete the old L-node entries
		"""
		data = Data(file_obj)
		path = data.get_file_path()
		is_json_file = Data.is_valid_json()
		if is_json_file:				
			x_aif = AIF.get_aif(path)
			json_dict = x_aif['AIF']
			if AIF.is_valid_json_aif(json_dict):
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
							nodes, edges, locutions  = AIF.remove_entries(node_id, nodes, edges, locutions)

				return SegmenterOutput.format_output(nodes, edges, json_dict, locutions,x_aif)
			else:
				return("Invalid json-aif")
		else:
			return("Invalid input")
	






  
