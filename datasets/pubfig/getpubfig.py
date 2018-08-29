#!/usr/bin/env python

import cv2
import logging
import os
import sys
import subprocess
import random

def logdbg(where, s):
    logging.getLogger(where).debug(s)

def logerr(where, s):
    logging.getLogger(where).error(s)

def loginfo(where, s):
    logging.getLogger(where).info(s)

def wget_cmd(url, to_path, log_file):
    print('TOPATH', url, to_path, log_file)
    cmd = ['wget',
            url,
            '-O', to_path,
            '-o', log_file,
            '--user-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.3) Gecko/2008092416 Firefox/3.0.3',
            '-e', 'robots=off',
            '-t', '3',
            '--waitretry', '5',
            ]
    return cmd

def url_list_parse(file_handle):
    for line in file_handle:
        if line.startswith('#'): continue
        (name, num, url, coords, md5) = line.strip().split('\t')
        # print(name.replace(' ','_') + '_' + str(num) , num)
        folder_name = name.replace(' ','_')
        file_name = name.replace(' ','_') + '_' + str( "%04d" % int(num))
        yield (url, md5, folder_name, file_name)

def download_images(dev_or_eval):
    logging.basicConfig(level=logging.DEBUG)
    if not os.path.exists(dev_or_eval):
        loginfo('download_images', 'mkdir %s'%dev_or_eval)
        os.mkdir(dev_or_eval)
    
    not_found_images_handle = open('%s_not_found.log'%dev_or_eval, 'a')
    url_list_handle = open('%s_urls.txt'%dev_or_eval)
    base_folder = '%s'%dev_or_eval
    log_file = '%s_wget.log'%dev_or_eval
    images_saved, images_processed = 0, 0
    url_md5s = list(url_list_parse(url_list_handle))
    random.shuffle(url_md5s)
    
    for (url, md5, folder_name, file_name) in url_md5s:
        path_to_create = dev_or_eval + '/' + folder_name
        if not os.path.exists(path_to_create):
            os.mkdir(path_to_create)
        
        images_processed += 1
        img_termination = url[url.rfind('.'):]
        img_path = folder_name + '/' + file_name + img_termination
        loginfo("download_images", "downloading %s to %s"%(url, img_path))
        fullpath = os.path.join(base_folder, img_path)
        if os.path.exists(fullpath):
            logerr("download_images", "%s already exists, skipping" % fullpath)
            continue

        cmd = wget_cmd(url, fullpath, log_file)
        logdbg('download_images', ' '.join(cmd))
        retcode = subprocess.call(cmd)
        if retcode != 0:
            logerr("download_images", "Error saving %s!"%fullpath)
            not_found_images_handle.write("%s %s\n"%(url, img_path))
            not_found_images_handle.flush()
            continue
        images_saved += 1
        img = cv2.imread("lenna.png")
    loginfo("download_images", "images processed: %d "%(images_processed))
    loginfo("download_images", "images saved: %d"%(images_saved))

def usage():
    print """\
USAGE: getpubfig.py dev | eval
to download either dev or eval dataset. dev_urls.txt and eval_urls.txt must be
in the current working directory. Images and logs will be saved to the current
working directory.
"""

def main():
    if len(sys.argv) != 2 or sys.argv[1] not in ('dev', 'eval'):
        usage()
        return

    logging.getLogger().setLevel(logging.DEBUG)
    logging.getLogger().addHandler(logging.FileHandler('getpubfig.log'))
    logging.getLogger().addHandler(logging.StreamHandler())
    download_images(sys.argv[1])

if __name__ == '__main__':
    main()
