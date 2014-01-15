from java.io import FileInputStream
    
TargetServerName='AdminServer'    
soaHome=os.environ["SOAHOME"]    
appPathSock=soaHome+'/soa/connectors/SocketAdapter.rar'
appNameSock='SocketAdapter'
moduleOverrideNameSock=appNameSock+'.rar'    
moduleDescriptorName='META-INF/weblogic-ra.xml'

def createSocketConnectionFactory(propFile):

    edit()
    startEdit()
    propInputStream = FileInputStream(propFile)
    configProps = Properties()
    configProps.load(propInputStream)  
        

    socketHost=configProps.get("domain1.socket.connectionpool.host")
    socketPort=configProps.get("domain1.socket.connectionpool.port")
    socketKeepAlive=configProps.get("domain1.socket.connectionpool.keepalive")
    socketTimeOut=configProps.get("domain1.socket.connectionpool.timeout")
    socketJNDIName=configProps.get("domain1.socket.datasource.jndi.name")
    planPathSocket=configProps.get('global.resource.deployment.plan.path')+'/'+domainName+'_PlanSocket.xml'

    print socketJNDIName
    startApplication(appNameSock)
    myPlanSock=loadApplication(appPathSock, planPathSocket)
    makeDeploymentPlanVariable(myPlanSock,'ConnectionInstance_eis/Socket_JNDIName_1310297935734342223209', socketJNDIName , '/weblogic-connector/outbound-resource-adapter/connection-definition-group/[connection-factory-interface="javax.resource.cci.ConnectionFactory"]/connection-instance/[jndi-name="'+socketJNDIName+'"]/jndi-name',moduleOverrideNameSock)
    makeDeploymentPlanVariable(myPlanSock, 'ConfigProperty_eis/Socket_JNDIName_Host_Name_1310292729357210', socketHost,'/weblogic-connector/outbound-resource-adapter/connection-definition-group/[connection-factory-interface="javax.resource.cci.ConnectionFactory"]/connection-instance/[jndi-name="'+socketJNDIName+'"]/connection-properties/properties/property/[name="Host"]/value',moduleOverrideNameSock)
    makeDeploymentPlanVariable(myPlanSock, 'ConfigProperty_eis/Socket_JNDIName_KeepAlive_1310297329357211', socketKeepAlive,'/weblogic-connector/outbound-resource-adapter/connection-definition-group/[connection-factory-interface="javax.resource.cci.ConnectionFactory"]/connection-instance/[jndi-name="'+socketJNDIName+'"]/connection-properties/properties/property/[name="KeepAlive"]/value',moduleOverrideNameSock)
    makeDeploymentPlanVariable(myPlanSock, 'ConfigProperty_eis/Socket_JNDIName_Port_1310297935742212', socketPort,'/weblogic-connector/outbound-resource-adapter/connection-definition-group/[connection-factory-interface="javax.resource.cci.ConnectionFactory"]/connection-instance/[jndi-name="'+socketJNDIName+'"]/connection-properties/properties/property/[name="Port"]/value',moduleOverrideNameSock)
    makeDeploymentPlanVariable(myPlanSock, 'ConfigProperty_eis/Socket_JNDIName_Timeout_1310297393257213', socketTimeOut,'/weblogic-connector/outbound-resource-adapter/connection-definition-group/[connection-factory-interface="javax.resource.cci.ConnectionFactory"]/connection-instance/[jndi-name="'+socketJNDIName+'"]/connection-properties/properties/property/[name="Timeout"]/value',moduleOverrideNameSock)
            
    myPlanSock.save();
    save();
    cd('/AppDeployments/SocketAdapter/Targets');
    updateApplication(appNameSock, planPathSocket);
    activate(block='true');
       
    
def makeDeploymentPlanVariable(wlstPlan, name, value, xpath,overrideName, origin='planbased'):
    wlstPlan.destroyVariable(name)
    wlstPlan.destroyVariableAssignment(name, overrideName, moduleDescriptorName)
    variableAssignment = wlstPlan.createVariableAssignment(name, overrideName, moduleDescriptorName)
    print 'XPATH=',xpath
    variableAssignment.setXpath(xpath)
    variableAssignment.setOrigin(origin)
    wlstPlan.createVariable(name, value)
    print 'moduleDescriptorName=',moduleDescriptorName


def main():
    
       propInputStream1 = FileInputStream("domain.properties")
       domainProps = util.Properties()
       domainProps.load(propInputStream1)
       
       #SOA Server Details
       adminURL='t3://'+domainProps.get('domain1.AdminIP')+':'+domainProps.get('domain1.AdminPort')
       adminUserName='weblogic'
       adminPassword=domainProps.get("domain1.AdminPasswd")
       connect(adminUserName, adminPassword, adminURL)
       createSocketConnectionFactory("ResourceAdapter_SOACoreDomain.properties");
       disconnect()
       print 'Successfully created socket connection factory under SOACoreDomain'
main()