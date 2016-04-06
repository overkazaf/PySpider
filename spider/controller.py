import os
import spider as Spider

' controller module '

__author__ = 'overkazaf'
__resource__ = 'static'

def isExcludeFiles(ext):
	excludeFiles = ['.js', '.css']
	for fileExt in excludeFiles:
		if ext == fileExt:
			return True
	return False

def filterPath (dirs):
	list = []
	for dir in dirs:
		if dir == 'css' or dir == 'js':
			continue
		list.append(dir)
	return list

def getVolumnList():
	list = []
	dirs = os.listdir(__resource__)
	print 'dirs ', dirs
	for dir in dirs:
		if dir == 'css' or dir == 'js':
			continue
		list.append(dir)

	return list

#functions
def getDownloadedMusicList ():
	dirs = os.listdir(__resource__)
	for dir in dirs:
		mp3Path = __resource__ + '/' + dir + '/mp3/'
		picPath = __resource__ + '/' + dir + '/pic/'

		filename, file_extension = os.path.splitext(dir)

		print 'file_extension ', file_extension
		print 'filename ', filename
		#filter js files
		if isExcludeFiles(file_extension) :
			continue
		if mp3Path == 'static/css/mp3/':
			continue

		mp3 = os.listdir(mp3Path)
		mp3 = map(lambda x : mp3Path + x, mp3)
		#print 'mp3Path:', mp3Path 
		#print mp3

		pic = os.listdir(picPath)
		pic = map(lambda x : picPath + x, pic)
		#print 'picPath:', picPath
		#print pic
	return None

#get all the downloaded resources for local folder
def getLocalResources ():
	dirs = os.listdir(__resource__)
	dirs = filterPath(dirs)
	mp3, pic = [],[]
	dict = {'mp3':[], 'pic':[]}
	for dir in dirs:
		mp3Path = __resource__ + '/' + dir + '/mp3/'
		picPath = __resource__ + '/' + dir + '/pic/'

		#filter js files
		filename, file_extension = os.path.splitext(dir)
		
		if not os.path.exists(mp3Path):
			continue
			
		if isExcludeFiles(file_extension) :
			continue

		mp3 = os.listdir(mp3Path)
		mp3 = map(lambda x : mp3Path + x, mp3)

		pic = os.listdir(picPath)
		pic = map(lambda x : picPath + x, pic)
		

		ret1 = {}
		ret1[dir] = mp3
		ret2 = {}
		ret2[dir] = pic
		dict['mp3'].append(ret1)
		dict['pic'].append(ret2)
	return dict

#get current range of the downloaded volumns
def getVolRange ():
	minVol = 0
	maxVol = 0
	dirs = os.listdir(__resource__)
	dirs = filterPath(dirs)

	#sort by the volumn
	dirs.sort(lambda x,y: cmp(x.split('.')[1], y.split('.')[1]))

	minVol = dirs[0].split('.')[1]
	maxVol = dirs[-1].split('.')[1]

	print 'minVol ', minVol, ' maxVol ', maxVol

	return {'min': minVol, 'max': maxVol}


def runScheduler(type, start, end):
	tasks = []

	print 'start at ', str(start), ' end at ', end
	if type == 'mp3':
		Spider.getMusicByRange(start, end)
	elif type == 'pic':
		Spider.getPicByRange(start, end)
	elif type == 'all':
		Spider.getPicByRange(start, end)
		Spider.getMusicByRange(start, end)

	
def startScheduler(type, rangeType, start, end):
	volRange = getVolRange()
	minVol = int(volRange['min'])
	maxVol = int(volRange['max'])
	start = int(start)
	end = int(end)

	if rangeType == 'normal':
		runScheduler(type, start, end)
	elif rangeType == 'forward':
		runScheduler(type, maxVol + 1, maxVol + end)
	elif rangeType == 'backward':
		runScheduler(type, minVol - start, minVol - 1)

	return True



def getThanksDict (list):
	return Spider.getThanksByVolumns(list)