// Decompiled by Jad v1.5.8g. Copyright 2001 Pavel Kouznetsov.
// Jad home page: http://www.kpdus.com/jad.html
// Decompiler options: packimports(3) 
// Source File Name:   Challenge4.java

import java.applet.Applet;
import java.applet.AppletContext;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.net.URL;

public class Challenge4 extends Applet
    implements ActionListener
{

    public void stop()
    {
    }



    private String decrypt(String target, String phrase)
    {
        for(; target.length() > phrase.length(); phrase += phrase);
        String s1 = "";
        for(int i = 0; i < target.length(); i++)
            s1 = s1 + "" + (char)(target.charAt(i) - phrase.charAt(i) - i);

        return s1;
    }

    public Challenge4()
    {
        SubmitButton = null;
        PasswordField = null;
        SubmitButton = null;
        PasswordField = null;
        SubmitButton = new Button();
        PasswordField = new TextField("", 8);
    }

    public void destroy()
    {
    }

    public void actionPerformed(ActionEvent actionevent)
    {
        String pass = PasswordField.getText();
        String base = getDocumentBase().toString();
        char urlchars[] = {
            '\301', '\317', '\310', '\332', '\227', '\351', '\271', '\334'
        };
        String crypturl = new String(urlchars);
        char passchars[] = {
            '\u0114', '\u0135', '\u012D', '\u014F', '\u0100', '\u0162', '\u010A', '\u0148', '\u0142'
        };
        String cryptpass = new String(passchars);
        String newurl = "";
        String newpass = "";
        newpass = encrypt(pass, crypturl);
        crypturl = decrypt(crypturl, pass);
        base = base.substring(0, base.lastIndexOf('/') + 1);
        if(newpass.compareTo(cryptpass) == 0)
            newurl = base + crypturl;
        else
            newurl = base + "level104.php";
        try
        {
            getAppletContext().showDocument(new URL(newurl), "_self");
        }
        catch(Exception exception)
        {
            exception.printStackTrace();
        }
    }

    public void start()
    {
    }

    private String encrypt(String target, String phrase)
    {
        for(; target.length() > phrase.length(); phrase += phrase);
        String s1 = "";
        for(int i = 0; i < target.length(); i++)
            s1 = s1 + "" + (char)(target.charAt(i) + phrase.charAt(i) + i);

        return s1;
    }

    public void init()
    {
        SubmitButton.setLabel("submit");
        SubmitButton.addActionListener(this);
        PasswordField.setEchoChar('*');
        PasswordField.setForeground(new Color(192, 192, 192));
        add(PasswordField);
        add(SubmitButton);
        setBackground(new Color(0, 0, 0));
    }

    private Button SubmitButton;
    private TextField PasswordField;
}
