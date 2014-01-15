from java.io import FileInputStream
    

def createJDBCResources(dsURL,propFile):
    edit()
    startEdit()
    propInputStream = FileInputStream(propFile)
    configProps = Properties()
    configProps.load(propInputStream)     

    totalDataSource_to_Create=configProps.get("domain1.total.DS")
     
    server='AdminServer'
    cd("Servers/"+server)
    target=cmo
    cd("../..")
    print '========================================='
    print 'Creating DataSource....'
    print '========================================='
    dsTestQuery=configProps.get("domain1.connectionpool.test.query")
    dsDriverName=configProps.get("domain1.connectionpool.driver.class")
    
    i=1
    while (i <= int(totalDataSource_to_Create)) :
           #try:        
           cd('/')            
           prefix = configProps.get("domain1.prefix."+ str(i)) 
           poolName = configProps.get("domain1."+prefix+".connectionpool.name."+ str(i))
           dsUserName = configProps.get("domain1."+prefix+".connectionpool.username."+ str(i))
           dsPassword = configProps.get("domain1."+prefix+".connectionpool.password."+ str(i))
           initCapacity = configProps.get("domain1."+prefix+".connectionpool.initCapacity."+ str(i))
           maxCapacity = configProps.get("domain1."+prefix+".connectionpool.maxCapacity."+ str(i))
           dsName = configProps.get("domain1."+prefix+".datasource.name."+ str(i))
           jndiname = configProps.get("domain1."+prefix+".datasource.jndi.name."+ str(i))
           datasourceTargets = configProps.get("domain1."+prefix+".datasource.target."+ str(i)).split(",")
    
           print 'prefix',prefix 
           print 'poolName',poolName 
           print 'dsUserName',dsUserName 
           print 'dsPassword',dsPassword 
           print 'initCapacity',initCapacity 
           print 'maxCapacity',maxCapacity 
           print 'dsName',dsName 
           print 'jndiname',jndiname 
           print 'datasourceTargets',datasourceTargets

           print 'Creating DataSource: ',dsName,' ....'
           print("")       
           print("*** Creating JDBC with property prefix " + prefix)    
           
           myResourceName = dsName       
           print("Here is the Resource Name: " + myResourceName)       
           jdbcSystemResource = create(myResourceName,"JDBCSystemResource")       
           myFile = jdbcSystemResource.getDescriptorFileName()       
           print ("HERE IS THE JDBC FILE NAME: " + myFile)           
           jdbcResource = jdbcSystemResource.getJDBCResource()       
           jdbcResource.setName(myResourceName)    
           
           # Create the DataSource Params       
           dpBean = jdbcResource.getJDBCDataSourceParams()       
           myName=jndiname   
           dpBean.setJNDINames([myName])  
           #dpBean.setGlobalTransactionsProtocol('EmulateTwoPhaseCommit')   
           dpBean.setGlobalTransactionsProtocol('None')
           # Create the Driver Params       
           drBean = jdbcResource.getJDBCDriverParams()       
           drBean.setPassword(dsPassword)       
           drBean.setUrl(dsURL)       
           drBean.setDriverName(dsDriverName)       
           propBean = drBean.getProperties()
           driverProps = Properties()       
           driverProps.setProperty("user",dsUserName)       
           e = driverProps.propertyNames()       
           while e.hasMoreElements() :              
               propName = e.nextElement()              
               myBean = propBean.createProperty(propName)             
               myBean.setValue(driverProps.getProperty(propName))    
           
           # Create the ConnectionPool Params       
           ppBean = jdbcResource.getJDBCConnectionPoolParams()       
           ppBean.setInitialCapacity(int(initCapacity))       
           ppBean.setMaxCapacity(int(maxCapacity))       
           ppBean.setTestConnectionsOnReserve(true)       
           ppBean.setTestTableName('SQL SELECT 1 FROM DUAL')
           #ppBean.setCapacityIncrement(int(props.getProperty(prefix+"CapacityIncrement")))       
           #if not props.getProperty(prefix+"ShrinkPeriodMinutes") == None:      
           #ppBean.setShrinkFrequencySeconds(int(props.getProperty(prefix+"ShrinkPeriodMinutes")))
           #if not props.getProperty(prefix+"TestTableName") == None:              
           #ppBean.setTestTableName(props.getProperty(prefix+"TestTableName"))       
           #if not props.getProperty(prefix+"LoginDelaySeconds") == None:      
           #ppBean.setLoginDelaySeconds(int(props.getProperty(prefix+"LoginDelaySeconds")))    
           
           # Adding KeepXaConnTillTxComplete to help with in-doubt transactions.       
           xaParams = jdbcResource.getJDBCXAParams()       
           xaParams.setKeepXaConnTillTxComplete(1)    
    
           # Add Target
           for datasourceTarget in datasourceTargets:
                print 'DataSourceTargets',datasourceTargets
                print 'DataSourceTarget',datasourceTarget
                if datasourceTarget=='':
                   print ''
                else:
                   jdbcSystemResource.addTarget(getMBean(datasourceTarget))   		   
           
            
           print 'DataSource: ',dsName,', has been created Successfully !!!'
           print '========================================='     
           #except:
           #print '***** CANNOT CREATE DATASOURCE !!! Check If the DataSource With the Name : ' , dsName ,' Alreday exists or NOT...'
           #print ''
           i = i + 1
    
    print '========================================='
    save()
    activate()    


    
def main():
    propInputStream1 = FileInputStream("domain.properties")
    domainProps = util.Properties()
    domainProps.load(propInputStream1) 

    if sys.argv[1] == 'SOACoreDomain':

        adminURL='t3://'+domainProps.get('domain1.AdminIP')+':'+domainProps.get('domain1.AdminPort')
        adminUserName='weblogic'
        adminPassword=domainProps.get("domain1.AdminPasswd")
        connect(adminUserName, adminPassword, adminURL)


        createJDBCResources(domainProps.get('domain1.DBURL'),'ResourceAdapter_SOACoreDomain.properties');   

        print 'Successfully created JDBC resources for SOACoreDomain'

        disconnect()

    if sys.argv[1] == 'SOAExtDomain':
        adminURL='t3://'+domainProps.get('domain2.AdminIP')+':'+domainProps.get('domain2.AdminPort')
        adminUserName='weblogic'
        adminPassword=domainProps.get("domain2.AdminPasswd")
        connect(adminUserName, adminPassword, adminURL)

        createJDBCResources(domainProps.get('domain2.DBURL'),'ResourceAdapter_SOAExtDomain.properties');

        disconnect()    
        print 'Successfully created JDBC resources for SOAExtDomain'    
main()