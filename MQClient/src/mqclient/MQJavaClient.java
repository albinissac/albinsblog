package mqclient;


import com.ibm.mq.jms.*;
import javax.jms.*;


public class MQJavaClient {
    
    public static void main(String[] args)
     {
      try {
       MQQueueConnectionFactory cf = new MQQueueConnectionFactory();
       cf.setHostName("10.30.34.78");
          
       cf.setPort(2022);      
       cf.setTransportType(JMSC.MQJMS_TP_CLIENT_MQ_TCPIP);     
       // cf.setTargetClientMatching(true);  
       cf.setQueueManager("TBNGEAI1");
       cf.setChannel("T_CRM_FUSION_CLIENT");
         
       MQQueueConnection connection = (MQQueueConnection) cf.createQueueConnection();
       MQQueueSession session = (MQQueueSession) connection.createQueueSession(false, Session.AUTO_ACKNOWLEDGE);
       MQQueue queue = (MQQueue) session.createQueue("queue:///DUMMY_Q?targetClient=1");
       
       MQQueueSender sender =  (MQQueueSender) session.createSender(queue);
       
       
      String message="<ns1:EmployeeRequest xmlns:ns1=\"http://xmlns.oracle.com/JEJBSample/EmployeeDetailService/EmployeeDetailService\">\n" + 
      "<ns1:empNo>987654</ns1:empNo>\n" + 
      "</ns1:EmployeeRequest>";
       
       TextMessage textMessage = (TextMessage) session.createTextMessage(message);    
       connection.start();
       sender.send(textMessage);
       
       
       sender.close();
       session.close();
       connection.close();
      
      }catch (Exception e) {
          e.printStackTrace();
       
      }
     }
}
