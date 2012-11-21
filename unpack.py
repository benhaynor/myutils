#!/usr/bin/env python
'''
Used to label all the java files that my EITs submit, before sending the to moss.
'''

import shutil
import glob
import re
import os
import sys

def unpackAll():
    for eit in glob.glob('*'):
        out = re.search('[^_]+',eit)
        outdir = out.group(0).replace(' ','_')
        os.mkdir(outdir)
        shutil.move(eit,outdir)
        for dp,dn,flist in os.walk(outdir):
            for f in flist:
                compressed = re.search('.*\.zip',f)
                if compressed:
                    zipfile = os.path.join(dp,f)
                    os.popen("unzip -d '%s' '%s'" % (outdir, zipfile))
                compressed = re.search('.*\.rar',f)
                if compressed:
                    rarfile = os.path.join(dp,f)
                    os.popen("unrar e '%s' '%s'" % (rarfile,outdir))
                compressed = re.search('.*\.7z',f)
                if compressed:
                    sevenZ = os.path.join(dp,f)
                    #print sevenZ
                    os.popen("7z e '%s' -o'%s' -y" % (sevenZ,outdir))

def moveAll(outdir):
    for dp,dn,flist in os.walk('.'):
        for f in flist:
            if '.java' in f:
                eitName = dp.split('/')[1]
                os.popen ("mv '%s' '%s%s%s'"%(os.path.join(dp,f),outdir,eitName,f))

if __name__ == '__main__':
    unpackAll()
    moveAll(sys.argv[1])
    
