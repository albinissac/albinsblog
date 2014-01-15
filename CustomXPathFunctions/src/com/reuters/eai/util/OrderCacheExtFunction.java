 /**
  * Copyright 2005, Satyam Computers Limited  All Rights Reserved.
  *
  * FILE                 :       OrderCacheExtFunction.java
  * Description          :       Class used in Creating Custom XPath Function used in BPEL
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
   * 
   * Sprint - 9
   * 12 May 2008    Added two new fields(userNumber,userIDtype) to upsertOrderCache()function and in Database by Sreedevi.
   * 28 May 2008    Synchronized methods to improve thread safety
   * 
   * */

package com.reuters.eai.util;

import oracle.fabric.common.xml.xpath.IXPathContext;
import oracle.fabric.common.xml.xpath.XPathFunctionException;

import java.sql.SQLException;

import java.util.List;

import javax.naming.NamingException;

import org.w3c.dom.Element;
import org.w3c.dom.Node;
import org.w3c.dom.Text;


public class OrderCacheExtFunction {
    public OrderCacheExtFunction() {
    }

    public static class upsertOrderCache {
        public upsertOrderCache() {
        }

        /**
         * @param iXPathContext
         * @param list
         * @return
         * @throws XPathFunctionException
         * @throws NamingException
         * @throws SQLException
         */
        public synchronized Object call(IXPathContext iXPathContext, List list) throws XPathFunctionException, 
                                             NamingException, SQLException {
            try {
                if (list.size() != 19)
                throw new XPathFunctionException("Invalid Number of Arguments required 19 arguments");

                Object p1 = list.get(0);                        //DataSourceName
                Object p2 = list.get(1);                        //crm_ord_no
                Object p3 = list.get(2);                        //crm_oli_id
                Object p4 = list.get(3);                        //ord_line_action_code
                Object p5 = list.get(4);                        //root_item_id
                Object p6 = list.get(5);                        //asset_integration_id
                Object p7 = list.get(6);                        //action_code
                Object p8 = list.get(7);                        //permissioning_system
                Object p9 = list.get(8);                        //manual_perm_required
                Object p10 = list.get(9);                       //free_trail_flag
                Object p11 = list.get(10);                      //stb
                Object p12 = list.get(11);                      //country
                Object p13 = list.get(12);                      //fulfilment_status
                Object p14 = list.get(13);                      //fulfilment_integn_flag
                Object p15 = list.get(14);                      //business_case
                Object p16 = list.get(15);                      //billing_integration_flag
                Object p17 = list.get(16);                      //OrderLine Status
                Object p18 = list.get(17);                      //userNumber
                Object p19 = list.get(18);                      //userIDtype

                String sp1 = getParamValue(p1);                 //DataSourceName
                String sp2 = getParamValue(p2);                 //crm_ord_no
                String sp3 = getParamValue(p3);                 //crm_oli_id
                String sp4 = getParamValue(p4);                 //ord_line_action_code
                String sp5 = getParamValue(p5);                 //root_item_id
                String sp6 = getParamValue(p6);                 //asset_integration_id
                String sp7 = getParamValue(p7);                 //action_code
                String sp8 = getParamValue(p8);                 //permissioning_system
                String sp9 = getParamValue(p9);                 //manual_perm_required
                String sp10 = getParamValue(p10);               //free_trail_flag
                String sp11 = getParamValue(p11);               //stb
                String sp12 = getParamValue(p12);               //country
                String sp13 = getParamValue(p13);               //fulfilment_status
                String sp14 = getParamValue(p14);               //fulfilment_integn_flag
                String sp15 = getParamValue(p15);               //business_case
                String sp16 = getParamValue(p16);               //billing_integration_flag 
                String sp17 = getParamValue(p17);               //ManualPermComplete
                String sp18 = getParamValue(p18);               //userNumber
                String sp19 = getParamValue(p19);               //userIDtype

                return OrderCacheDBAccess.upsertOrderCache(sp1, sp2, sp3, sp4, sp5, sp6, sp7, sp8, 
                                        sp9, sp10, sp11, sp12, sp13, sp14, 
                                        sp15, sp16, sp17,sp18,sp19);

            } catch (XPathFunctionException e) {
                throw new XPathFunctionException("Failed to initialise DatatypeFactory", e);
            }
        }

        private  String getParamValue(Object param) {
            String value;
            if (param instanceof Element) {
                Node n = (Node)param;
                value = n.getFirstChild().getNodeValue();
            } else if (param instanceof Text) {
                Node n = (Node)param;
                value = n.getNodeValue();
            } else {
                value = String.valueOf(param);
            }
            return value;
        }    
    }



    public static class updateOrderCache {
    
            public updateOrderCache() {
            }

            public synchronized Object call(IXPathContext iXPathContext, 
                               List list) throws XPathFunctionException, 
                                                 NamingException, SQLException {
                try {

                    if (list.size() != 4)
                    throw new XPathFunctionException("Invalid Number of Arguments required 4 arguments");

                    
                    Object p1 = list.get(0);                //DataSourceName
                    Object p2 = list.get(1);                //crm_oli_id
                    Object p3 = list.get(2);                //Column Name to be Update
                    Object p4 = list.get(3);                //Column Value to be Update
                    
                    String sp1 = getParamValue(p1);        //DataSourceName
                    String sp2 = getParamValue(p2);        //crm_oli_id
                    String sp3 = getParamValue(p3);        //Column Name to be Update
                    String sp4 = getParamValue(p4);        //Column Value to be Update
                    
                    return OrderCacheDBAccess.updateOrderCache(sp1, sp2, sp3, sp4);

                } catch (XPathFunctionException e) {
                    throw new XPathFunctionException("Failed to initialise DatatypeFactory ", e);
                }
            }

            private String getParamValue(Object param) {
                String value;
                if (param instanceof Element) {
                    Node n = (Node)param;
                    value = n.getFirstChild().getNodeValue();
                } else if (param instanceof Text) {
                    Node n = (Node)param;
                    value = n.getNodeValue();
                } else {
                    value = String.valueOf(param);
                }
                return value;
            }
    }
}

