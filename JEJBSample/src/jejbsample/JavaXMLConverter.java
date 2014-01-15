package javaxmlconverter;

import java.io.InputStream;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;

import jejbsample.Employee;

import org.apache.xmlbeans.XmlException;

import org.apache.xmlbeans.XmlObject;

import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;


public class JavaXMLConverter {
    public JavaXMLConverter() {
        super();
    }

    public static String getEmpRequestXML(Employee emp) {
       
        return emp.getEmpNo();

    }

    public static Employee getEmpResponseJava(XmlObject xml) throws Exception{
        Employee emp = new Employee();
        
            DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
            InputStream inputStream = xml.newInputStream();
            DocumentBuilder db = dbf.newDocumentBuilder();
            Document doc = db.parse(inputStream);           
            String empName=null ;
            String empNo=null;
            String empDept=null;
            String empLoc=null;            
            
            NodeList nList = doc.getElementsByTagName("EmployeeResponse");
            for (int temp = 0; temp < nList.getLength(); temp++) {
                Node nNode = nList.item(temp);
                if (nNode.getNodeType() == Node.ELEMENT_NODE) {
                    Element eElement = (Element)nNode;
                     empName =eElement.getElementsByTagName("empName").item(0).getTextContent();
                     empNo =eElement.getElementsByTagName("empNo").item(0).getTextContent();
                     empDept =eElement.getElementsByTagName("empDept").item(0).getTextContent();
                     empLoc =eElement.getElementsByTagName("empLoc").item(0).getTextContent();
                   
                }
            }
        emp.setEmpDept(empDept);
        emp.setEmpName(empName);
        emp.setEmpLoc(empLoc);
        emp.setEmpNo(empNo);
        
        return emp;

        }
    }

