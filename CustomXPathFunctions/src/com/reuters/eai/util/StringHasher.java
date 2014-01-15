package com.reuters.eai.util;

import java.io.UnsupportedEncodingException;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

import java.util.List;
import java.util.logging.Level;
import java.util.logging.Logger;

import oracle.fabric.common.xml.xpath.IXPathContext;
import oracle.fabric.common.xml.xpath.IXPathFunction;
import oracle.fabric.common.xml.xpath.XPathFunctionException;

import org.w3c.dom.Node;

public class StringHasher implements IXPathFunction {

    private static String HASH_ALGORITHM = "MD5";
    private static String STRING_ENCODING = "UTF-8";

    /**
     * Returns the MD5 hash of a string in hexadecimal format
     * @param input The string to hash
     * @return the 16-byte MD5 hash in hex
     */
    public static synchronized String hashString(String input) {
        MessageDigest md;
        byte[] md5hash = new byte[32];

        try {
            md = MessageDigest.getInstance(HASH_ALGORITHM);
            md5hash = md.digest(input.getBytes());
            md.update(input.getBytes(STRING_ENCODING), 0, input.length());
            md5hash = md.digest();
        } catch (NoSuchAlgorithmException e) {
            throw new RuntimeException(e);
        } catch (UnsupportedEncodingException e) {
            throw new RuntimeException(e);
        }

        return StringHasher.byteArrayToHexString(md5hash);

    }

    /**
     * Convert a byte[] array to readable string format.
     * @return result String buffer in String format 
     * @param in byte[] buffer to convert to string format
     */
    private static String byteArrayToHexString(byte[] in) {

        byte ch = 0x00;
        int i = 0;
        if (in == null || in.length <= 0)
            return null;

        String pseudo[] = 
        { "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", 
          "E", "F" };
          
        // Each byte in hex will need 2 characters
        StringBuffer out = new StringBuffer(in.length * 2);

        while (i < in.length) {
            ch = (byte)(in[i] & 0xF0); // Take high nibble
            ch = (byte) (ch >>> 4); // shift the bits down
            ch = (byte)(ch & 0x0F); // strip off high-order bit
            out.append(pseudo[(int)ch]); // convert the nibble to a String Character
            ch = (byte)(in[i] & 0x0F); // Take low nibble 
            out.append(pseudo[(int)ch]); // convert the nibble to a String Character
            i++;
        }

        return new String(out);
    }

    public synchronized Object call(IXPathContext ixPathContext, List args) {
        if (args.size() == 1) {
            if (args.get(0) instanceof String) {
                return hashString((String)args.get(0));
            } else if (args.get(0) instanceof Node) {
                Node n = (Node)args.get(0);
                return hashString(n.getNodeValue());
            }
        }
        throw new RuntimeException("hash() requires one string argument.");
    }
}
