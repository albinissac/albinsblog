 
from java.io import FileInputStream
    
def updateConnectionPool():
    propInputStream = FileInputStream("domain.properties")
    configProps = Properties()
    configProps.load(propInputStream)     

    adminURL='t3://'+configProps.get('domain1.AdminIP')+':'+configProps.get('domain1.AdminPort')
    adminUserName='weblogic'
    adminPassword=configProps.get("domain1.AdminPasswd")

    connect(adminUserName, adminPassword, adminURL)

    connRetryFrequency=sys.argv[1]
    print 'Updating Frequency value to :',connRetryFrequency
    server='AdminServer'
    cd("Servers/"+server)
    edit()
    startEdit()
    cd('JDBCSystemResources')
    target=cmo
    pwd()
    #ls()

    allDS=cmo.getJDBCSystemResources()
    for tmpDS in allDS:
           dsName=tmpDS.getName();
           cd('/JDBCSystemResources/'+dsName+'/JDBCResource/'+dsName+'/JDBCDataSourceParams/'+dsName)
           print 'DataSource Name:',dsName
           print 'cmo.getDataSourceList()',cmo.getDataSourceList()
           multiDS=cmo.getDataSourceList();
           if multiDS == None:
           	cd('/JDBCSystemResources/'+dsName+'/JDBCResource/'+dsName+'/JDBCConnectionPoolParams/'+dsName)
           	cmo.setConnectionCreationRetryFrequencySeconds(int(connRetryFrequency))
           	print("*** CONGRATES !!! Updated frequency for the DataSource: ", dsName)
           print ('')
           print ('')
    save()
    activate()
    
 
    print '========================================='     
    	   
    disconnect()

def main():
 updateConnectionPool();   
main()