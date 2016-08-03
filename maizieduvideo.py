# coding: utf-8
import sys
import urllib
import urllib2
import re
import cookielib
import requests
import chardet
import os
import thread,threading
from requests.adapters import HTTPAdapter

reload(sys)
sys.setdefaultencoding("utf-8")

class MaiZiVideo(object):

	@staticmethod
	def download_video(page_url, video_url, file_dir):
		course_resp = requests.get(page_url)
		course_resp.encoding = 'utf-8'
		course_html = course_resp.text.encode('utf-8')
		class_name = re.search(r'<h1 class="color33 font24 marginB10">(.*?)</h1>', course_html, re.S).group(1)
		#if not os._exists(file_dir + "/" + class_name):
		os.mkdir(file_dir + "/" + class_name)
		class_list = re.findall('target="_blank" class="font14 color66"><span class="fl">(.*?)</span><span class="fr color99">', course_html, re.S)
		count = 1
		for  each_class_name in class_list:
			print "正在下载第%d个视频" % count
			if count < 10:
				video_url_full = video_url + "0" + str(count) + ".mp4"
			else:
				video_url_full = video_url + str(count) + ".mp4"

			urllib.urlretrieve(video_url_full, file_dir + class_name + "/" + each_class_name + ".mp4", Schedule)
			count += 1

def Schedule(downloadSize, dataSize, remotelyFileSize):
	'''
	downloadSize:已经下载的数据块
	dataSize:数据块的大小
	remotelyFileSize:远程文件的大小
	'''
	per = 100.0 * downloadSize * dataSize / remotelyFileSize
	if per > 100:
		per = 100

	print u'当前下载进度:%.2f%%\r' % per

if __name__ == '__main__':
	page_url = 'http://www.maiziedu.com/course/645/'
	video_url = 'http://newoss.maiziedu.com/pcjc/pcjc-'
	file_dir = u'D:/personal/video/program/python/'
	MaiZiVideo.download_video(page_url, video_url, file_dir)