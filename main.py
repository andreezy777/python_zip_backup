import os, time, zipfile
from os.path import basename

# python script for backup data to .zip-archive
#
#
#
# v 0.1 by Andrew Vasylyna
#

dirFrom = '/Users/andreezy/Documents/python'

dirTO = "/Users/andreezy/Documents"

target = dirTO + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'
if os.path.isdir(dirFrom):
    with zipfile.ZipFile(target, 'w') as backup:
        # Iterate over all the files in directory
        for folderName, subfolders, filenames in os.walk(dirFrom):
            for filename in filenames:
                # create complete filepath of file in directory
                filePath = os.path.join(folderName, filename)
                if os.path.exists(filePath):
                    # Add file to zip
                    backup.write(filePath, basename(filePath))
                else:
                    print('Backup FAILED')
    if os.path.getsize(target) > 200:
        print('Backup created successfully', target)
    else:
        print('Size very small, you should check .zip-archive! Size is: {} bytes'.format(os.path.getsize(target)))
else:
    print('Backup FAILED')
