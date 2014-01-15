from java.io import FileInputStream

propInputStream1 = FileInputStream("domain.properties")
domainProps = util.Properties()
domainProps.load(propInputStream1) 


adminURL='t3://'+domainProps.get('domain1.AdminIP')+':'+domainProps.get('domain1.AdminPort')
adminUserName='weblogic'
adminPassword=domainProps.get("domain1.AdminPasswd")
connect(adminUserName, adminPassword, adminURL)
server='AdminServer'
cd("Servers/"+server)
assign("AppDeployment", "JMS Reporting Provider", "Target", "AdminServer")
target=cmo
edit()
startEdit()

# SOADomain Datasource Configuration
DBURL= domainProps.getProperty("domain1.DBURL")
DBUSER_PREFIX=domainProps.getProperty("domain1.DBUSER_PREFIX")
DBPASSWORD=domainProps.getProperty("domain1.DBPASSWORD")

cd('/JDBCSystemResources/wlsbjmsrpDataSource/JDBCResource/wlsbjmsrpDataSource/JDBCDriverParams/wlsbjmsrpDataSource')
cmo.setPassword(DBUSER_PREFIX+'_OSB')       
cmo.setDriverName('  oracle.jdbc.OracleDriver')
cmo.setUrl(DBURL)

cd('/JDBCSystemResources/wlsbjmsrpDataSource/JDBCResource/wlsbjmsrpDataSource/JDBCDriverParams/wlsbjmsrpDataSource/Properties/wlsbjmsrpDataSource')
cmo.destroyProperty(getMBean('/JDBCSystemResources/wlsbjmsrpDataSource/JDBCResource/wlsbjmsrpDataSource/JDBCDriverParams/wlsbjmsrpDataSource/Properties/wlsbjmsrpDataSource/Properties/user'))
cmo.createProperty('user')

cd('/JDBCSystemResources/wlsbjmsrpDataSource/JDBCResource/wlsbjmsrpDataSource/JDBCDriverParams/wlsbjmsrpDataSource/Properties/wlsbjmsrpDataSource/Properties/user')
cmo.setValue(DBUSER_PREFIX+'_OSB')

cd('/JDBCSystemResources/wlsbjmsrpDataSource/JDBCResource/wlsbjmsrpDataSource/JDBCConnectionPoolParams/wlsbjmsrpDataSource')
cmo.setInitialCapacity(5)

cmo.setMaxCapacity(50)

cd('/SystemResources/wlsbjmsrpDataSource')
#set('Targets',jarray.array([ObjectName('com.bea:Name=OSBCluster,Type=Cluster')], ObjectName))

if sys.argv[1] == 'StandAlone':
	set('Targets',jarray.array([ObjectName('com.bea:Name=AdminServer,Type=Server')], ObjectName))
if sys.argv[1] == 'Cluster':
	set('Targets',jarray.array([ObjectName('com.bea:Name=AdminServer,Type=Server'), ObjectName('com.bea:Name=OSBCluster,Type=Cluster')], ObjectName))

cd('/JDBCSystemResources/mds-soa/JDBCResource/mds-soa/JDBCConnectionPoolParams/mds-soa')
cmo.setInitialCapacity(5)
cmo.setMaxCapacity(50)

cd('/JDBCSystemResources/mds-owsm/JDBCResource/mds-owsm/JDBCConnectionPoolParams/mds-owsm')
cmo.setMaxCapacity(50)

save()
activate()
disconnect()
