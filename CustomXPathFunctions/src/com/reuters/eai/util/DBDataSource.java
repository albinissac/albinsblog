/**
 * Copyright 2005, Satyam Computers Limited  All Rights Reserved.
 *
 * FILE			:	DBDataSource.java
 * Description          :	Creates a DataSource and Returns a Connectin Object From Database
 * company		:	Satyam Computers Limited
 * Author		: 	anvv sharma
 * Date			:	27-Nov-2007
 **/

package com.reuters.eai.util;

import java.sql.Connection;
import java.sql.SQLException;

import java.util.ResourceBundle;

import javax.naming.Context;
import javax.naming.InitialContext;

import javax.sql.DataSource;

public class DBDataSource {

	
	public static Connection getDataSource(String DSName) throws SQLException {
		DataSource ds           =   null;
		Connection conn         =   null;
		try{
                    Context ctx = new InitialContext();
                    System.out.println(ctx);
                    ds = (DataSource)ctx.lookup(DSName);
                    System.out.println(ds);
                    conn = ds.getConnection();
		}catch(javax.naming.NamingException e) {
			System.out.println("Naming Service = "+e.getMessage());
		}
		return conn;
		}
}
