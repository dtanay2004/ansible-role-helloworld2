# -*- coding: utf-8 -*-

import requests
import logging

"""Main module."""

def download(logLevel, repo="inhumantsar/flask-helloworld2"):
    download_url=""

    print(logLevel) 
  # setting up the logger
    logger = logging.getLogger('ghdl')

    if (logLevel == 'DEBUG'):
        logger.setLevel(logging.DEBUG)
    elif (logLevel == 'INFO'):
        logger.setLevel(logging.INFO)

  # set up for logging to stdout & stderr
    ch = logging. StreamHandler()
    logger.addHandler(ch)
  
    listRelease=requests.get('https://api.github.com/repos/{}/releases'.format(repo)).json()
    
    if (len(listRelease) > 0):
       logger.info("repo doesn't contain any tarball url")
       download_url = listRelease[0]['tarball_url']
    else:
       logger.info("INFO: no url found")
       logger.debug("DEBUG:setting up a default url")
       download_url = 'https://github.com/{}/archive/master.tar.gz'.format(repo)

    print ("List length %s\n" % len(listRelease))
    print(download_url)

# 2nd part of the code
   
    local_filename = "{}.tgz".format(repo.replace('/','_'))
    r = requests.get(download_url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk:      
                f.write(chunk)
    print('file written to {}'.format(local_filename))
    logger.info("INFO: download is completed")
