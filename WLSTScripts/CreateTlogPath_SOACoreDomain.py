import sys


print "@@@ Starting the script ..."

from java.util import *
from javax.management import *   
from java.io import FileInputStream 

print "@@@ Starting the script ..."
global props
   

propInputStream1 = FileInputStream("domain.properties")
domainProps = util.Properties()
domainProps.load(propInputStream1) 

#The directory of the domain configuration
#/app/oracle/products/11g/admin/domains 
wlsDomain=os.environ["WLSDOMAIN"]
print "WLSDOMAIN="+wlsDomain


adminURL='t3://'+domainProps.get('domain1.AdminIP')+':'+domainProps.get('domain1.AdminPort')
adminUserName='weblogic'
adminPassword=domainProps.get("domain1.AdminPasswd")
connect(adminUserName, adminPassword, adminURL)

edit()
startEdit()

adminserverDir = File(wlsDomain+'/SOACoreDomain/soa_cluster/tlogs')
bool = adminserverDir.mkdirs()

cd('/Servers/MS1')
cd('/Servers/MS1/DefaultFileStore/MS1')
cmo.setDirectory(wlsDomain+'/SOACoreDomain/soa_cluster/tlogs')

cd('/Servers/MS2')
cd('/Servers/MS2/DefaultFileStore/MS2')
cmo.setDirectory(wlsDomain+'/SOACoreDomain/soa_cluster/tlogs')

cd('/Servers/MS3')
cd('/Servers/MS3/DefaultFileStore/MS3')
cmo.setDirectory(wlsDomain+'/SOACoreDomain/soa_cluster/tlogs')

cd('/Servers/MS4')
cd('/Servers/MS4/DefaultFileStore/MS4')
cmo.setDirectory(wlsDomain+'/SOACoreDomain/soa_cluster/tlogs')


cd('/Servers/SOA1')
cd('/Servers/SOA1/DefaultFileStore/SOA1')
cmo.setDirectory(wlsDomain+'/SOACoreDomain/soa_cluster/tlogs')

cd('/Servers/SOA2')
cd('/Servers/SOA2/DefaultFileStore/SOA2')
cmo.setDirectory(wlsDomain+'/SOACoreDomain/soa_cluster/tlogs')

cd('/Servers/SOA3')
cd('/Servers/SOA3/DefaultFileStore/SOA3')
cmo.setDirectory(wlsDomain+'/SOACoreDomain/soa_cluster/tlogs')

cd('/Servers/SOA4')
cd('/Servers/SOA4/DefaultFileStore/SOA4')
cmo.setDirectory(wlsDomain+'/SOACoreDomain/soa_cluster/tlogs')


cd('/Servers/OSB1')
cd('/Servers/OSB1/DefaultFileStore/OSB1')
cmo.setDirectory(wlsDomain+'/SOACoreDomain/soa_cluster/tlogs')

cd('/Servers/OSB2')
cd('/Servers/OSB2/DefaultFileStore/OSB2')
cmo.setDirectory(wlsDomain+'/SOACoreDomain/soa_cluster/tlogs')

cd('/Servers/OSB3')
cd('/Servers/OSB3/DefaultFileStore/OSB3')
cmo.setDirectory(wlsDomain+'/SOACoreDomain/soa_cluster/tlogs')

cd('/Servers/OSB4')
cd('/Servers/OSB4/DefaultFileStore/OSB4')
cmo.setDirectory(wlsDomain+'/SOACoreDomain/soa_cluster/tlogs')
save()
activate()
