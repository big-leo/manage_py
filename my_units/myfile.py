class MyFile(object):
    """file for diff
    name - all name with path
    path - parent folder
    hash - field for compare"""

    def __init__(self, path, name, hash):
        self.path = path
        self.name = name
        self.hash = hash
