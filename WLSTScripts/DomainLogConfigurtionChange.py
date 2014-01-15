from java.util import *
from javax.management import *   
from java.io import FileInputStream 

propInputStream = FileInputStream("domain_log.properties")
configProps = Properties()
configProps.load(propInputStream)

totalNumbersofDomains=configProps.get("total.domain.count")


wlsHome=os.environ["MWHOME"] 
print "MWHOME="+wlsHome

rotationType=configProps.get("rotationType")
#numberOfFilesLimited=configProps.get("numberOfFilesLimited")
fileMinSize=configProps.get("fileMinSize")
rotateLogOnStartup=configProps.get("rotateLogOnStartup")
fileCount=configProps.get("fileCount")
log4jEnabled = configProps.get("log4jEnabled")
stdoutSeverity = configProps.get("stdoutSeverity")
logBRSeverity = configProps.get("logBRSeverity")
logFileSeverity = configProps.get("logFileSeverity")
memBufferSeverity = configProps.get("memBufferSeverity")
memBufferSize = configProps.get("memBufferSize")
numOfFilesLimited = configProps.get("numOfFilesLimited")
redirectStdout = configProps.get("redirectStdout")
redirectStdErr = configProps.get("redirectStdErr")
rotateOnStartup = configProps.get("rotateOnStartup")
#rotateTime = configProps.get("rotateTime")
rotateType = configProps.get("rotateType")
httpAccessLoggingEnabled = configProps.get("httpAccessLoggingEnabled")


def str2bool(v):
	return v.lower() in ("yes", "true", "t", "1")

domainTmpCount=1
while (domainTmpCount <= int(totalNumbersofDomains)) :

	domainName = configProps.get("domain."+ str(domainTmpCount)+".name")
	domainAdminUrl = configProps.get("domain."+ str(domainTmpCount)+".admin.url")
	domainAdminUserName = configProps.get("domain."+ str(domainTmpCount)+".admin.username")
	domainAdminPassword = configProps.get("domain."+ str(domainTmpCount)+".admin.password")
	serverCount = configProps.get("total.domain."+ str(domainTmpCount)+".server.count")
	folderPath=wlsHome+'/adminlogs/'+domainName
	adminserverDir = File(folderPath)
	bool = adminserverDir.mkdirs()
	connect(domainAdminUserName, domainAdminPassword, domainAdminUrl)
	res=''
	print '##################################################'
	print 'Changing Log Settings For Domain: ', domainName
	print '##################################################'
	serverTmpCount=1
	edit()
	startEdit()
	cd('/Log/'+domainName)
	cmo.setRotationType('bySize')
	cmo.setFileMinSize(5000)
	set("FileCount", 10)
	print 'Setting FileName to be ' + folderPath+ '/logs/AdminServer/'  + domainName + '.log'
	set("FileName", folderPath+ '/logs/AdminServer/'  + domainName + '.log')

	#cmo.setFileName( 'logs/AdminServer/'  + domainName + '.log')
	print "Original LogFileSeverity is " , get("LogFileSeverity")
	print "Setting LogFileSeverity to be " , logFileSeverity
	set("LogFileSeverity", logFileSeverity)
	
	print "Original MemoryBufferSeverity is " , get("MemoryBufferSeverity")
	print "Setting MemoryBufferSeverity to be " , memBufferSeverity
	set("MemoryBufferSeverity", memBufferSeverity)
	
	print "Original MemoryBufferSize is " , get("MemoryBufferSize")
	print "Setting MemoryBufferSize to be " , memBufferSize
	set("MemoryBufferSize", int(memBufferSize))
	
	print "Original NumberOfFilesLimited is " , get("NumberOfFilesLimited")
	print "Setting NumberOfFilesLimited to be " , numOfFilesLimited
	set("NumberOfFilesLimited", numOfFilesLimited)

	print "Original RedirectStdoutToServerLogEnabled is " , get("RedirectStdoutToServerLogEnabled")
	print "Setting RedirectStdoutToServerLogEnabled to be " , redirectStdout
	set("RedirectStdoutToServerLogEnabled", redirectStdout)
	
	print "Original RedirectStderrToServerLogEnabled is " , get("RedirectStderrToServerLogEnabled")
	print "Setting RedirectStderrToServerLogEnabled to be " , redirectStdErr
	set("RedirectStderrToServerLogEnabled", redirectStdErr)

	print "Original RotateLogOnStartup is " , get("RotateLogOnStartup")
	print "Setting RotateLogOnStartup to be " , rotateOnStartup
	set("RotateLogOnStartup", rotateOnStartup)

	print "Original RotationTime is " , get("RotationTime")
	#print "Setting RotationTime to be " , rotateTime
	#set("RotationTime", rotateTime)

	print "Original RotationType is " , get("RotationType")
	print "Setting RotationType to be " , rotateType
	set("RotationType", rotateType)
	while (serverTmpCount <= int(serverCount)) :
		edit()
		startEdit()
		serverName1 = configProps.get("domain."+ str(domainTmpCount)+".server."+ str(serverTmpCount)+".name")
		print '----------------------------------------------------'
		print 'Changing Log Setting for serverName: ' , serverName1
		print '----------------------------------------------------'
		cd('/Servers/' + serverName1 + '/Log/' + serverName1)
		# change the LogFileMBean and LogMBean attributes
		print "Original FileCount is " ,get("FileCount")
		print "Setting FileCount to be " , fileCount
		set("FileCount", int(fileCount))
		print "Original FileMinSize is " , get("FileMinSize")
		print "Setting FileMinSize to be " , fileMinSize
		set("FileMinSize", int(fileMinSize))
		print "Original FileName is " , get("FileName")

		
		if serverName1 == 'AdminServer':
		  print "Setting FileName to be " + folderPath+ "/logs/"+serverName1+ "/" + serverName1 + ".log"
		  set("FileName", folderPath+ '/logs/'+serverName1+ "/"  + serverName1 + '.log')
		
		#if serverName1 != 'AdminServer':
		#print "Setting FileName to be " +  "logs/"+serverName1+ "/" + serverName1 + ".log"
		#set("FileName",  'logs/'+serverName1+ "/"  + serverName1 + '.log')
		  
		print "Original FileTimeSpan is " , get("FileTimeSpan")
		#print "Setting FileTimeSpan to be " , fileTimeSpan
		#set("FileTimeSpan", fileTimeSpan)
		
		print "Original Log4jEnabled is " , get("Log4jLoggingEnabled")
		print "Setting Log4jLoggingEnabled to be " , log4jEnabled
		set("Log4jLoggingEnabled", log4jEnabled)
		
		print "Original StdoutSeverity is " , get("StdoutSeverity")
		print "Setting StdoutSeverity to be " , stdoutSeverity
		set("StdoutSeverity", stdoutSeverity)
		
		print "Original DomainLogBroadcastSeverity is " , get("DomainLogBroadcastSeverity")
		print "Setting DomainLogBroadcastSeverity to be " , logBRSeverity
		set("DomainLogBroadcastSeverity", logBRSeverity)
		
		print "Original LogFileSeverity is " , get("LogFileSeverity")
		print "Setting LogFileSeverity to be " , logFileSeverity
		set("LogFileSeverity", logFileSeverity)
		
		print "Original MemoryBufferSeverity is " , get("MemoryBufferSeverity")
		print "Setting MemoryBufferSeverity to be " , memBufferSeverity
		set("MemoryBufferSeverity", memBufferSeverity)
		
		print "Original MemoryBufferSize is " , get("MemoryBufferSize")
		print "Setting MemoryBufferSize to be " , memBufferSize
		set("MemoryBufferSize", int(memBufferSize))
		
		print "Original NumberOfFilesLimited is " , get("NumberOfFilesLimited")
		print "Setting NumberOfFilesLimited to be " , numOfFilesLimited
		set("NumberOfFilesLimited", numOfFilesLimited)
		
		print "Original RedirectStdoutToServerLogEnabled is " , get("RedirectStdoutToServerLogEnabled")
		print "Setting RedirectStdoutToServerLogEnabled to be " , redirectStdout
		set("RedirectStdoutToServerLogEnabled", redirectStdout)
		
		print "Original RedirectStderrToServerLogEnabled is " , get("RedirectStderrToServerLogEnabled")
		print "Setting RedirectStderrToServerLogEnabled to be " , redirectStdErr
		set("RedirectStderrToServerLogEnabled", redirectStdErr)

		print "Original RotateLogOnStartup is " , get("RotateLogOnStartup")
		print "Setting RotateLogOnStartup to be " , rotateOnStartup
		set("RotateLogOnStartup", rotateOnStartup)

		print "Original RotationTime is " , get("RotationTime")
		#print "Setting RotationTime to be " , rotateTime
		#set("RotationTime", rotateTime)

		print "Original RotationType is " , get("RotationType")
		print "Setting RotationType to be " , rotateType
		set("RotationType", rotateType)

		print '===> Log Setting for serverName: ' , serverName1, ' has been changed Successfully !!'
		print ''
		serverTmpCount = serverTmpCount +1
		
		#Webserver Http Access Log
		print '===> Log Setting changes for Http Access Log: '
		cd('/Servers/'+serverName1+'/WebServer/'+serverName1+'/WebServerLog/'+serverName1)
		
		if serverName1 == 'AdminServer':
		  set("FileName", folderPath+ '/logs/'+serverName1+ "/"  + 'accesss.log')

		print "Original Http Access LoggingEnabled is " , get("LoggingEnabled")
		print "Setting Http Access LoggingEnabled to be " , httpAccessLoggingEnabled
		set("LoggingEnabled", httpAccessLoggingEnabled)
		
		print "Original NumberOfFilesLimited is " , get("NumberOfFilesLimited")
		print "Setting NumberOfFilesLimited to be " , numOfFilesLimited
		set("NumberOfFilesLimited", numOfFilesLimited)
		
		print "Original RotateLogOnStartup is " , get("RotateLogOnStartup")
		print "Setting RotateLogOnStartup to be " , rotateOnStartup
		set("RotateLogOnStartup", rotateOnStartup)

		print "Original RotationType is " , get("RotationType")
		print "Setting RotationType to be " , rotateType
		set("RotationType", rotateType)

		#Diagnostic Log files
		print '===> Log Setting changes for diagnostics Log: '
		path = '/Servers/' + serverName1
		cd(path)
		
		lh = listLogHandlers()
		for l in lh:
		  lname = l.get('name')
		  #odlfile = 'logs/' + serverName1 + '/' + serverName1 + '-' + lname + '-diagnostic.log'
		  if serverName1 == 'AdminServer':
		    odlfile = folderPath + '/logs/' + serverName1 + '/' + serverName1 + '-' + lname + '-diagnostic.log'
		    print 'Diagnostic path===>',odlfile
		    configureLogHandler(target=serverName1,name=lname, path=odlfile,maxFileSize="20M")

		  if serverName1 != 'AdminServer':
		    #odlfile = 'logs/' + serverName1 + '/' + serverName1 + '-' + lname + '-diagnostic.log'
		    print 'Diagnostic path===>',odlfile
		    configureLogHandler(target=serverName1,name=lname, maxFileSize="20M")

		  res = res + '\n' + odlfile

		save()
		activate()
	
		print '===> Diagnostic Log Setting for serverName: ' , serverName1, ' has been changed Successfully !!'		

	print '***** Log Settings For Domain: ', domainName ,' has been changed Successfully !! *****'
	print ''
	domainTmpCount = domainTmpCount +1
exit()
