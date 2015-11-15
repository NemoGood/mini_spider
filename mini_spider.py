#encoding:UTF-8

import argparse
import ConfigParser

class MiniSpider:
    url_list_file=""
    output_directory=""
    max_depth=1
    crawl_interval=1
    crawl_timeout=1
    target_url=""
    thread_count=1


    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-c','--conf',help="the file of the conf")
        parser.add_argument('-v','--version', action='version',version='%(prog)s 1.0')
        args = parser.parse_args()
        confFile = args.conf
        self.__getConf__(confFile)

    def __getConf__(self,filename):
        configParser = ConfigParser.ConfigParser()
        configParser.read(filename)
        self.url_list_file = configParser.get("spider","url_list_file")
        self.output_directory = configParser.get("spider","output_directory")
        self.max_depth = configParser.getint("spider","max_depth")
        self.crawl_interval = configParser.getint("spider","crawl_interval")
        self.crawl_timeout = configParser.getint("spider","crawl_timeout")
        self.target_url = configParser.get("spider","target_url")
        self.thread_count = configParser.getint("spider","thread_count")
        #print self.url_list_file
        #print self.thread_count

if __name__=="__main__":
    miniSpider = MiniSpider()
