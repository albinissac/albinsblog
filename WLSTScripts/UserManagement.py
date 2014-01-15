from java.io import FileInputStream
from java.util import *
from javax.management import *

domainName=raw_input('Please enter the weblogic domain name for the user creation: ')
print 'domainName:',domainName

propInputStream = FileInputStream("UserManagement_"+domainName+".properties")
configProps = Properties()
configProps.load(propInputStream)
adminURL=configProps.get("admin.url")
adminUserName=configProps.get("admin.userName")
adminPassword=configProps.get("admin.password")
realmName=configProps.get("security.realmName")

totalUsers_to_Create=configProps.get("total.username")

connect(adminUserName, adminPassword, adminURL)
serverConfig()
authenticatorPath= '/SecurityConfiguration/' + domainName + '/Realms/myrealm/AuthenticationProviders/DefaultAuthenticator'
print authenticatorPath
cd(authenticatorPath)
print 'Creating Users . . .'
x=1
while (x <= int(totalUsers_to_Create)):
        userName = configProps.get("create.user.name."+ str(x))
        userPassword = configProps.get("create.user.password."+ str(x))
        userDescription = configProps.get("create.user.description."+ str(x))
        try:
            cmo.createUser(userName , userPassword , userDescription)
            print '-----------User Created With Name : ' , userName
        except:
            print '*************** Check If the User With the Name : ' , userName ,' already Exists...'
        x = x + 1
        print ' '
        print ' '



print 'Adding Group Membership of the Users:'
y=1
while (y <= int(totalUsers_to_Create)):
        grpNames = configProps.get("create.user.groups."+ str(y)).split(",")
        userName = configProps.get("create.user.name."+ str(y))
        for grpName in grpNames:
            if grpName=='':
                 print ''
            else:
               cmo.addMemberToGroup(grpName,userName)
               print 'USER:' , userName , 'Added to GROUP: ' , grpName
        y=y+1

print 'Adding SOA Roles Membership of the Users:'
y=1
while (y <= int(totalUsers_to_Create)):
        roleNames = configProps.get("create.user.soarole."+ str(y)).split(",")
        userName = configProps.get("create.user.name."+ str(y))
        for roleName in roleNames:
            if roleName=='':
                 print ''
            else:
               grantAppRole(appStripe="soa-infra", appRoleName=roleName,principalClass="weblogic.security.principal.WLSUserImpl", principalName=userName)
               print 'USER:' , userName , 'Added the Role: ' , roleName
        y=y+1

