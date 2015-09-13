// Decompiled by Jad v1.5.8g. Copyright 2001 Pavel Kouznetsov.
// Jad home page: http://www.kpdus.com/jad.html
// Decompiler options: packimports(3) 
// Source File Name:   Challenge2.java

import java.applet.Applet;
import java.applet.AppletContext;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.net.URL;

public class Challenge2 extends Applet
    implements ActionListener
{

    public void stop()
    {
    }

    public Challenge2()
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
        String s = PasswordField.getText();
        String s1 = "";
        String s2 = getDocumentBase().toString();
        String s3 = decrypt("ejeju/qiq");
        s = encrypt(s);
        s2 = s2.substring(0, s2.lastIndexOf('/') + 1);
        if(s.compareTo("SjhiuQbttxpse") == 0)
            s1 = s2 + s3;
        else
            s1 = s2 + "level102.php";
        try
        {
            getAppletContext().showDocument(new URL(s1), "_self");
        }
        catch(Exception exception)
        {
            exception.printStackTrace();
        }
    }

    public void start()
    {
    }

    private String encrypt(String s)
    {
        String s1 = "";
        for(int i = 0; i < s.length(); i++)
            s1 = s1 + "" + (char)(s.charAt(i) + 1);

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

    private String decrypt(String s)
    {
        String s1 = "";
        for(int i = 0; i < s.length(); i++)
            s1 = s1 + "" + (char)(s.charAt(i) - 1);

        return s1;
    }

    private Button SubmitButton;
    private TextField PasswordField;
}
