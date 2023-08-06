import json
import sys
import requests
import base64
import string


class SlideScoreResult:
    def __init__(self, dict=None):
        if dict is None:
            self.image_id = 0
            self.image_name = ''
            self.user = None
            self.tma_row = None
            self.tma_col = None
            self.tma_sample_id = None
            self.question = None
            self.answer = None
            return

        self.image_id = int(dict['imageID'])
        self.image_name = dict['imageName']
        self.user = dict['user']
        self.tma_row = int(dict['tmaRow']) if 'tmaRow' in dict else 0
        self.tma_col = int(dict['tmaCol']) if 'tmaCol' in dict else 0
        self.tma_sample_id = dict['tmaSampleID'] if 'tmaSampleID' in dict else ""
        self.question = dict['question']
        self.answer = dict['answer']

        if self.answer[:2] == '[{':
            annos = json.loads(self.answer)
            if len(annos) > 0:
                if hasattr(annos[0], 'type'):
                    self.annotations = annos
                else:
                    self.points = annos
                    
    def toRow(self):
        ret = str(self.image_id) + "\t" + self.image_name + "\t" + self.user + "\t"
        if self.tma_row is not None:
            ret = ret + str(self.tma_row) + "\t" + str(self.tma_col)+"\t" + self.tma_sample_id + "\t"
        ret = ret + self.question + "\t" + self.answer
        return ret

