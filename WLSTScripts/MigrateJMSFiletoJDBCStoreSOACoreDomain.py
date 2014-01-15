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
	###################Create JDBC Stores for cluster####################

	cd('/')
	cmo.createJDBCStore('WseeJaxwsJDBCStore_auto_1')
	cd('/JDBCStores/WseeJaxwsJDBCStore_auto_1')
	cmo.setDataSource(getMBean('/SystemResources/EAIJMSDataSource'))
	cmo.setPrefixName('WseeJaxws1')
	set('Targets',jarray.array([ObjectName('com.bea:Name=MS1,Type=Server')], ObjectName))

	cd('/')
	cmo.createJDBCStore('WseeJaxwsJDBCStore_auto_2')
	cd('/JDBCStores/WseeJaxwsJDBCStore_auto_2')
	cmo.setDataSource(getMBean('/SystemResources/EAIJMSDataSource'))
	cmo.setPrefixName('WseeJaxws2')
	set('Targets',jarray.array([ObjectName('com.bea:Name=MS2,Type=Server')], ObjectName))

	cd('/')
	cmo.createJDBCStore('WseeJaxwsJDBCStore_auto_3')
	cd('/JDBCStores/WseeJaxwsJDBCStore_auto_3')
	cmo.setDataSource(getMBean('/SystemResources/EAIJMSDataSource'))
	cmo.setPrefixName('WseeJaxws3')
	set('Targets',jarray.array([ObjectName('com.bea:Name=MS3,Type=Server')], ObjectName))

	cd('/')
	cmo.createJDBCStore('WseeJaxwsJDBCStore_auto_4')
	cd('/JDBCStores/WseeJaxwsJDBCStore_auto_4')
	cmo.setDataSource(getMBean('/SystemResources/EAIJMSDataSource'))
	cmo.setPrefixName('WseeJaxws4')
	set('Targets',jarray.array([ObjectName('com.bea:Name=MS4,Type=Server')], ObjectName))

	cd('/')
	cmo.createJDBCStore('WseeJDBCStore_auto_1')
	cd('/JDBCStores/WseeJDBCStore_auto_1')
	cmo.setDataSource(getMBean('/SystemResources/EAIJMSDataSource'))
	cmo.setPrefixName('Wsee1')
	set('Targets',jarray.array([ObjectName('com.bea:Name=MS1,Type=Server')], ObjectName))

	cd('/')
	cmo.createJDBCStore('WseeJDBCStore_auto_2')
	cd('/JDBCStores/WseeJDBCStore_auto_2')
	cmo.setDataSource(getMBean('/SystemResources/EAIJMSDataSource'))
	cmo.setPrefixName('Wsee2')
	set('Targets',jarray.array([ObjectName('com.bea:Name=MS2,Type=Server')], ObjectName))

	cd('/')
	cmo.createJDBCStore('WseeJDBCStore_auto_3')
	cd('/JDBCStores/WseeJDBCStore_auto_3')
	cmo.setDataSource(getMBean('/SystemResources/EAIJMSDataSource'))
	cmo.setPrefixName('Wsee3')
	set('Targets',jarray.array([ObjectName('com.bea:Name=MS3,Type=Server')], ObjectName))

	cd('/')
	cmo.createJDBCStore('WseeJDBCStore_auto_4')
	cd('/JDBCStores/WseeJDBCStore_auto_4')
	cmo.setDataSource(getMBean('/SystemResources/EAIJMSDataSource'))
	cmo.setPrefixName('Wsee4')
	set('Targets',jarray.array([ObjectName('com.bea:Name=MS4,Type=Server')], ObjectName))

	cd('/')
	cmo.createJDBCStore('WseeJDBCStore_auto_5')
	cd('/JDBCStores/WseeJDBCStore_auto_5')
	cmo.setDataSource(getMBean('/SystemResources/EAIJMSDataSource'))
	cmo.setPrefixName('WseeOSB5')
	set('Targets',jarray.array([ObjectName('com.bea:Name=OSB1,Type=Server')], ObjectName))

	cd('/')
	cmo.createJDBCStore('WseeJDBCStore_auto_6')
	cd('/JDBCStores/WseeJDBCStore_auto_6')
	cmo.setDataSource(getMBean('/SystemResources/EAIJMSDataSource'))
	cmo.setPrefixName('WseeOSB6')
	set('Targets',jarray.array([ObjectName('com.bea:Name=OSB2,Type=Server')], ObjectName))

	cd('/')
	cmo.createJDBCStore('WseeJDBCStore_auto_7')
	cd('/JDBCStores/WseeJDBCStore_auto_7')
	cmo.setDataSource(getMBean('/SystemResources/EAIJMSDataSource'))
	cmo.setPrefixName('WseeOSB7')
	set('Targets',jarray.array([ObjectName('com.bea:Name=OSB3,Type=Server')], ObjectName))

	cd('/')
	cmo.createJDBCStore('WseeJDBCStore_auto_8')
	cd('/JDBCStores/WseeJDBCStore_auto_8')
	cmo.setDataSource(getMBean('/SystemResources/EAIJMSDataSource'))
	cmo.setPrefixName('WseeOSB8')
	set('Targets',jarray.array([ObjectName('com.bea:Name=OSB4,Type=Server')], ObjectName))

	cd('/')
	cmo.createJDBCStore('UMSJMSJDBCStore_auto_1')
	cd('/JDBCStores/UMSJMSJDBCStore_auto_1')
	cmo.setDataSource(getMBean('/SystemResources/EAIJMSDataSource'))
	cmo.setPrefixName('UMSJMS1')
	set('Targets',jarray.array([ObjectName('com.bea:Name=SOA1,Type=Server')], ObjectName))

	cd('/')
	cmo.createJDBCStore('UMSJMSJDBCStore_auto_2')
	cd('/JDBCStores/UMSJMSJDBCStore_auto_2')
	cmo.setDataSource(getMBean('/SystemResources/EAIJMSDataSource'))
	cmo.setPrefixName('UMSJMS2')
	set('Targets',jarray.array([ObjectName('com.bea:Name=SOA2,Type=Server')], ObjectName))

	cd('/')
	cmo.createJDBCStore('UMSJMSJDBCStore_auto_3')
	cd('/JDBCStores/UMSJMSJDBCStore_auto_3')
	cmo.setDataSource(getMBean('/SystemResources/EAIJMSDataSource'))
	cmo.setPrefixName('UMSJMS3')
	set('Targets',jarray.array([ObjectName('com.bea:Name=SOA3,Type=Server')], ObjectName))

	cd('/')
	cmo.createJDBCStore('UMSJMSJDBCStore_auto_4')
	cd('/JDBCStores/UMSJMSJDBCStore_auto_4')
	cmo.setDataSource(getMBean('/SystemResources/EAIJMSDataSource'))
	cmo.setPrefixName('UMSJMS4')
	set('Targets',jarray.array([ObjectName('com.bea:Name=SOA4,Type=Server')], ObjectName))

	cd('/')
	cmo.createJDBCStore('BPMJMSJDBCStore_auto_1')
	cd('/JDBCStores/BPMJMSJDBCStore_auto_1')
	cmo.setDataSource(getMBean('/SystemResources/EAIJMSDataSource'))
	cmo.setPrefixName('BPMJMS1')
	set('Targets',jarray.array([ObjectName('com.bea:Name=SOA1,Type=Server')], ObjectName))

	cd('/')
	cmo.createJDBCStore('BPMJMSJDBCStore_auto_2')
	cd('/JDBCStores/BPMJMSJDBCStore_auto_2')
	cmo.setDataSource(getMBean('/SystemResources/EAIJMSDataSource'))
	cmo.setPrefixName('BPMJMS2')
	set('Targets',jarray.array([ObjectName('com.bea:Name=SOA2,Type=Server')], ObjectName))

	cd('/')
	cmo.createJDBCStore('BPMJMSJDBCStore_auto_3')
	cd('/JDBCStores/BPMJMSJDBCStore_auto_3')
	cmo.setDataSource(getMBean('/SystemResources/EAIJMSDataSource'))
	cmo.setPrefixName('BPMJMS3')
	set('Targets',jarray.array([ObjectName('com.bea:Name=SOA3,Type=Server')], ObjectName))

	cd('/')
	cmo.createJDBCStore('BPMJMSJDBCStore_auto_4')
	cd('/JDBCStores/BPMJMSJDBCStore_auto_4')
	cmo.setDataSource(getMBean('/SystemResources/EAIJMSDataSource'))
	cmo.setPrefixName('BPMJMS4')
	set('Targets',jarray.array([ObjectName('com.bea:Name=SOA4,Type=Server')], ObjectName))

	cd('/')
	cmo.createJDBCStore('SOAJMSJDBCStore_auto_1')
	cd('/JDBCStores/SOAJMSJDBCStore_auto_1')
	cmo.setDataSource(getMBean('/SystemResources/EAIJMSDataSource'))
	cmo.setPrefixName('SOAJMS1')
	set('Targets',jarray.array([ObjectName('com.bea:Name=SOA1,Type=Server')], ObjectName))

	cd('/')
	cmo.createJDBCStore('SOAJMSJDBCStore_auto_2')
	cd('/JDBCStores/SOAJMSJDBCStore_auto_2')
	cmo.setDataSource(getMBean('/SystemResources/EAIJMSDataSource'))
	cmo.setPrefixName('SOAJMS2')
	set('Targets',jarray.array([ObjectName('com.bea:Name=SOA2,Type=Server')], ObjectName))

	cd('/')
	cmo.createJDBCStore('SOAJMSJDBCStore_auto_3')
	cd('/JDBCStores/SOAJMSJDBCStore_auto_3')
	cmo.setDataSource(getMBean('/SystemResources/EAIJMSDataSource'))
	cmo.setPrefixName('SOAJMS3')
	set('Targets',jarray.array([ObjectName('com.bea:Name=SOA3,Type=Server')], ObjectName))

	cd('/')
	cmo.createJDBCStore('SOAJMSJDBCStore_auto_4')
	cd('/JDBCStores/SOAJMSJDBCStore_auto_4')
	cmo.setDataSource(getMBean('/SystemResources/EAIJMSDataSource'))
	cmo.setPrefixName('SOAJMS4')
	set('Targets',jarray.array([ObjectName('com.bea:Name=SOA4,Type=Server')], ObjectName))

	cd('/')
	cmo.createJDBCStore('JDBCStore_auto_1')
	cd('/JDBCStores/JDBCStore_auto_1')
	cmo.setDataSource(getMBean('/SystemResources/EAIJMSDataSource'))
	cmo.setPrefixName('JDBCStore1')

	set('Targets',jarray.array([ObjectName('com.bea:Name=OSB1,Type=Server')], ObjectName))

	cd('/')
	cmo.createJDBCStore('JDBCStore_auto_2')
	cd('/JDBCStores/JDBCStore_auto_2')
	cmo.setDataSource(getMBean('/SystemResources/EAIJMSDataSource'))
	cmo.setPrefixName('JDBCStore2')

	set('Targets',jarray.array([ObjectName('com.bea:Name=OSB2,Type=Server')], ObjectName))

	cd('/')
	cmo.createJDBCStore('JDBCStore_auto_3')
	cd('/JDBCStores/JDBCStore_auto_3')
	cmo.setDataSource(getMBean('/SystemResources/EAIJMSDataSource'))
	cmo.setPrefixName('JDBCStore3')

	set('Targets',jarray.array([ObjectName('com.bea:Name=OSB3,Type=Server')], ObjectName))

	cd('/')
	cmo.createJDBCStore('JDBCStore_auto_4')
	cd('/JDBCStores/JDBCStore_auto_4')
	cmo.setDataSource(getMBean('/SystemResources/EAIJMSDataSource'))
	cmo.setPrefixName('JDBCStore4')
	set('Targets',jarray.array([ObjectName('com.bea:Name=OSB4,Type=Server')], ObjectName))

	################  end of JDBC Stores ####################

	############Set Persistent Stores for all the JMS Servers for cluster

	cd('/Deployments/WseeJaxwsJmsServer_auto_1')
	cmo.setPersistentStore(getMBean('/JDBCStores/WseeJaxwsJDBCStore_auto_1'))


	cd('/Deployments/WseeJaxwsJmsServer_auto_2')
	cmo.setPersistentStore(getMBean('/JDBCStores/WseeJaxwsJDBCStore_auto_2'))


	cd('/Deployments/WseeJaxwsJmsServer_auto_3')
	cmo.setPersistentStore(getMBean('/JDBCStores/WseeJaxwsJDBCStore_auto_3'))


	cd('/Deployments/WseeJaxwsJmsServer_auto_4')
	cmo.setPersistentStore(getMBean('/JDBCStores/WseeJaxwsJDBCStore_auto_4'))


	cd('/Deployments/WseeJmsServer_auto_1')
	cmo.setPersistentStore(getMBean('/JDBCStores/WseeJDBCStore_auto_1'))


	cd('/Deployments/WseeJmsServer_auto_2')
	cmo.setPersistentStore(getMBean('/JDBCStores/WseeJDBCStore_auto_2'))


	cd('/Deployments/WseeJmsServer_auto_3')
	cmo.setPersistentStore(getMBean('/JDBCStores/WseeJDBCStore_auto_3'))


	cd('/Deployments/WseeJmsServer_auto_4')
	cmo.setPersistentStore(getMBean('/JDBCStores/WseeJDBCStore_auto_4'))


	cd('/Deployments/WseeJmsServer_auto_5')
	cmo.setPersistentStore(getMBean('/JDBCStores/WseeJDBCStore_auto_5'))


	cd('/Deployments/WseeJmsServer_auto_6')
	cmo.setPersistentStore(getMBean('/JDBCStores/WseeJDBCStore_auto_6'))


	cd('/Deployments/WseeJmsServer_auto_7')
	cmo.setPersistentStore(getMBean('/JDBCStores/WseeJDBCStore_auto_7'))


	cd('/Deployments/WseeJmsServer_auto_8')
	cmo.setPersistentStore(getMBean('/JDBCStores/WseeJDBCStore_auto_8'))


	cd('/Deployments/UMSJMSServer_auto_1')
	cmo.setPersistentStore(getMBean('/JDBCStores/UMSJMSJDBCStore_auto_1'))



	cd('/Deployments/UMSJMSServer_auto_2')
	cmo.setPersistentStore(getMBean('/JDBCStores/UMSJMSJDBCStore_auto_2'))



	cd('/Deployments/UMSJMSServer_auto_3')
	cmo.setPersistentStore(getMBean('/JDBCStores/UMSJMSJDBCStore_auto_3'))



	cd('/Deployments/UMSJMSServer_auto_4')
	cmo.setPersistentStore(getMBean('/JDBCStores/UMSJMSJDBCStore_auto_4'))



	cd('/Deployments/BPMJMSServer_auto_1')
	cmo.setPersistentStore(getMBean('/JDBCStores/BPMJMSJDBCStore_auto_1'))



	cd('/Deployments/BPMJMSServer_auto_2')
	cmo.setPersistentStore(getMBean('/JDBCStores/BPMJMSJDBCStore_auto_2'))



	cd('/Deployments/BPMJMSServer_auto_3')
	cmo.setPersistentStore(getMBean('/JDBCStores/BPMJMSJDBCStore_auto_3'))



	cd('/Deployments/BPMJMSServer_auto_4')
	cmo.setPersistentStore(getMBean('/JDBCStores/BPMJMSJDBCStore_auto_4'))



	cd('/Deployments/SOAJMSServer_auto_1')
	cmo.setPersistentStore(getMBean('/JDBCStores/SOAJMSJDBCStore_auto_1'))


	cd('/Deployments/SOAJMSServer_auto_2')
	cmo.setPersistentStore(getMBean('/JDBCStores/SOAJMSJDBCStore_auto_2'))


	cd('/Deployments/SOAJMSServer_auto_3')
	cmo.setPersistentStore(getMBean('/JDBCStores/SOAJMSJDBCStore_auto_3'))


	cd('/Deployments/SOAJMSServer_auto_4')
	cmo.setPersistentStore(getMBean('/JDBCStores/SOAJMSJDBCStore_auto_4'))


	cd('/Deployments/wlsbJMSServer_auto_1')
	cmo.setPersistentStore(getMBean('/JDBCStores/JDBCStore_auto_1'))




	cd('/Deployments/wlsbJMSServer_auto_2')
	cmo.setPersistentStore(getMBean('/JDBCStores/JDBCStore_auto_2'))




	cd('/Deployments/wlsbJMSServer_auto_3')

	cmo.setPersistentStore(getMBean('/JDBCStores/JDBCStore_auto_3'))




	cd('/Deployments/wlsbJMSServer_auto_4')
	cmo.setPersistentStore(getMBean('/JDBCStores/JDBCStore_auto_4'))


	##### Set the persistent stores for all SAF agents
	cd('/SAFAgents/ReliableWseeJaxwsSAFAgent_MS1')
	cmo.setStore(getMBean('/JDBCStores/WseeJaxwsJDBCStore_auto_1'))


	cd('/SAFAgents/ReliableWseeJaxwsSAFAgent_MS2')
	cmo.setStore(getMBean('/JDBCStores/WseeJaxwsJDBCStore_auto_2'))


	cd('/SAFAgents/ReliableWseeJaxwsSAFAgent_MS3')
	cmo.setStore(getMBean('/JDBCStores/WseeJaxwsJDBCStore_auto_3'))


	cd('/SAFAgents/ReliableWseeJaxwsSAFAgent_MS4')
	cmo.setStore(getMBean('/JDBCStores/WseeJaxwsJDBCStore_auto_4'))

	#################DESTROY ALL THE FILE STORES

	cd('/')
	cmo.destroyFileStore(getMBean('/FileStores/WseeJaxwsFileStore_auto_1'))
	cmo.destroyFileStore(getMBean('/FileStores/WseeJaxwsFileStore_auto_2'))
	cmo.destroyFileStore(getMBean('/FileStores/WseeJaxwsFileStore_auto_3'))
	cmo.destroyFileStore(getMBean('/FileStores/WseeJaxwsFileStore_auto_4'))

	cmo.destroyFileStore(getMBean('/FileStores/WseeFileStore_auto_1'))
	cmo.destroyFileStore(getMBean('/FileStores/WseeFileStore_auto_2'))
	cmo.destroyFileStore(getMBean('/FileStores/WseeFileStore_auto_3'))
	cmo.destroyFileStore(getMBean('/FileStores/WseeFileStore_auto_4'))
	cmo.destroyFileStore(getMBean('/FileStores/WseeFileStore_auto_5'))
	cmo.destroyFileStore(getMBean('/FileStores/WseeFileStore_auto_6'))
	cmo.destroyFileStore(getMBean('/FileStores/WseeFileStore_auto_7'))
	cmo.destroyFileStore(getMBean('/FileStores/WseeFileStore_auto_8'))

	cmo.destroyFileStore(getMBean('/FileStores/UMSJMSFileStore_auto_1'))
	cmo.destroyFileStore(getMBean('/FileStores/UMSJMSFileStore_auto_2'))
	cmo.destroyFileStore(getMBean('/FileStores/UMSJMSFileStore_auto_3'))
	cmo.destroyFileStore(getMBean('/FileStores/UMSJMSFileStore_auto_4'))

	cmo.destroyFileStore(getMBean('/FileStores/BPMJMSFileStore_auto_1'))
	cmo.destroyFileStore(getMBean('/FileStores/BPMJMSFileStore_auto_2'))
	cmo.destroyFileStore(getMBean('/FileStores/BPMJMSFileStore_auto_3'))
	cmo.destroyFileStore(getMBean('/FileStores/BPMJMSFileStore_auto_4'))

	cmo.destroyFileStore(getMBean('/FileStores/SOAJMSFileStore_auto_1'))
	cmo.destroyFileStore(getMBean('/FileStores/SOAJMSFileStore_auto_2'))
	cmo.destroyFileStore(getMBean('/FileStores/SOAJMSFileStore_auto_3'))
	cmo.destroyFileStore(getMBean('/FileStores/SOAJMSFileStore_auto_4'))

	cmo.destroyFileStore(getMBean('/FileStores/FileStore_auto_1'))
	cmo.destroyFileStore(getMBean('/FileStores/FileStore_auto_2'))
	cmo.destroyFileStore(getMBean('/FileStores/FileStore_auto_3'))
	cmo.destroyFileStore(getMBean('/FileStores/FileStore_auto_4'))

if sys.argv[1] == 'StandAlone':
	############# JDBC stores for STANDALONE ADMINSERVER
	cd('/')

	cmo.createJDBCStore('WseeJaxwsJDBCStore')
	cd('/JDBCStores/WseeJaxwsJDBCStore')
	cmo.setDataSource(getMBean('/SystemResources/EAIJMSDataSource'))
	cmo.setPrefixName('WseeJaxws')
	set('Targets',jarray.array([ObjectName('com.bea:Name=AdminServer,Type=Server')], ObjectName))

	cd('/')
	cmo.createJDBCStore('UMSJMSJDBCStore')
	cd('/JDBCStores/UMSJMSJDBCStore')
	cmo.setDataSource(getMBean('/SystemResources/EAIJMSDataSource'))
	cmo.setPrefixName('UMSJMS')
	set('Targets',jarray.array([ObjectName('com.bea:Name=AdminServer,Type=Server')], ObjectName))

	cd('/')
	cmo.createJDBCStore('SOAJMSJDBCStore')
	cd('/JDBCStores/SOAJMSJDBCStore')
	cmo.setDataSource(getMBean('/SystemResources/EAIJMSDataSource'))
	cmo.setPrefixName('SOAJMS')
	set('Targets',jarray.array([ObjectName('com.bea:Name=AdminServer,Type=Server')], ObjectName))

	cd('/')
	cmo.createJDBCStore('JDBCStore')
	cd('/JDBCStores/JDBCStore')
	cmo.setDataSource(getMBean('/SystemResources/EAIJMSDataSource'))
	cmo.setPrefixName('rmjdbcstore')
	set('Targets',jarray.array([ObjectName('com.bea:Name=AdminServer,Type=Server')], ObjectName))

	cd('/')
	cmo.createJDBCStore('WseeJDBCStore')
	cd('/JDBCStores/WseeJDBCStore')
	cmo.setDataSource(getMBean('/SystemResources/EAIJMSDataSource'))
	cmo.setPrefixName('Wsee')
	set('Targets',jarray.array([ObjectName('com.bea:Name=AdminServer,Type=Server')], ObjectName))

	cd('/')
	cmo.createJDBCStore('BPMJMSJDBCStore')
	cd('/JDBCStores/BPMJMSJDBCStore')
	cmo.setDataSource(getMBean('/SystemResources/EAIJMSDataSource'))
	cmo.setPrefixName('BPMJMS')
	set('Targets',jarray.array([ObjectName('com.bea:Name=AdminServer,Type=Server')], ObjectName))

	#### end of creating jdbc stores

	############Set Persistent Stores for all the JMS Servers

	cd('/Deployments/WseeJaxwsJmsServer')
	cmo.setPersistentStore(getMBean('/JDBCStores/WseeJaxwsJDBCStore'))


	cd('/Deployments/UMSJMSServer')
	cmo.setPersistentStore(getMBean('/JDBCStores/UMSJMSJDBCStore'))


	cd('/Deployments/BPMJMSServer')
	cmo.setPersistentStore(getMBean('/JDBCStores/BPMJMSJDBCStore'))


	cd('/Deployments/SOAJMSServer')
	cmo.setPersistentStore(getMBean('/JDBCStores/SOAJMSJDBCStore'))


	cd('/Deployments/wlsbJMSServer')
	cmo.setPersistentStore(getMBean('/JDBCStores/JDBCStore'))


	cd('/Deployments/WseeJmsServer')
	cmo.setPersistentStore(getMBean('/JDBCStores/WseeJDBCStore'))

	##### Set the persistent stores for all SAF agents
	cd('/SAFAgents/ReliableWseeJaxwsSAFAgent')
	cmo.setStore(getMBean('/JDBCStores/WseeJaxwsJDBCStore'))

	cd('/SAFAgents/ReliableWseeSAFAgent')
	cmo.setStore(getMBean('/JDBCStores/WseeJDBCStore'))

	#################DESTROY ALL THE FILE STORES	

	cd('/')
	cmo.destroyFileStore(getMBean('/FileStores/WseeJaxwsFileStore'))
	cmo.destroyFileStore(getMBean('/FileStores/UMSJMSFileStore'))
	cmo.destroyFileStore(getMBean('/FileStores/SOAJMSFileStore'))
	cmo.destroyFileStore(getMBean('/FileStores/BPMJMSFileStore'))
	cmo.destroyFileStore(getMBean('/FileStores/WseeFileStore'))
	cmo.destroyFileStore(getMBean('/FileStores/FileStore'))

save()
activate()