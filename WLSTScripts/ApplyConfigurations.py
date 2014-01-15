
import sys


print "@@@ Starting the script ..."

from java.util import *
from javax.management import *   
from java.io import FileInputStream 

def createAdminStartupPropertiesFile(directoryPath, args,adminlogspath):
    adminserverDir1 = File(directoryPath)
    bool1 = adminserverDir1.mkdirs()
    adminserverDir2 = File(adminlogspath)
    bool2 = adminserverDir2.mkdirs()
    args=args+ '-Dweblogic.Stdout='+adminlogspath+'/AdminServer.out -Dweblogic.Stderr='+adminlogspath+'/AdminServer_error.out'
    fileNew=open(directoryPath + '/startup.properties', 'w')
    args=args.replace(':','\\:')
    args=args.replace('=','\\=')
    fileNew.write('Arguments=%s\n' % args)
    fileNew.flush()
    fileNew.close()

propInputStream1 = FileInputStream("domain.properties")
domainProps = util.Properties()
domainProps.load(propInputStream1) 

#The directory of the domain configuration
#/app/oracle/products/11g/admin/domains 
wlsDomain=os.environ["WLSDOMAIN"]
print "WLSDOMAIN="+wlsDomain

DOMAIN_PATH= wlsDomain + '/SOACoreDomain/aserver/SOACoreDomain'
print 'reading domain from '+DOMAIN_PATH


readDomain(DOMAIN_PATH)

cd('/')
assign('AppDeployment', 'Message Reporting Purger', 'Target', 'OSB1') 
unassign('AppDeployment', 'FileAdapter', 'Target', 'AdminServer')
unassign('AppDeployment', 'DbAdapter', 'Target', 'AdminServer')
unassign('AppDeployment', 'JmsAdapter', 'Target', 'AdminServer')
unassign('AppDeployment', 'AqAdapter', 'Target', 'AdminServer')
unassign('AppDeployment', 'FtpAdapter', 'Target', 'AdminServer')
unassign('AppDeployment', 'SocketAdapter', 'Target', 'AdminServer')
unassign('AppDeployment', 'MQSeriesAdapter', 'Target', 'AdminServer')
unassign('AppDeployment', 'OracleAppsAdapter', 'Target', 'AdminServer')
unassign('AppDeployment', 'OracleBamAdapter', 'Target', 'AdminServer')

unassign('AppDeployment', 'JMS Reporting Provider', 'Target', 'AdminServer')
unassign('AppDeployment', 'Ftp Transport Provider', 'Target', 'AdminServer')
unassign('AppDeployment', 'SFTP Transport Provider', 'Target', 'AdminServer')
unassign('AppDeployment', 'Email Transport Provider', 'Target', 'AdminServer')
unassign('AppDeployment', 'File Transport Provider', 'Target', 'AdminServer')
unassign('AppDeployment', 'MQ Transport Provider', 'Target', 'AdminServer')
unassign('AppDeployment', 'EJB Transport Provider', 'Target', 'AdminServer')
unassign('AppDeployment', 'Tuxedo Transport Provider', 'Target', 'AdminServer')
unassign('AppDeployment', 'ALDSP Transport Provider', 'Target', 'AdminServer')
unassign('AppDeployment', 'SB Transport Provider', 'Target', 'AdminServer')
unassign('AppDeployment', 'WS Transport Provider', 'Target', 'AdminServer')
unassign('AppDeployment', 'WS Transport Async Applcation', 'Target', 'AdminServer')
unassign('AppDeployment', 'FLOW Transport Provider', 'Target', 'AdminServer')
unassign('AppDeployment', 'BPEL 10g Transport Provider', 'Target', 'AdminServer')
unassign('AppDeployment', 'JCA Transport Provider', 'Target', 'AdminServer')
unassign('AppDeployment', 'JEJB Transport Provider', 'Target', 'AdminServer')
unassign('AppDeployment', 'SOA-DIRECT Transport Provider', 'Target', 'AdminServer')

applyJRF('WLSCoreCluster', wlsDomain + '/SOACoreDomain/aserver/SOACoreDomain')
Admin_Java_Arguments= domainProps.get("domain1.Admin_Java_Arguments")

wlsHome=os.environ["MWHOME"] 
print "MWHOME="+wlsHome	
#createAdminStartupPropertiesFile(DOMAIN_PATH+'/servers/AdminServer/data/nodemanager',Admin_Java_Arguments, wlsHome+'/adminlogs/SOACoreDomain/logs/AdminServer')
updateDomain()
closeDomain()
print 'Successfully updated domain.'
exit()
