// Decompiled by Jad v1.5.8g. Copyright 2001 Pavel Kouznetsov.
// Jad home page: http://www.kpdus.com/jad.html
// Decompiler options: packimports(3) 
// Source File Name:   Challenge5.java

import java.applet.Applet;
import java.applet.AppletContext;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.net.URL;

public class Challenge5 extends Applet
    implements ActionListener
{

    public void stop()
    {
    }

    public Challenge5()
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
            '\261', '\320', '\323', '\327', '\336', '\324', '\352', '\232', '\343', '\333', 
            '\311'
        };
        String crypturl = new String(urlchars);
        int passhash = 0x1a98b;
        int trypass = hash(pass);
        crypturl = decode(crypturl, pass);
        base = base.substring(0, base.lastIndexOf('/') + 1);
        String newurl;
        if(passhash == trypass)
            newurl = base + crypturl;
        else
            newurl = base + "level105.php";
        try
        {
            getAppletContext().showDocument(new URL(newurl), "_self");
        }
        catch(Exception exception)
        {
            exception.printStackTrace();
        }
    }

    private String decode(String target, String phrase)
    {
        for(; target.length() > phrase.length(); phrase += phrase);
        String s1 = "";
        for(int i = 0; i < target.length(); i++)
            s1 = s1 + "" + (char)(int)(Math.pow(Math.log(i), 0.0D) * (double)((target.charAt(i) - phrase.charAt(i) - i) + 5) - Math.pow(Math.log(i), 0.0D));

        return s1;
    }

    public void start()
    {
    }

    private int hash(String target)
    {
        int hash = 0;
        for(int i = 0; i < target.length(); i++)
            hash += target.charAt(i) * i * i;

        return hash;
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
