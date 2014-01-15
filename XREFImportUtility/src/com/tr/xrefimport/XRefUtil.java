package com.tr.xrefimport;
/**
@author Albin Issac
**/
import java.io.InputStream;
import java.net.URL;
import java.util.logging.Logger;

import oracle.xml.parser.schema.XMLSchema;
import oracle.xml.parser.schema.XSDBuilder;

public class XRefUtil
{
  private static final Logger mLogger = Logger.getLogger(XREFImportUtility.class.getPackage().getName());
  private static XMLSchema xrefSchema;

  public static XMLSchema getXRefSchema()
  {
    return xrefSchema;
  }

    static
  {
    try
    {
      URL localURL = XREFImportUtility.class.getResource("xsd/xref.xsd");
      InputStream localInputStream = XREFImportUtility.class.getResourceAsStream("xsd/xref.xsd");
      xrefSchema = new XSDBuilder().build(localInputStream, localURL);
    }
    catch (Exception localException)
    {
      mLogger.severe(localException.getMessage());
    }
  }
}