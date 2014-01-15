import sys


print "@@@ Starting the script ..."

from java.util import *
from javax.management import *   
from java.io import FileInputStream 

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
if sys.argv[1] == 'Cluster':
	###################Create KeyStores for cluster####################
	print 'Applying changes to cluster'
	cd('/Servers/AdminServer')
	cmo.setCustomIdentityKeyStoreFileName(wlsDomain+'/certs/appIdentityKeyStore.jks')
	set('CustomIdentityKeyStorePassPhrase', 'welcome1')
	cmo.setCustomTrustKeyStoreFileName(wlsDomain+'/certs/appTrustKeyStore.jks')
	set('CustomTrustKeyStorePassPhrase', 'welcome1')
	cmo.setKeyStores('CustomIdentityAndCustomTrust')
	cmo.setCustomIdentityKeyStoreType('JKS')
	cmo.setCustomTrustKeyStoreType('JKS')

	cd('/Servers/AdminServer/SSL/AdminServer')
	cmo.setServerPrivateKeyAlias(domainProps.get('domain1.cadm-vip1'))
	set('ServerPrivateKeyPassPhrase', 'welcome1')

	cd('/Servers/MS1')
	cmo.setCustomIdentityKeyStoreFileName(wlsDomain+'/certs/appIdentityKeyStore.jks')
	set('CustomIdentityKeyStorePassPhrase', 'welcome1')
	cmo.setCustomTrustKeyStoreFileName(wlsDomain+'/certs/appTrustKeyStore.jks')
	set('CustomTrustKeyStorePassPhrase', 'welcome1')
	cmo.setKeyStores('CustomIdentityAndCustomTrust')
	cmo.setCustomIdentityKeyStoreType('JKS')
	cmo.setCustomTrustKeyStoreType('JKS')

	cd('/Servers/MS1/SSL/MS1')
	cmo.setServerPrivateKeyAlias(domainProps.get('domain1.ms-vip1'))
	set('ServerPrivateKeyPassPhrase', 'welcome1')

	cd('/Servers/MS2')
	cmo.setCustomIdentityKeyStoreFileName(wlsDomain+'/certs/appIdentityKeyStore.jks')
	set('CustomIdentityKeyStorePassPhrase', 'welcome1')
	cmo.setCustomTrustKeyStoreFileName(wlsDomain+'/certs/appTrustKeyStore.jks')
	set('CustomTrustKeyStorePassPhrase', 'welcome1')
	cmo.setKeyStores('CustomIdentityAndCustomTrust')
	cmo.setCustomIdentityKeyStoreType('JKS')
	cmo.setCustomTrustKeyStoreType('JKS')

	cd('/Servers/MS2/SSL/MS2')
	cmo.setServerPrivateKeyAlias(domainProps.get('domain1.ms-vip2'))
	set('ServerPrivateKeyPassPhrase', 'welcome1')

	cd('/Servers/MS3')
	cmo.setCustomIdentityKeyStoreFileName(wlsDomain+'/certs/appIdentityKeyStore.jks')
	set('CustomIdentityKeyStorePassPhrase', 'welcome1')
	cmo.setCustomTrustKeyStoreFileName(wlsDomain+'/certs/appTrustKeyStore.jks')
	set('CustomTrustKeyStorePassPhrase', 'welcome1')
	cmo.setKeyStores('CustomIdentityAndCustomTrust')
	cmo.setCustomIdentityKeyStoreType('JKS')
	cmo.setCustomTrustKeyStoreType('JKS')

	cd('/Servers/MS3/SSL/MS3')
	cmo.setServerPrivateKeyAlias(domainProps.get('domain1.ms-vip3'))
	set('ServerPrivateKeyPassPhrase', 'welcome1')

	cd('/Servers/MS4')
	cmo.setCustomIdentityKeyStoreFileName(wlsDomain+'/certs/appIdentityKeyStore.jks')
	set('CustomIdentityKeyStorePassPhrase', 'welcome1')
	cmo.setCustomTrustKeyStoreFileName(wlsDomain+'/certs/appTrustKeyStore.jks')
	set('CustomTrustKeyStorePassPhrase', 'welcome1')
	cmo.setKeyStores('CustomIdentityAndCustomTrust')
	cmo.setCustomIdentityKeyStoreType('JKS')
	cmo.setCustomTrustKeyStoreType('JKS')

	cd('/Servers/MS4/SSL/MS4')
	cmo.setServerPrivateKeyAlias(domainProps.get('domain1.ms-vip4'))
	set('ServerPrivateKeyPassPhrase', 'welcome1')

	cd('/Servers/SOA1')
	cmo.setCustomIdentityKeyStoreFileName(wlsDomain+'/certs/appIdentityKeyStore.jks')
	set('CustomIdentityKeyStorePassPhrase', 'welcome1')
	cmo.setCustomTrustKeyStoreFileName(wlsDomain+'/certs/appTrustKeyStore.jks')
	set('CustomTrustKeyStorePassPhrase', 'welcome1')
	cmo.setKeyStores('CustomIdentityAndCustomTrust')
	cmo.setCustomIdentityKeyStoreType('JKS')
	cmo.setCustomTrustKeyStoreType('JKS')

	cd('/Servers/SOA1/SSL/SOA1')
	cmo.setServerPrivateKeyAlias(domainProps.get('domain1.soac-vip1'))
	set('ServerPrivateKeyPassPhrase', 'welcome1')

	cd('/Servers/SOA2')
	cmo.setCustomIdentityKeyStoreFileName(wlsDomain+'/certs/appIdentityKeyStore.jks')
	set('CustomIdentityKeyStorePassPhrase', 'welcome1')
	cmo.setCustomTrustKeyStoreFileName(wlsDomain+'/certs/appTrustKeyStore.jks')
	set('CustomTrustKeyStorePassPhrase', 'welcome1')
	cmo.setKeyStores('CustomIdentityAndCustomTrust')
	cmo.setCustomIdentityKeyStoreType('JKS')
	cmo.setCustomTrustKeyStoreType('JKS')

	cd('/Servers/SOA2/SSL/SOA2')
	cmo.setServerPrivateKeyAlias(domainProps.get('domain1.soac-vip2'))
	set('ServerPrivateKeyPassPhrase', 'welcome1')

	cd('/Servers/SOA3')
	cmo.setCustomIdentityKeyStoreFileName(wlsDomain+'/certs/appIdentityKeyStore.jks')
	set('CustomIdentityKeyStorePassPhrase', 'welcome1')
	cmo.setCustomTrustKeyStoreFileName(wlsDomain+'/certs/appTrustKeyStore.jks')
	set('CustomTrustKeyStorePassPhrase', 'welcome1')
	cmo.setKeyStores('CustomIdentityAndCustomTrust')
	cmo.setCustomIdentityKeyStoreType('JKS')
	cmo.setCustomTrustKeyStoreType('JKS')

	cd('/Servers/SOA3/SSL/SOA3')
	cmo.setServerPrivateKeyAlias(domainProps.get('domain1.soac-vip3'))
	set('ServerPrivateKeyPassPhrase', 'welcome1')

	cd('/Servers/SOA4')
	cmo.setCustomIdentityKeyStoreFileName(wlsDomain+'/certs/appIdentityKeyStore.jks')
	set('CustomIdentityKeyStorePassPhrase', 'welcome1')
	cmo.setCustomTrustKeyStoreFileName(wlsDomain+'/certs/appTrustKeyStore.jks')
	set('CustomTrustKeyStorePassPhrase', 'welcome1')
	cmo.setKeyStores('CustomIdentityAndCustomTrust')
	cmo.setCustomIdentityKeyStoreType('JKS')
	cmo.setCustomTrustKeyStoreType('JKS')

	cd('/Servers/SOA4/SSL/SOA4')
	cmo.setServerPrivateKeyAlias(domainProps.get('domain1.soac-vip4'))
	set('ServerPrivateKeyPassPhrase', 'welcome1')

	cd('/Servers/OSB1')
	cmo.setCustomIdentityKeyStoreFileName(wlsDomain+'/certs/appIdentityKeyStore.jks')
	set('CustomIdentityKeyStorePassPhrase', 'welcome1')
	cmo.setCustomTrustKeyStoreFileName(wlsDomain+'/certs/appTrustKeyStore.jks')
	set('CustomTrustKeyStorePassPhrase', 'welcome1')
	cmo.setKeyStores('CustomIdentityAndCustomTrust')
	cmo.setCustomIdentityKeyStoreType('JKS')
	cmo.setCustomTrustKeyStoreType('JKS')

	cd('/Servers/OSB1/SSL/OSB1')
	cmo.setServerPrivateKeyAlias(domainProps.get('domain1.osb-vip1'))
	set('ServerPrivateKeyPassPhrase', 'welcome1')

	cd('/Servers/OSB2')
	cmo.setCustomIdentityKeyStoreFileName(wlsDomain+'/certs/appIdentityKeyStore.jks')
	set('CustomIdentityKeyStorePassPhrase', 'welcome1')
	cmo.setCustomTrustKeyStoreFileName(wlsDomain+'/certs/appTrustKeyStore.jks')
	set('CustomTrustKeyStorePassPhrase', 'welcome1')
	cmo.setKeyStores('CustomIdentityAndCustomTrust')
	cmo.setCustomIdentityKeyStoreType('JKS')
	cmo.setCustomTrustKeyStoreType('JKS')

	cd('/Servers/OSB2/SSL/OSB2')
	cmo.setServerPrivateKeyAlias(domainProps.get('domain1.osb-vip2'))
	set('ServerPrivateKeyPassPhrase', 'welcome1')

	cd('/Servers/OSB3')
	cmo.setCustomIdentityKeyStoreFileName(wlsDomain+'/certs/appIdentityKeyStore.jks')
	set('CustomIdentityKeyStorePassPhrase', 'welcome1')
	cmo.setCustomTrustKeyStoreFileName(wlsDomain+'/certs/appTrustKeyStore.jks')
	set('CustomTrustKeyStorePassPhrase', 'welcome1')
	cmo.setKeyStores('CustomIdentityAndCustomTrust')
	cmo.setCustomIdentityKeyStoreType('JKS')
	cmo.setCustomTrustKeyStoreType('JKS')

	cd('/Servers/OSB3/SSL/OSB3')
	cmo.setServerPrivateKeyAlias(domainProps.get('domain1.osb-vip3'))
	set('ServerPrivateKeyPassPhrase', 'welcome1')

	cd('/Servers/OSB4')
	cmo.setCustomIdentityKeyStoreFileName(wlsDomain+'/certs/appIdentityKeyStore.jks')
	set('CustomIdentityKeyStorePassPhrase', 'welcome1')
	cmo.setCustomTrustKeyStoreFileName(wlsDomain+'/certs/appTrustKeyStore.jks')
	set('CustomTrustKeyStorePassPhrase', 'welcome1')
	cmo.setKeyStores('CustomIdentityAndCustomTrust')
	cmo.setCustomIdentityKeyStoreType('JKS')
	cmo.setCustomTrustKeyStoreType('JKS')

	cd('/Servers/OSB4/SSL/OSB4')
	cmo.setServerPrivateKeyAlias(domainProps.get('domain1.osb-vip4'))
	set('ServerPrivateKeyPassPhrase', 'welcome1')



if sys.argv[1] == 'StandAlone':
	############# JDBC stores for STANDALONE ADMINSERVER

	cd('/Servers/AdminServer')
	cmo.setCustomIdentityKeyStoreFileName(wlsDomain+'/certs/appIdentityKeyStore.jks')
	set('CustomIdentityKeyStorePassPhrase', 'welcome1')
	cmo.setCustomTrustKeyStoreFileName(wlsDomain+'/certs/appTrustKeyStore.jks')
	set('CustomTrustKeyStorePassPhrase', 'welcome1')
	cmo.setKeyStores('CustomIdentityAndCustomTrust')
	cmo.setCustomIdentityKeyStoreType('JKS')
	cmo.setCustomTrustKeyStoreType('JKS')

	cd('/Servers/AdminServer/SSL/AdminServer')
	cmo.setServerPrivateKeyAlias(domainProps.get('domain1.cadm-vip1'))
	set('ServerPrivateKeyPassPhrase', 'welcome1')
save()
activate()