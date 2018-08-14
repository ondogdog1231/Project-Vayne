"""
1. Create Folder
2. Save article
"""


class contentSaver():
    def __init__(self,savePath):
        self.filePath = savePath
    def save(self,token,content):
        print "save"