import subprocess

# example
# link = ['https://youtube.com/videos/1','https://www.dailymotion.com/video/2']
link = ['',]

for i in link:
	print('Start download ' + i + ' ...')
	cmd = subprocess.run('youtube-dl -o %(title)s.%(ext)s ' + i,shell='False',stdout=subprocess.PIPE)
	print('Download ' + i + ' done!\n')
	#exit()

print('done')
