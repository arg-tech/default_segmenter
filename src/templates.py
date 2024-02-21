import json

class SegmenterOutput:
    @staticmethod
    def format_output(nodes, edges, locutions):
        json_aif = {
            'nodes': nodes,
            'edges': edges,
            'locutions': locutions
        }
        x_aif = {'AIF': json_aif}
        return json.dumps(x_aif)
