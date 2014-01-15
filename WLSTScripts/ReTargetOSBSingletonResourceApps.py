#=======================================================================================
#Script to re-point JMS System resource for purge Queues in OSB Clusture 
#usage: wlst.sh ReTargetOSBSingletonResourceApps.py <TOtargetOSB> wlsbJMSServer_auto_1 wlsbJMSServer_auto_2
#=======================================================================================
from java.io import FileInputStream

propInputStream1 = FileInputStream("domain.properties")
domainProps = util.Properties()
domainProps.load(propInputStream1) 
envType = wlsDomain=os.environ["EAI_ENV_TYPE"]

adminURL='t3://'+domainProps.get('domain1.AdminIP')+':'+domainProps.get('domain1.AdminPort')
adminUserName='weblogic'
adminPassword=domainProps.get("domain1.AdminPasswd")
connect(adminUserName, adminPassword, adminURL)



if len(sys.argv) != 4:
	print "Wrong Usage!! No.of Arguents passed:",len(sys.argv) ,"\n--------------\n usage: wlst.sh ReTagetJMSResourceforPurgeQueues <TOtargetOSB> <old jms sub-deployment> <new jms sub-deployment>\n--------------"
	sys.exit(-1)
if (sys.argv[1][:3] != 'OSB'):
	print "Wrong Arguement Values!!","Use Valid argument values:OSB1/OSB2/OSB3/OSB4"
	sys.exit(-1)

TOtargetOSB=sys.argv[1]
oldSubDeployment=sys.argv[2]
newSubDeployment=sys.argv[3]
edit()
startEdit()

print "Targeting Intiated...!! for ",TOtargetOSB

sentence = ['com.bea:Name=',TOtargetOSB,',Type=Server']

cd('/AppDeployments/ALSB Domain Singleton Marker Application')
set('Targets',jarray.array([], ObjectName))
set('Targets',jarray.array([ObjectName(''.join(sentence))], ObjectName))
print "...Targeted the Domain Singleton Marker Application to !!",TOtargetOSB

cd('/AppDeployments/ALSB Cluster Singleton Marker Application')
set('Targets',jarray.array([], ObjectName))
set('Targets',jarray.array([ObjectName(''.join(sentence))], ObjectName))
print "...Targeted the Cluster Singleton Marker Application to !!",TOtargetOSB

cd('/AppDeployments/Message Reporting Purger')
set('Targets',jarray.array([], ObjectName))
set('Targets',jarray.array([ObjectName(''.join(sentence))], ObjectName))
print "...Targeted the Message Reporting Purger to ",TOtargetOSB

# Change subdeployment targets
print "Locating JMS system resources for queues!!Intiated Repointing target ","to",TOtargetOSB
cd('/JMSSystemResources/configwiz-jms/JMSResource/configwiz-jms')
cmo.destroyQueue(getMBean('/JMSSystemResources/configwiz-jms/JMSResource/configwiz-jms/Queues/wli.reporting.purge.queue'))

cd('/SystemResources/configwiz-jms')
cmo.destroySubDeployment(getMBean('/SystemResources/configwiz-jms/SubDeployments/'+oldSubDeployment))


cd('/SystemResources/configwiz-jms')
set('Targets',jarray.array([], ObjectName))
set('Targets',jarray.array([ObjectName(''.join(sentence))], ObjectName))

cmo.createSubDeployment(newSubDeployment)

cd('/JMSSystemResources/configwiz-jms/JMSResource/configwiz-jms')
cmo.createQueue('wli.reporting.purge.queue')

cd('/JMSSystemResources/configwiz-jms/JMSResource/configwiz-jms/Queues/wli.reporting.purge.queue')
cmo.setJNDIName('wli.reporting.purge.queue')
cmo.setSubDeploymentName(newSubDeployment)

cd('/JMSSystemResources/configwiz-jms/JMSResource/configwiz-jms/Queues/wli.reporting.purge.queue/DeliveryFailureParams/wli.reporting.purge.queue')
cmo.setRedeliveryLimit(2)

cd('/SystemResources/configwiz-jms/SubDeployments/'+newSubDeployment)
set('Targets',jarray.array([ObjectName('com.bea:Name='+newSubDeployment+',Type=JMSServer')], ObjectName))

print "Re-targeted configwiz-jms on clusture to",TOtargetOSB

activate()