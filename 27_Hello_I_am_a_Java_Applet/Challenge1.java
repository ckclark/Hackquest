// Decompiled by Jad v1.5.8g. Copyright 2001 Pavel Kouznetsov.
// Jad home page: http://www.kpdus.com/jad.html
// Decompiler options: packimports(3) 
// Source File Name:   Challenge1.java

import java.applet.Applet;
import java.applet.AppletContext;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.net.URL;

public class Challenge1 extends Applet
    implements ActionListener
{

    public void stop()
    {
    }

    public Challenge1()
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
        s2 = s2.substring(0, s2.lastIndexOf('/') + 1);
        if(s.compareTo("GoodPassword") == 0)
            s1 = s2 + "lingo.php";
        else
            s1 = s2 + "level101.php";
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
