from java.io import FileInputStream

TargetServerName='AdminServer'
 
#Connect
#The directory of the SOA binaries
#/app/oracle/products/11g/fmw/Oracle_SOA
soaHome=os.environ["SOAHOME"]
print "SOAHOME="+soaHome 

#The directory of the domain configuration
#/app/oracle/products/11g/admin/domains 
wlsDomain=os.environ["WLSDOMAIN"]
print "WLSDOMAIN="+wlsDomain
 
appPathDB=soaHome+'/soa/connectors/DbAdapter.rar'
appNameDB='DbAdapter'
moduleOverrideNameDB=appNameDB+'.rar'

appPathFTP=soaHome+'/soa/connectors/FtpAdapter.rar'
appNameFTP='FtpAdapter'
moduleOverrideNameFTP=appNameFTP+'.rar'

appPathMQ=soaHome+'/soa/connectors/MQSeriesAdapter.rar'
appNameMQ='MQSeriesAdapter'
moduleOverrideNameMQ=appNameMQ+'.rar'

moduleDescriptorName='META-INF/weblogic-ra.xml'

OMJNDIName = 'eis/DB/OM'

OMXADataSourceName = 'eai/ds/EAIReference'

EAISOAJNDIName = 'eis/DB/EAISOA'

EAISOAXADataSourceName = 'eai/ds/EAISOA'


EAIXREFJNDIName = 'eis/DB/XRef'

EAIXREFXADataSourceName = 'eai/ds/EAIXRef'

transactionSupport='LocalTransaction'

ftpJNDIName='eis/Ftp/ProductRefXML'

mqJNDIName='eis/MQ/MQSeriesAdapterRemoteCRMtoEAI'
mqJNDIName1='eis/MQ/MQSeriesAdapterRemote'

def createDBConnectionFactory(propsFile,domainName):
        propInputStream = FileInputStream(propsFile)
        configProps1 = Properties()
        configProps1.load(propInputStream)  
        planPathDB=configProps1.get('global.resource.deployment.plan.path')+'/'+domainName+'_PlanDB.xml'
        edit()
        startEdit()
        startApplication(appNameDB)
        myPlanDB=loadApplication(appPathDB, planPathDB)
        makeDeploymentPlanVariable(myPlanDB, 'ConnectionInstance_eis/DB/OM_JNDIName_13102979357209', OMJNDIName , '/weblogic-connector/outbound-resource-adapter/connection-definition-group/[connection-factory-interface="javax.resource.cci.ConnectionFactory"]/connection-instance/[jndi-name="'+OMJNDIName+'"]/jndi-name',moduleOverrideNameDB)
        
        makeDeploymentPlanVariable(myPlanDB, 'ConfigProperty_xADataSourceName_Value_13102979357210', OMXADataSourceName,'/weblogic-connector/outbound-resource-adapter/connection-definition-group/[connection-factory-interface="javax.resource.cci.ConnectionFactory"]/connection-instance/[jndi-name="'+OMJNDIName+'"]/connection-properties/properties/property/[name="xADataSourceName"]/value',moduleOverrideNameDB)
        
        makeDeploymentPlanVariable(myPlanDB, 'ConnectionInstance_eis/DB/EAISOA_JNDIName_13102979357211', EAISOAJNDIName , '/weblogic-connector/outbound-resource-adapter/connection-definition-group/[connection-factory-interface="javax.resource.cci.ConnectionFactory"]/connection-instance/[jndi-name="'+EAISOAJNDIName+'"]/jndi-name',moduleOverrideNameDB)
        
        makeDeploymentPlanVariable(myPlanDB, 'ConfigProperty_xADataSourceName_Value_13102979357212', EAISOAXADataSourceName,'/weblogic-connector/outbound-resource-adapter/connection-definition-group/[connection-factory-interface="javax.resource.cci.ConnectionFactory"]/connection-instance/[jndi-name="'+EAISOAJNDIName+'"]/connection-properties/properties/property/[name="xADataSourceName"]/value',moduleOverrideNameDB)

        
        makeDeploymentPlanVariable(myPlanDB, 'ConnectionInstance_eis/DB/XRef_JNDIName_13102979357211', EAIXREFJNDIName , '/weblogic-connector/outbound-resource-adapter/connection-definition-group/[connection-factory-interface="javax.resource.cci.ConnectionFactory"]/connection-instance/[jndi-name="'+EAIXREFJNDIName+'"]/jndi-name',moduleOverrideNameDB)
        
        makeDeploymentPlanVariable(myPlanDB, 'ConfigProperty_xADataSourceName_Value_13102979357213', EAIXREFXADataSourceName,'/weblogic-connector/outbound-resource-adapter/connection-definition-group/[connection-factory-interface="javax.resource.cci.ConnectionFactory"]/connection-instance/[jndi-name="'+EAIXREFJNDIName+'"]/connection-properties/properties/property/[name="xADataSourceName"]/value',moduleOverrideNameDB)
        
        makeDeploymentPlanVariable(myPlanDB, 'ConnectionDefinitionProperties_TransactionSupport_13123107532320', transactionSupport,'/weblogic-connector/outbound-resource-adapter/connection-definition-group/[connection-factory-interface="javax.resource.cci.ConnectionFactory"]/connection-instance/[jndi-name="'+OMJNDIName+'"]/connection-properties/transaction-support',moduleOverrideNameDB)

        makeDeploymentPlanVariable(myPlanDB, 'ConnectionDefinitionProperties_TransactionSupport_13123107532320', transactionSupport,'/weblogic-connector/outbound-resource-adapter/connection-definition-group/[connection-factory-interface="javax.resource.cci.ConnectionFactory"]/connection-instance/[jndi-name="'+EAISOAJNDIName+'"]/connection-properties/transaction-support',moduleOverrideNameDB)
        
        makeDeploymentPlanVariable(myPlanDB, 'ConnectionDefinitionProperties_TransactionSupport_13123107532320', transactionSupport,'/weblogic-connector/outbound-resource-adapter/connection-definition-group/[connection-factory-interface="javax.resource.cci.ConnectionFactory"]/connection-instance/[jndi-name="'+EAIXREFJNDIName+'"]/connection-properties/transaction-support',moduleOverrideNameDB)
        
        myPlanDB.save();
        save();
        cd('/AppDeployments/DbAdapter/Targets');
        updateApplication(appNameDB, planPathDB);
        #redeploy(appNameDB, planPathDB,targets=cmo.getTargets());
        activate(block='true');
       
    
def createFTPConnectionFactory(propsFile,domainName):
        propInputStream = FileInputStream(propsFile)
        configProps1 = Properties()
        configProps1.load(propInputStream)  

        planPathFTP=configProps1.get('global.resource.deployment.plan.path')+'/'+domainName+'_PlanFTP.xml'

        ftpHost=configProps1.get('domain1.resource.ftpHost')

        ftpUserName=configProps1.get('domain1.resource.ftpUserName')

        ftpPassword=configProps1.get('domain1.resource.ftpPassword')

        edit()
        startEdit()
        startApplication(appNameFTP)
        myPlanFTP=loadApplication(appPathFTP, planPathFTP)
        makeDeploymentPlanVariable(myPlanFTP, 'ConnectionInstance_eis/Ftp/FtpPRD_JNDIName', ftpJNDIName, '/weblogic-connector/outbound-resource-adapter/connection-definition-group/[connection-factory-interface="javax.resource.cci.ConnectionFactory"]/connection-instance/[jndi-name="'+ftpJNDIName+'"]/jndi-name',moduleOverrideNameFTP)        
        makeDeploymentPlanVariable(myPlanFTP, 'ConfigProperty_useSftp_Value_FtpPRD', 'false', '/weblogic-connector/outbound-resource-adapter/connection-definition-group/[connection-factory-interface="javax.resource.cci.ConnectionFactory"]/connection-instance/[jndi-name="'+ftpJNDIName+'"]/connection-properties/properties/property/[name="useSftp"]/value',moduleOverrideNameFTP)
          
        makeDeploymentPlanVariable(myPlanFTP, 'ConfigProperty_host_Value_FtpPRD', ftpHost,   '/weblogic-connector/outbound-resource-adapter/connection-definition-group/[connection-factory-interface="javax.resource.cci.ConnectionFactory"]/connection-instance/[jndi-name="'+ftpJNDIName+'"]/connection-properties/properties/property/[name="host"]/value',moduleOverrideNameFTP)

        makeDeploymentPlanVariable(myPlanFTP, 'ConfigProperty_UserName_Value_FtpPRD', ftpUserName, '/weblogic-connector/outbound-resource-adapter/connection-definition-group/[connection-factory-interface="javax.resource.cci.ConnectionFactory"]/connection-instance/[jndi-name="'+ftpJNDIName+'"]/connection-properties/properties/property/[name="username"]/value',moduleOverrideNameFTP)

        makeDeploymentPlanVariable(myPlanFTP, 'ConfigProperty_password_Value_FtpPRD', ftpPassword, '/weblogic-connector/outbound-resource-adapter/connection-definition-group/[connection-factory-interface="javax.resource.cci.ConnectionFactory"]/connection-instance/[jndi-name="'+ftpJNDIName+'"]/connection-properties/properties/property/[name="password"]/value',moduleOverrideNameFTP)
        
        myPlanFTP.save();
        save();
        cd('/AppDeployments/FtpAdapter/Targets');
        updateApplication(appNameFTP, planPathFTP);
        #redeploy(appNameFTP, planPathFTP,targets=cmo.getTargets());
        activate(block='true');
 
def createMQConnectionFactory(propsFiile,domainName):
        propInputStream = FileInputStream(propsFiile)
        configProps1 = Properties()
        configProps1.load(propInputStream)  
        planPathMQ=configProps1.get('global.resource.deployment.plan.path')+'/'+domainName+'_PlanMQ.xml'

        startApplication(appNameMQ)
        mqQueueManager=configProps1.get('domain1.resource.mqQueueManager')

        mqHostName=configProps1.get('domain1.resource.mqHost')

        totalMq_to_Create=configProps1.get("domain1.total.mq.nodes")

        print '========================================='
        print 'Creating MQ Connection Factory....'
        print '========================================='

        edit()
        startEdit()

# This is for Siebel Queue Channels
        i=1 
        prefix = configProps1.get("domain1.mq.prefix."+ str(1)) 
        while (i <= int(totalMq_to_Create)) :
            poolName = configProps1.get("domain1."+prefix+".resource.mqport.config."+ str(i))
        
            MqPort=configProps1.get("domain1."+prefix+".resource.mqport.config."+ str(i))
        
            mqChannelName=configProps1.get("domain1."+prefix+".resource.mqChannel.config."+ str(i))
        
            targetsValue=configProps1.get("domain1."+prefix+".resource.targets.config."+ str(i))
        
        
            myPlanMQ=loadApplication(appPathMQ, planPathMQ)
            makeDeploymentPlanVariable(myPlanMQ, 'ConnectionInstance_eis_MQ_MQSeriesAdapterRemoteCRMtoEAI_JNDIName'+prefix+ str(i), mqJNDIName, '/weblogic-connector/outbound-resource-adapter/connection-definition-group/[connection-factory-interface="javax.resource.cci.ConnectionFactory"]/connection-instance/[jndi-name="'+mqJNDIName+'"]/jndi-name',moduleOverrideNameMQ)        
        
            makeDeploymentPlanVariable(myPlanMQ, 'ConfigProperty_host_Value_mqQueueManagerPRD'+prefix+ str(i), mqQueueManager,   '/weblogic-connector/outbound-resource-adapter/connection-definition-group/[connection-factory-interface="javax.resource.cci.ConnectionFactory"]/connection-instance/[jndi-name="'+mqJNDIName+'"]/connection-properties/properties/property/[name="queueManagerName"]/value',moduleOverrideNameMQ)
        
            makeDeploymentPlanVariable(myPlanMQ, 'ConfigProperty_password_Value_mqHostNamePRD'+prefix+ str(i), mqHostName, '/weblogic-connector/outbound-resource-adapter/connection-definition-group/[connection-factory-interface="javax.resource.cci.ConnectionFactory"]/connection-instance/[jndi-name="'+mqJNDIName+'"]/connection-properties/properties/property/[name="hostName"]/value',moduleOverrideNameMQ)
        
            makeDeploymentPlanVariable(myPlanMQ, 'ConfigProperty_password_Value_MqPortPRD'+prefix+ str(i), MqPort, '/weblogic-connector/outbound-resource-adapter/connection-definition-group/[connection-factory-interface="javax.resource.cci.ConnectionFactory"]/connection-instance/[jndi-name="'+mqJNDIName+'"]/connection-properties/properties/property/[name="portNumber"]/value',moduleOverrideNameMQ)
        
            makeDeploymentPlanVariable(myPlanMQ, 'ConfigProperty_password_Value_mqChannelNamePRD'+prefix+ str(i), mqChannelName, '/weblogic-connector/outbound-resource-adapter/connection-definition-group/[connection-factory-interface="javax.resource.cci.ConnectionFactory"]/connection-instance/[jndi-name="'+mqJNDIName+'"]/connection-properties/properties/property/[name="channelName"]/value',moduleOverrideNameMQ)
        
            #makeDeploymentPlanVariable(myPlanMQ, 'ConfigProperty_password_Value_mqInitialCapacityPRD'+prefix+ str(i), '5', '/weblogic-connector/outbound-resource-adapter/connection-definition-group/[connection-factory-interface="javax.resource.cci.ConnectionFactory"]/connection-instance/[jndi-name="'+mqJNDIName+'"]/connection-properties/pool-params/initial-capacity',moduleOverrideNameMQ)

            #makeDeploymentPlanVariable(myPlanMQ, 'ConfigProperty_password_Value_mqTestConnOnReservePRD'+prefix+ str(i), 'true', '/weblogic-connector/outbound-resource-adapter/connection-definition-group/[connection-factory-interface="javax.resource.cci.ConnectionFactory"]/connection-instance/[jndi-name="'+mqJNDIName+'"]/connection-properties/pool-params/test-connections-on-reserve',moduleOverrideNameMQ)

            myPlanMQ.save();
            save();
            cd('/AppDeployments/MQSeriesAdapter/Targets');
            updateApplication(appNameMQ, planPathMQ);
            i = i + 1

# This is for non siebel Queue channels

        i=1
        prefix = configProps1.get("domain1.mq.prefix."+ str(2)) 
        while (i <= int(totalMq_to_Create)) :
            poolName = configProps1.get("domain1."+prefix+".resource.mqport.config."+ str(i))
        
            MqPort=configProps1.get("domain1."+prefix+".resource.mqport.config."+ str(i))
        
            mqChannelName=configProps1.get("domain1."+prefix+".resource.mqChannel.config."+ str(i))
        
            targetsValue=configProps1.get("domain1."+prefix+".resource.targets.config."+ str(i))
        
            myPlanMQ=loadApplication(appPathMQ, planPathMQ)
            makeDeploymentPlanVariable(myPlanMQ, 'ConnectionInstance_eis_MQSeriesAdapterRemote_JNDINameNSieb'+prefix+ str(i), mqJNDIName1, '/weblogic-connector/outbound-resource-adapter/connection-definition-group/[connection-factory-interface="javax.resource.cci.ConnectionFactory"]/connection-instance/[jndi-name="'+mqJNDIName1+'"]/jndi-name',moduleOverrideNameMQ)        
        
            makeDeploymentPlanVariable(myPlanMQ, 'ConfigProperty_host_Value_mqQueueManagerPRDNSieb'+prefix+ str(i), mqQueueManager,   '/weblogic-connector/outbound-resource-adapter/connection-definition-group/[connection-factory-interface="javax.resource.cci.ConnectionFactory"]/connection-instance/[jndi-name="'+mqJNDIName1+'"]/connection-properties/properties/property/[name="queueManagerName"]/value',moduleOverrideNameMQ)
        
            makeDeploymentPlanVariable(myPlanMQ, 'ConfigProperty_password_Value_mqHostNamePRDNSieb'+prefix+ str(i), mqHostName, '/weblogic-connector/outbound-resource-adapter/connection-definition-group/[connection-factory-interface="javax.resource.cci.ConnectionFactory"]/connection-instance/[jndi-name="'+mqJNDIName1+'"]/connection-properties/properties/property/[name="hostName"]/value',moduleOverrideNameMQ)
        
            makeDeploymentPlanVariable(myPlanMQ, 'ConfigProperty_password_Value_MqPortPRDNSieb'+prefix+ str(i), MqPort, '/weblogic-connector/outbound-resource-adapter/connection-definition-group/[connection-factory-interface="javax.resource.cci.ConnectionFactory"]/connection-instance/[jndi-name="'+mqJNDIName1+'"]/connection-properties/properties/property/[name="portNumber"]/value',moduleOverrideNameMQ)
        
            makeDeploymentPlanVariable(myPlanMQ, 'ConfigProperty_password_Value_mqChannelNamePRDNSieb'+prefix+ str(i), mqChannelName, '/weblogic-connector/outbound-resource-adapter/connection-definition-group/[connection-factory-interface="javax.resource.cci.ConnectionFactory"]/connection-instance/[jndi-name="'+mqJNDIName1+'"]/connection-properties/properties/property/[name="channelName"]/value',moduleOverrideNameMQ)        

            #makeDeploymentPlanVariable(myPlanMQ, 'ConfigProperty_password_Value_mqInitialCapacityPRD'+prefix+ str(i), '5', '/weblogic-connector/outbound-resource-adapter/connection-definition-group/[connection-factory-interface="javax.resource.cci.ConnectionFactory"]/connection-instance/[jndi-name="'+mqJNDIName1+'"]/connection-properties/pool-params/initial-capacity',moduleOverrideNameMQ)

            #makeDeploymentPlanVariable(myPlanMQ, 'ConfigProperty_password_Value_mqTestConnOnReservePRD'+prefix+ str(i), 'true', '/weblogic-connector/outbound-resource-adapter/connection-definition-group/[connection-factory-interface="javax.resource.cci.ConnectionFactory"]/connection-instance/[jndi-name="'+mqJNDIName1+'"]/connection-properties/pool-params/test-connections-on-reserve',moduleOverrideNameMQ)

            myPlanMQ.save();
            save();
            cd('/AppDeployments/MQSeriesAdapter/Targets');
            updateApplication(appNameMQ, planPathMQ);
            i = i + 1



        #redeploy(appNameFTP, planPathMQ,targets=cmo.getTargets());
        activate(block='true');
 
def makeDeploymentPlanVariable(wlstPlan, name, value, xpath,overrideName, origin='planbased'):
    wlstPlan.destroyVariable(name)
    wlstPlan.destroyVariableAssignment(name, overrideName, moduleDescriptorName)
    variableAssignment = wlstPlan.createVariableAssignment(name, overrideName, moduleDescriptorName)
    variableAssignment.setXpath(xpath)
    variableAssignment.setOrigin(origin)
    wlstPlan.createVariable(name, value)
    print 'moduleDescriptorName=',moduleDescriptorName

 
def main():
    #DOMAIN1
    adminserverDir = File(wlsDomain+'/deployplan')
    bool = adminserverDir.mkdirs()
    
    propInputStream1 = FileInputStream("domain.properties")
    domainProps = util.Properties()
    domainProps.load(propInputStream1)

    if sys.argv[1] == 'SOACoreDomain':

       adminURL='t3://'+domainProps.get('domain1.AdminIP')+':'+domainProps.get('domain1.AdminPort')
       adminUserName='weblogic'
       adminPassword=domainProps.get("domain1.AdminPasswd")

       connect(adminUserName, adminPassword, adminURL)

       createDBConnectionFactory("ResourceAdapter_SOACoreDomain.properties",'SOACoreDomain')
       createFTPConnectionFactory("ResourceAdapter_SOACoreDomain.properties",'SOACoreDomain')
       createMQConnectionFactory("ResourceAdapter_SOACoreDomain.properties",'SOACoreDomain')
       disconnect()

    #DOMAIN2

    if sys.argv[1] == 'SOAExtDomain':
       adminURL='t3://'+domainProps.get('domain2.AdminIP')+':'+domainProps.get('domain2.AdminPort')
       adminUserName='weblogic'
       adminPassword=domainProps.get("domain2.AdminPasswd")
       connect(adminUserName, adminPassword, adminURL)

       createDBConnectionFactory("ResourceAdapter_SOAExtDomain.properties",'SOAExtDomain')
       createFTPConnectionFactory("ResourceAdapter_SOAExtDomain.properties",'SOAExtDomain')
       createMQConnectionFactory("ResourceAdapter_SOAExtDomain.properties",'SOAExtDomain')
       disconnect()    

main()
