package jejbsample;
import java.util.Hashtable;
import javax.naming.Context;
import javax.naming.InitialContext;

public class ServiceClient {
    public ServiceClient() {
        super();
    }
    public static void main(String[] args) {

            {
                try

                {
                Hashtable<String, String> env = new Hashtable<String, String>();
                env.put(Context.INITIAL_CONTEXT_FACTORY,"weblogic.jndi.WLInitialContextFactory");
                env.put(Context.SECURITY_PRINCIPAL,"weblogic");
                env.put(Context.SECURITY_CREDENTIALS, "reuters123");
                env.put(Context.PROVIDER_URL,"t3://10.30.34.216:8000");
                InitialContext ctx = new InitialContext(env);

                System.out.println("Initial Context created");
                    Employee request=new Employee();
                    request.setEmpNo("48");

                EmployeeDetails empDetails  = (EmployeeDetails)ctx.lookup("EmployeeDetailsPS#jejbsample.EmployeeDetails");
                 // Employee response=  empDetails.getEmployeeDetails(request);

                System.out.println(empDetails.getEmployeeDetails(request).getEmpLoc());
                
                }

                catch (Exception e)
                {
                e.printStackTrace();
                }

        }
        }
}
