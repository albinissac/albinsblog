 /**
  * Copyright 2005, Satyam Computers Limited  All Rights Reserved.
  *
  * FILE                 :       OrderCacheDBAccess.java
  * Description          :       Class used in Creating Core Logic for Custom XPath Function used in BPEL
  * company              :       Satyam Computers Limited
  * Author               :       anvv sharma
  * Date                 :       28-Nov-2007
  **/

  /* 
   * Change History 
   * 
   * Sprint - 5
   * 28 Nov 2007    Created OrderCacheDBAccess File for Custom XPath Function
   * 
   * Sprint - 6
   * 11 Jan 2008    Added New Columns rcrm_fulfilment_status, rcrm_fulfilment_integn_flag, rcrm_business_case, rcrm_billing_integration_flag
   * 
   * Sprint - 7
   * 20 Feb 2008    Modified the above column Names to fulfilment_status, fulfilment_integn_flag, business_case, billing_integration_flag
   * 19 Feb 2008    Added the Column manual_perm_required, Auto_Perm_Complete, OrderLineStatus in Database 
   *                Corresponding Changes in Custom Xpath Function
   * 21 Feb 2008    Added the New Function updateOrderCache() to Update a Column at Runtime.            
   * 08 Apr 2008    Changed the code not to update the permissioning status and billing status if the request has the oder line status as 'Permision Date Error'            
   * 22 Apr 2008    Changed the code to update Auto_Perm_Complete flag to N when permissioning system is CPFG as well
   * 
   * Sprint 9
   * 12 May 2008    Added the new Column userNumber,userIDtype in Database Corresponding Changes in Custom Xpath Function for PBI 653(Sreedevi).
   * 24 May 2008    Replaced strings with constants, removed unused imports and variables
   *                Corrected parameter order for upate statements for defect #14784
   *                Synchronized methods to avoid threading issues
   *06-Jul 2008    Added a condition for update to address defect 16124.Removed the finally blocks and added the all closes to the end of try.
   *                
   * */

 package

/*
   * Change History
   *
   * Sprint - 5
   * 28 Nov 2007    Created OrderCacheDBAccess File for Custom XPath Function
   *
   * Sprint - 6
   * 11 Jan 2008    Added New Columns rcrm_fulfilment_status, rcrm_fulfilment_integn_flag, rcrm_business_case, rcrm_billing_integration_flag
   *
   * Sprint - 7
   * 20 Feb 2008    Modified the above column Names to fulfilment_status, fulfilment_integn_flag, business_case, billing_integration_flag
   * 19 Feb 2008    Added the Column manual_perm_required, Auto_Perm_Complete, OrderLineStatus in Database
   *                Corresponding Changes in Custom Xpath Function
   * 21 Feb 2008    Added the New Function updateOrderCache() to Update a Column at Runtime.
   * 08 Apr 2008    Changed the code not to update the permissioning status and billing status if the request has the oder line status as 'Permision Date Error'
   * 22 Apr 2008    Changed the code to update Auto_Perm_Complete flag to N when permissioning system is CPFG as well
   *
   * Sprint 9
   * 12 May 2008    Added the new Column userNumber,userIDtype in Database Corresponding Changes in Custom Xpath Function for PBI 653(Sreedevi).
   * 24 May 2008    Replaced strings with constants, removed unused imports and variables
   *                Corrected parameter order for upate statements for defect #14784
   *                Added RuntimeExceptions rather than silently logging errors to System.out
   *                Synchronized methods to avoid threading issues
   * Sprint 11
   * 13 july 2008   Added code for Special Price Change
   * */

com.reuters.eai.util;

import com.reuters.eai.util.DBDataSource;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

import javax.naming.NamingException;


public class OrderCacheDBAccess {

    private static String ACTION_CODE_MANUAL_PERMISSIONED = 
        "Manual Permissioned";
    private static String ACTION_CODE_AKR_CHANGE = "AKR Change";
    private static String ACTION_CODE_START_DATE_CHANGE = "Start Date Change";
    private static String ACTION_CODE_STOP_DATE_CHANGE = "Stop Date Change";
    private static String ACTION_CODE_FT_EXTENSION = "FT Extension";
    private static String ACTION_CODE_BILLING_ACCOUNT_CHANGE = 
        "Billing Account Change";
   private static String FULFILMENT_STATUS_INPROGRESS = "In Progress"; 
   private static String ORDERLINE_STATUS_INPROGRESS  =  "In Progress";
   private static String ACTION_CODE_ABORT            = "Abort";
   private static String BUSINESS_CASE_ABORT          = "Abort";

    private static String FULFILMENT_STATUS_PERMISSION_DATE_ERROR = 
        "Permission Date Error";

    private static String YES = "Y";
    private static String NO = "N";

    private static String PERM_SYSTEM_SPM = "SPM";
    private static String PERM_SYSTEM_CPFG = "CPfG";
    
   private static String  BUSINESS_CASE_SP="Special Price Change";

    /**
     * @param DSName
     * @param crm_ord_no
     * @param crm_oli_id
     * @param ord_line_action_code
     * @param root_item_id
     * @param asset_integration_id
     * @param action_code
     * @param permissioning_system
     * @param manual_perm_required
     * @param free_trail_flag
     * @param stb
     * @param country
     * @param fulfilment_status
     * @param fulfilment_integn_flag
     * @param business_case
     * @param billing_integration_flag
     * @param orderline_Status
     * @param userNumber
     * @param userIDtype
     * @return
     * @throws NamingException
     * @throws SQLException
     */
    public static synchronized String upsertOrderCache(String DSName, 
                                                       String crm_ord_no, 
                                                       String crm_oli_id, 
                                                       String ord_line_action_code, 
                                                       String root_item_id, 
                                                       String asset_integration_id, 
                                                       String action_code, 
                                                       String permissioning_system, 
                                                       String manual_perm_required, 
                                                       String free_trail_flag, 
                                                       String stb, 
                                                       String country, 
                                                       String fulfilment_status, 
                                                       String fulfilment_integn_flag, 
                                                       String business_case, 
                                                       String billing_integration_flag, 
                                                       String orderline_Status, 
                                                       String userNumber, 
                                                       String userIDtype) {

        Connection connection = null;
        PreparedStatement pstmt = null;
        PreparedStatement pstmtUpdate = null;
        String Manual_Perm_Complete = "";
        String Auto_Perm_Complete = "";

        String pstmtInsert = 
            "INSERT INTO ORDER_CACHE (CRM_ORD_NO, CRM_OLI_ID, ORD_LINE_ACTION_CODE, ROOT_ITEM_ID, ASSET_INTEGRATION_ID, ACTION_CODE, PERMISSIONING_SYSTEM, MANUAL_PERM_REQUIRED, FREE_TRAIL_FLAG, STB, COUNTRY, FULFILMENT_STATUS, FULFILMENT_INTEGN_FLAG, BUSINESS_CASE, BILLING_INTEGRATION_FLAG, MANUAL_PERM_COMPLETE, AUTO_PERM_COMPLETE, ORDERLINE_STATUS, USERNUMBER, USERIDTYPE) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)";
        String pstmtUpdateExclAutoPermStatus = 
            "UPDATE ORDER_CACHE SET CRM_ORD_NO=?, ORD_LINE_ACTION_CODE=?, ROOT_ITEM_ID=?, ASSET_INTEGRATION_ID=?, ACTION_CODE=?, PERMISSIONING_SYSTEM=?, MANUAL_PERM_REQUIRED=?, FREE_TRAIL_FLAG=?, STB=?, COUNTRY=?, FULFILMENT_STATUS=?, FULFILMENT_INTEGN_FLAG=?, BUSINESS_CASE=?, BILLING_INTEGRATION_FLAG=?, MANUAL_PERM_COMPLETE=?, ORDERLINE_STATUS=?, USERNUMBER=?, USERIDTYPE=? WHERE CRM_OLI_ID=?";
        String pstmtUpdateExclStatus = 
            "UPDATE ORDER_CACHE SET CRM_ORD_NO=?, ORD_LINE_ACTION_CODE=?, ROOT_ITEM_ID=?, ASSET_INTEGRATION_ID=?, ACTION_CODE=?, PERMISSIONING_SYSTEM=?, MANUAL_PERM_REQUIRED=?, FREE_TRAIL_FLAG=?, STB=?, COUNTRY=?, FULFILMENT_STATUS=?, FULFILMENT_INTEGN_FLAG=?, BUSINESS_CASE=?, BILLING_INTEGRATION_FLAG=?, ORDERLINE_STATUS=?, USERNUMBER=?, USERIDTYPE=?  WHERE CRM_OLI_ID=?";
        String pstmtUpdateInclStatus = 
            "UPDATE ORDER_CACHE SET CRM_ORD_NO=?, ORD_LINE_ACTION_CODE=?, ROOT_ITEM_ID=?, ASSET_INTEGRATION_ID=?, ACTION_CODE=?, PERMISSIONING_SYSTEM=?, MANUAL_PERM_REQUIRED=?, FREE_TRAIL_FLAG=?, STB=?, COUNTRY=?, FULFILMENT_STATUS=?, FULFILMENT_INTEGN_FLAG=?, BUSINESS_CASE=?, BILLING_INTEGRATION_FLAG=?, ORDERLINE_STATUS=?, USERNUMBER=?, USERIDTYPE=? , AUTO_PERM_COMPLETE=?,MANUAL_PERM_COMPLETE=? WHERE CRM_OLI_ID=?";     
        String pstmtUpdateExclBothStatuses = 
            "UPDATE ORDER_CACHE SET CRM_ORD_NO=?, ORD_LINE_ACTION_CODE=?, ROOT_ITEM_ID=?, ASSET_INTEGRATION_ID=?, ACTION_CODE=?, PERMISSIONING_SYSTEM=?, MANUAL_PERM_REQUIRED=?, FREE_TRAIL_FLAG=?, STB=?, COUNTRY=?, FULFILMENT_INTEGN_FLAG=?, BUSINESS_CASE=?, BILLING_INTEGRATION_FLAG=?, USERNUMBER=?, USERIDTYPE=? WHERE CRM_OLI_ID=?";


        String insCrmOLID = "-1"; // Failure 
        boolean insStatus = false;
        int updateStatus = 0;
        try {

            connection = DBDataSource.getDataSource(DSName);
            if (manual_perm_required.equalsIgnoreCase(YES)) {
                                Manual_Perm_Complete = NO;
                            } else {
                                Manual_Perm_Complete = YES;
                            }

                            if ((permissioning_system.equalsIgnoreCase(PERM_SYSTEM_SPM) || 
                                 permissioning_system.equalsIgnoreCase(PERM_SYSTEM_CPFG)) && 
                                fulfilment_integn_flag.equalsIgnoreCase(YES)) {
                                Auto_Perm_Complete = NO;
                            } else {
                                Auto_Perm_Complete = YES;
                            }

                            if (ord_line_action_code.equalsIgnoreCase(ACTION_CODE_BILLING_ACCOUNT_CHANGE) || 
                                ord_line_action_code.equalsIgnoreCase(ACTION_CODE_AKR_CHANGE) || 
                                ord_line_action_code.equalsIgnoreCase(ACTION_CODE_START_DATE_CHANGE) || 
                                ord_line_action_code.equalsIgnoreCase(ACTION_CODE_STOP_DATE_CHANGE) || 
                                ord_line_action_code.equalsIgnoreCase(ACTION_CODE_FT_EXTENSION)) {
                                Manual_Perm_Complete = YES;
                                Auto_Perm_Complete = YES;
                            }
            if (ord_line_action_code.equalsIgnoreCase(BUSINESS_CASE_SP))
            {
                Manual_Perm_Complete = YES;
                Auto_Perm_Complete = YES;
            }
            if (action_code.equals(ACTION_CODE_MANUAL_PERMISSIONED)) {
                // Update order cache excluding auto perm complete status
                pstmtUpdate = 
                        connection.prepareStatement(pstmtUpdateExclAutoPermStatus);
                pstmtUpdate.setString(1, crm_ord_no);
                pstmtUpdate.setString(2, ord_line_action_code);
                pstmtUpdate.setString(3, root_item_id);
                pstmtUpdate.setString(4, asset_integration_id);
                pstmtUpdate.setString(5, action_code);
                pstmtUpdate.setString(6, permissioning_system);
                pstmtUpdate.setString(7, manual_perm_required);
                pstmtUpdate.setString(8, free_trail_flag);
                pstmtUpdate.setString(9, stb);
                pstmtUpdate.setString(10, country);
                pstmtUpdate.setString(11, fulfilment_status);
                pstmtUpdate.setString(12, fulfilment_integn_flag);
                pstmtUpdate.setString(13, business_case);
                pstmtUpdate.setString(14, billing_integration_flag);
                pstmtUpdate.setString(15, YES); // manual permissioning status
                pstmtUpdate.setString(16, orderline_Status);
                pstmtUpdate.setString(17, userNumber);
                pstmtUpdate.setString(18, userIDtype);
                pstmtUpdate.setString(19, crm_oli_id);

            } else if (fulfilment_status.equals(FULFILMENT_STATUS_PERMISSION_DATE_ERROR)) {
                pstmtUpdate = 
                        connection.prepareStatement(pstmtUpdateExclBothStatuses);
                pstmtUpdate.setString(1, crm_ord_no);
                pstmtUpdate.setString(2, ord_line_action_code);
                pstmtUpdate.setString(3, root_item_id);
                pstmtUpdate.setString(4, asset_integration_id);
                pstmtUpdate.setString(5, action_code);
                pstmtUpdate.setString(6, permissioning_system);
                pstmtUpdate.setString(7, manual_perm_required);
                pstmtUpdate.setString(8, free_trail_flag);
                pstmtUpdate.setString(9, stb);
                pstmtUpdate.setString(10, country);
                pstmtUpdate.setString(11, fulfilment_integn_flag);
                pstmtUpdate.setString(12, business_case);
                pstmtUpdate.setString(13, billing_integration_flag);
                pstmtUpdate.setString(14, userNumber);
                pstmtUpdate.setString(15, userIDtype);
                pstmtUpdate.setString(16, crm_oli_id);

            } else if((fulfilment_status.equals(FULFILMENT_STATUS_INPROGRESS) && orderline_Status.equals(ORDERLINE_STATUS_INPROGRESS))||(action_code.equals(ACTION_CODE_ABORT)&&business_case.equals(BUSINESS_CASE_ABORT))){
                // Update order cache including auto and man perm complete statuses
                pstmtUpdate = 
                        connection.prepareStatement(pstmtUpdateInclStatus);
                pstmtUpdate.setString(1, crm_ord_no);
                pstmtUpdate.setString(2, ord_line_action_code);
                pstmtUpdate.setString(3, root_item_id);
                pstmtUpdate.setString(4, asset_integration_id);
                pstmtUpdate.setString(5, action_code);
                pstmtUpdate.setString(6, permissioning_system);
                pstmtUpdate.setString(7, manual_perm_required);
                pstmtUpdate.setString(8, free_trail_flag);
                pstmtUpdate.setString(9, stb);
                pstmtUpdate.setString(10, country);
                pstmtUpdate.setString(11, fulfilment_status);
                pstmtUpdate.setString(12, fulfilment_integn_flag);
                pstmtUpdate.setString(13, business_case);
                pstmtUpdate.setString(14, billing_integration_flag);
                pstmtUpdate.setString(15, orderline_Status);
                pstmtUpdate.setString(16, userNumber);
                pstmtUpdate.setString(17, userIDtype);
                pstmtUpdate.setString(18, Auto_Perm_Complete);
                pstmtUpdate.setString(19,Manual_Perm_Complete);
                pstmtUpdate.setString(20,crm_oli_id);
            }
            else{
                            // Update order cache excluding auto and man perm complete statuses
                            pstmtUpdate = 
                                    connection.prepareStatement(pstmtUpdateExclStatus);
                            pstmtUpdate.setString(1, crm_ord_no);
                            pstmtUpdate.setString(2, ord_line_action_code);
                            pstmtUpdate.setString(3, root_item_id);
                            pstmtUpdate.setString(4, asset_integration_id);
                            pstmtUpdate.setString(5, action_code);
                            pstmtUpdate.setString(6, permissioning_system);
                            pstmtUpdate.setString(7, manual_perm_required);
                            pstmtUpdate.setString(8, free_trail_flag);
                            pstmtUpdate.setString(9, stb);
                            pstmtUpdate.setString(10, country);
                            pstmtUpdate.setString(11, fulfilment_status);
                            pstmtUpdate.setString(12, fulfilment_integn_flag);
                            pstmtUpdate.setString(13, business_case);
                            pstmtUpdate.setString(14, billing_integration_flag);
                            pstmtUpdate.setString(15, orderline_Status);
                            pstmtUpdate.setString(16, userNumber);
                            pstmtUpdate.setString(17, userIDtype);
                            pstmtUpdate.setString(18, crm_oli_id);

                        }

            updateStatus = pstmtUpdate.executeUpdate();
            insCrmOLID = crm_oli_id;

            /* Potential thread safety issue */

            if (updateStatus == 0) {
                // for Insert
              /* if (manual_perm_required.equalsIgnoreCase(YES)) {
                    Manual_Perm_Complete = NO;
                } else {
                    Manual_Perm_Complete = YES;
                }

                if ((permissioning_system.equalsIgnoreCase(PERM_SYSTEM_SPM) || 
                     permissioning_system.equalsIgnoreCase(PERM_SYSTEM_CPFG)) && 
                    fulfilment_integn_flag.equalsIgnoreCase(YES)) {
                    Auto_Perm_Complete = NO;
                } else {
                    Auto_Perm_Complete = YES;
                }

                if (ord_line_action_code.equalsIgnoreCase(ACTION_CODE_BILLING_ACCOUNT_CHANGE) || 
                    ord_line_action_code.equalsIgnoreCase(ACTION_CODE_AKR_CHANGE) || 
                    ord_line_action_code.equalsIgnoreCase(ACTION_CODE_START_DATE_CHANGE) || 
                    ord_line_action_code.equalsIgnoreCase(ACTION_CODE_STOP_DATE_CHANGE) || 
                    ord_line_action_code.equalsIgnoreCase(ACTION_CODE_FT_EXTENSION)) {
                    Manual_Perm_Complete = YES;
                    Auto_Perm_Complete = YES;
                }*/

                pstmt = connection.prepareStatement(pstmtInsert);
                pstmt.setString(1, crm_ord_no);
                pstmt.setString(2, crm_oli_id);
                pstmt.setString(3, ord_line_action_code);
                pstmt.setString(4, root_item_id);
                pstmt.setString(5, asset_integration_id);
                pstmt.setString(6, action_code);
                pstmt.setString(7, permissioning_system);
                pstmt.setString(8, manual_perm_required);
                pstmt.setString(9, free_trail_flag);
                pstmt.setString(10, stb);
                pstmt.setString(11, country);
                pstmt.setString(12, fulfilment_status);
                pstmt.setString(13, fulfilment_integn_flag);
                pstmt.setString(14, business_case);
                pstmt.setString(15, billing_integration_flag);
                pstmt.setString(16, Manual_Perm_Complete);
                pstmt.setString(17, Auto_Perm_Complete);
                pstmt.setString(18, orderline_Status);
                pstmt.setString(19, userNumber);
                pstmt.setString(20, userIDtype);

                insStatus = pstmt.execute();
                insCrmOLID = crm_oli_id;
            }

        }

        catch (Exception e) {
            return "Exception - " + e;
        } finally {
            if (connection != null) {
                try {
                    connection.close();
                } catch (Exception e) {
                    // Nothing we can do
                }
            }
            if (pstmt != null) {
                try {
                    pstmt.close();
                } catch (Exception e) {
                    // Nothing we can do
                }
            }
            if (pstmtUpdate != null) {
                try {
                    pstmtUpdate.close();
                } catch (Exception e) {
                    // Nothing we can do
                }
            }
        }

        return insCrmOLID;
    }

    /* Update Order Cache */

    /**
     * @param DSName
     * @param crm_oli_id
     * @param InsertcolumnName
     * @param InsertcomumnValue
     * @return
     * @throws NamingException
     * @throws SQLException
     */
    public static synchronized String updateOrderCache(String DSName, 
                                                          String crm_oli_id, 
                                                          String InsertcolumnName, 
                                                          String InsertcomumnValue) {

        Connection connection = null;
        PreparedStatement pstmtUpdate = null;
        String pstmtUpdateQuery = 
            "UPDATE ORDER_CACHE SET " + InsertcolumnName + 
            "=? WHERE CRM_OLI_ID=?";
        System.out.println(pstmtUpdateQuery);
        String insCrmOLID = "-1"; // Failure 
        boolean insStatus = false;
        try {
            connection = DBDataSource.getDataSource(DSName);
            pstmtUpdate = connection.prepareStatement(pstmtUpdateQuery);
            pstmtUpdate.setString(1, InsertcomumnValue);
            pstmtUpdate.setString(2, crm_oli_id);
            pstmtUpdate.executeUpdate();
            insCrmOLID = crm_oli_id;
        } catch (Exception e) {
            return "Exception - " + e;

        } finally {
            if (connection != null) {
                try {
                    connection.close();
                } catch (Exception e) {
                    // Nothing we can do
                }
            }
            if (pstmtUpdate != null) {
                try {
                    pstmtUpdate.close();
                } catch (Exception e) {
                    // Nothing we can do
                }
            }
        }

        return insCrmOLID;
    }

}


