import os
import hashlib
from collections import defaultdict

def listfiles(top, includes=(), excludes=[]):
    """
    Lists all files in all folders inside a root (top) folder.
    :param top:         root folder
    :param includes:    tuple of included extenstions. e.g ('.doc', '.exe')
    :param excludes:    list of subfolders to be excluded
    :return:            list of tuples. e.g. [('filename.ext', 'filepath')]
    """
    #list_of_items = []
    for root, dir, files in os.walk(top):
        if not root in excludes:
            for filename in files:
                item = None
                if includes:
                    if filename.endswith(includes):
                        filepath = os.path.join(root, filename)
                        item = (filename, filepath)
                else:
                    filepath = os.path.join(root, filename)
                    item = (filename, filepath)
            #list_of_items.append(item)
                if item:
                    yield item
    #return list_of_items

def hashfile(fname, hasher, blocksize=65536):
    """
    http://stackoverflow.com/questions/3431825/generating-a-md5-checksum-of-a-file

    :param afile:
    :param hasher:      e.g. hashlib.sha256()
    :param blocksize:
    :return:
    """

    with open(fname, 'rb') as afile:
        buf = afile.read(blocksize)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(blocksize)
    return hasher.digest()

def hash_items(list_of_items):
    """
    
    :param list_of_items: 
    :return:
    """
    items = []
    for filename, filepath in list_of_items:
        hash_string = hashfile(filepath, hashlib.sha256())
        item = (filename, filepath, hash_string)
        items.append(item)
        yield item
    #return items

def list_duplicates(items):
    """

    :param items:
    :return:
    """
    d = defaultdict(list)
    for filename, filepath, hashcode in items:
        d[hashcode].append(filepath)

    for hashcode, filelist in d.items():
        if len(filelist) == 1:
            del d[hashcode]
    return d

if __name__ == "__main__":
    # Find all files
    folder = '/home/prashanth/PycharmProjects/deduplicator/test_folder'

    includes = ('.doc', '.txt')
    excludes = ['/simple_choice_game',]

    items = listfiles(folder, includes=includes, excludes=excludes)
    print list_duplicates( hash_items(items))

    #for root, dir, files in os.walk(folder):
    #    for file in files:
    #        if file.endswith(includes):
    #            print file, root
    #            print os.path.join(root, file)
        #for directory in dir:
        #    if not directory in excludes :
        #        print directory

