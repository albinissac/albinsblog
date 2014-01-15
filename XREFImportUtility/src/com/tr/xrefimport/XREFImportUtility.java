package com.tr.xrefimport;

/**
@author Albin Issac
**/
import java.io.File;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

import java.util.HashMap;
import java.util.Locale;

import oracle.ldap.util.Guid;

import oracle.tip.xref.util.XMLUtil;

import oracle.xml.parser.v2.DOMParser;
import oracle.xml.parser.v2.XMLDocument;
import oracle.xml.parser.v2.XMLElement;

import org.w3c.dom.NodeList;


public class XREFImportUtility {

    private static Locale locale = Locale.getDefault();

    private static String TABLE = "table";
    private static String COLUMNS = "columns";
    private static String COLUMN = "column";
    private static String ROWS = "rows";
    private static String ROW = "row";
    private static String CELL = "cell";
    private static String NAME_ATTR = "name";
    private static String COLNAME_ATTR = "colName";
    private final String dbUrl = System.getProperty("DB_URL");
    private final String dbUser = System.getProperty("DB_USER");
    private final String dbPassword = System.getProperty("DB_PASSWORD");    
    private static String mode = "ignore";

    public XREFImportUtility() throws Exception {

    }

    public void importXref(String paramString1,
                           String paramString2) throws Exception {
            File localFile = new File(paramString1);
            if (!localFile.exists())
                throw new Exception();
            DOMParser localDOMParser = new DOMParser();
            localDOMParser.setValidationMode(3);
            localDOMParser.setXMLSchema(XRefUtil.getXRefSchema());
            localDOMParser.parse(localFile.toURL());
            XMLDocument localXMLDocument = localDOMParser.getDocument();
            XMLElement localXMLElement =
                (XMLElement)XMLUtil.getXRefElement(localXMLDocument);
            if (localXMLElement == null)
                throw new RuntimeException();
            importXrefData(localXMLElement);        
    }

    private void importXrefData(XMLElement paramXMLElement) throws Exception {

        XMLElement localXMLElement1 =
            (XMLElement)XMLUtil.getChildElement(paramXMLElement, TABLE);
        String str = XMLUtil.getAttributeValue(localXMLElement1, NAME_ATTR);
        HashMap localHashMap = new HashMap();
        populateColumnGuids(localXMLElement1, localHashMap);
        XMLElement localXMLElement2 =
            (XMLElement)XMLUtil.getChildElement(localXMLElement1, ROWS);
        if (localXMLElement2 != null) {
            Connection localConnection = getConnection();
            localConnection.setAutoCommit(false);
            NodeList localNodeList = null;
            localNodeList = XMLUtil.getChildElements(localXMLElement2, ROW);
            int i = localNodeList.getLength();
            PreparedStatement localPreparedStatement1 =
                prepareStatement(localConnection,
                                 "INSERT INTO XREF_DATA(XREF_TABLE_NAME,XREF_COLUMN_NAME,ROW_NUMBER,VALUE,IS_DELETED,LAST_MODIFIED) VALUES(?,?,?,?,'N',?)");

            PreparedStatement localPreparedStatement2 =
                prepareStatement(localConnection,
                                 "UPDATE XREF_DATA SET IS_DELETED='Y' WHERE ROW_NUMBER=?");
            for (int j = 0; j < i; j++) {
                XMLElement localXMLElement3 =
                    (XMLElement)localNodeList.item(j);
				addXrefRow(localXMLElement3, localHashMap, str,
                           localConnection, localPreparedStatement1,
                           localPreparedStatement2);
            }
            try {
                localConnection.commit();
                localPreparedStatement1.close();
                localPreparedStatement2.close();
                localConnection.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }

    }

    private void populateColumnGuids(XMLElement paramXMLElement,
                                     HashMap paramHashMap) throws Exception {

        String str = XMLUtil.getAttributeValue(paramXMLElement, NAME_ATTR);
        XMLElement localXMLElement =
            (XMLElement)XMLUtil.getChildElement(paramXMLElement, COLUMNS);
        if (localXMLElement == null) {
            throw new Exception();
        }
        NodeList localNodeList =
            XMLUtil.getChildElements(localXMLElement, COLUMN);
        int i = localNodeList.getLength();
        StringBuffer localStringBuffer = new StringBuffer();
        Object localObject1;
        Object localObject2;
        for (int j = 0; j < i; j++) {
            localObject1 = (XMLElement)localNodeList.item(j);
            localObject2 =
                    XMLUtil.getAttributeValue((XMLElement)localObject1, NAME_ATTR);
            paramHashMap.put(localObject2, localObject2);
        }

    }

    private void addXrefRow(XMLElement paramXMLElement, HashMap paramHashMap,
                            String paramString, Connection paramConnection,
                            PreparedStatement paramPreparedStatement1,
                            PreparedStatement paramPreparedStatement2) throws Exception {
        String str1 = Guid.newInstance().toString();
        ;
        NodeList localNodeList =
            XMLUtil.getChildElements(paramXMLElement, CELL);
        int i = localNodeList.getLength();
        Object localObject1;
        Object localObject2;
        for (int j = 0; j < i; j++) {
            localObject1 = (XMLElement)localNodeList.item(j);
            String str3 =
                XMLUtil.getAttributeValue((XMLElement)localObject1, COLNAME_ATTR);
              localObject2 = (String)paramHashMap.get(str3);
            String str4 = XMLUtil.getText((XMLElement)localObject1);
            String str5 = null;
            if ((str4 == null) || (str4.length() <= 0))
                continue;
            str5 =getExistingRowNum(paramString, (String)localObject2, str4, paramConnection);
            if (str5 != null) {
                if (mode.equals("overwrite")) {
                    delExistingRow(str5, paramPreparedStatement2);
                    insertXrefValue(paramString, (String)localObject2, str1,
                                    str4, paramPreparedStatement1);
                } else {
                    paramConnection.rollback();
                    return;
                }
            } else {
                insertXrefValue(paramString, (String)localObject2, str1, str4,
                                paramPreparedStatement1);
            }
        }

        paramConnection.commit();
    }

    private void insertXrefValue(String paramString1, String paramString2,
                                 String paramString3, String paramString4,
                                 PreparedStatement paramPreparedStatement) throws Exception {
        java.util.Date date = new java.util.Date(System.currentTimeMillis());
        java.sql.Timestamp timestamp = new java.sql.Timestamp(date.getTime());

        paramPreparedStatement.setString(1, paramString1);
        paramPreparedStatement.setString(2, paramString2);
        paramPreparedStatement.setString(3, paramString3);
        paramPreparedStatement.setString(4, paramString4);
        paramPreparedStatement.setTimestamp(5, timestamp);
        paramPreparedStatement.execute();

    }

    private void delExistingRow(String paramString,
                                PreparedStatement paramPreparedStatement) throws Exception {
        String[] arrayOfString = { paramString };
        execute(paramPreparedStatement, arrayOfString);
    }

    private String getExistingRowNum(String paramString1, String paramString2,
                                     String paramString3,
                                     Connection paramConnection) throws Exception {
        String str = null;
        PreparedStatement localPreparedStatement = null;
        try {
            localPreparedStatement =
                    prepareStatement(paramConnection, "SELECT ROW_NUMBER FROM XREF_DATA WHERE VALUE = ? AND XREF_TABLE_NAME=? AND XREF_COLUMN_NAME=? AND IS_DELETED='N'");
            String[] arrayOfString =
            { paramString3, paramString1,
              paramString2 };
            ResultSet localResultSet =
                executeQuery(localPreparedStatement, arrayOfString);
            while (localResultSet.next())
                str = localResultSet.getString(1);
        } finally {
            if (localPreparedStatement != null)
                try {
                    localPreparedStatement.close();
                } catch (SQLException localSQLException2) {
                }
        }
        return str;
    }

    protected Connection getConnection() throws Exception {
        Connection localConnection = null;
        Class.forName("oracle.jdbc.driver.OracleDriver");
        String url = dbUrl;
        localConnection =
                DriverManager.getConnection(url, dbUser, dbPassword);
        return localConnection;
    }


    public static ResultSet executeQuery(PreparedStatement paramPreparedStatement,
                                         String[] paramArrayOfString) throws SQLException {
        ResultSet localResultSet = null;
        if (paramArrayOfString != null)
            for (int i = 0; i < paramArrayOfString.length; i++)
                paramPreparedStatement.setString(i + 1, paramArrayOfString[i]);
        localResultSet = paramPreparedStatement.executeQuery();
        return localResultSet;
    }


    public static boolean execute(PreparedStatement paramPreparedStatement,
                                  String[] paramArrayOfString) throws SQLException {
        boolean bool = false;
        if (paramArrayOfString != null)
            for (int i = 0; i < paramArrayOfString.length; i++)
                paramPreparedStatement.setString(i + 1, paramArrayOfString[i]);
        bool = paramPreparedStatement.execute();
        return bool;
    }

    public static final PreparedStatement prepareStatement(Connection paramConnection,
                                                           String paramString) throws SQLException {
        return paramConnection.prepareStatement(paramString);
    }


    public static void main(String[] paramArrayOfString) {
        Object localObject1 = null;
        Object localObject2;
        localObject1 =paramArrayOfString[0];
        try {
            localObject2 = new XREFImportUtility();
            ((XREFImportUtility)localObject2).importXref((String)localObject1,
                                                         null);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

}
