package com.reuters.eai.util;

/**
 * Copyright 2010,   All Rights Reserved.
 *
 * FILE			:	StringFormatter.java
 * Description          :	Creates a DataSource and Returns a Connectin Object From Database
 * company		:	Thomson Reuters
 * Author		: 	Rijoy Purayil
 * Date			:	21-June-2010
 **/


public class StringFormatter {
    private static String REGEX = "[!\"#$%:;<>{|}~€ƒ„…†‡ˆ‰Š‹ŒŽ“”•—˜™š›œžŸ ¤¦¨©«¬­®¯°²³´¶·¸¹º»¼½¾ÆÞßæþ \n]+";
    private static String FIRSTNLASTNAMEREGEX ="[&]+";  
    private static String REPLACE = "";



    /**
     * @param strToFormat : String to be formatted
     * @param attrName : Name of the attribute 
     * @return formattedStr : Formatted String with Removed Charaters in REGEX String
     */
    public static String removeSpecialCharacters(String strToFormat,String attrName) {

        try {
            String formattedStr = strToFormat.replaceAll(REGEX, REPLACE);
            formattedStr = formattedStr.replaceAll("\\u0081", REPLACE);
         // formattedStr = formattedStr.replaceAll("\\u0082", REPLACE);
            formattedStr = formattedStr.replaceAll("\\u008D", REPLACE);
            formattedStr = formattedStr.replaceAll("\\u008F", REPLACE);
            formattedStr = formattedStr.replaceAll("\\u0090", REPLACE);
            formattedStr = formattedStr.replaceAll("\\u009D", REPLACE);
            
            if(attrName.equalsIgnoreCase("firstName") || attrName.equalsIgnoreCase("lastName")){
                formattedStr = formattedStr.replaceAll(FIRSTNLASTNAMEREGEX, REPLACE);
            }
            return(formattedStr);
        }
        catch (Exception e) {
            return "Exception Formatting - " + e;
        }

    }
}
