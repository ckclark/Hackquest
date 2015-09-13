// Decompiled by Jad v1.5.8g. Copyright 2001 Pavel Kouznetsov.
// Jad home page: http://www.kpdus.com/jad.html
// Decompiler options: packimports(3) 
// Source File Name:   Challenge6.java

import java.applet.Applet;
import java.applet.AppletContext;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.URL;
import java.util.StringTokenizer;

public class Challenge6 extends Applet
    implements ActionListener
{

    public void stop()
    {
    }

    public Challenge6()
    {
        maxurls = 0;
        SubmitButton = null;
        PasswordField = null;
        m_t = null;
        password = null;
        url = null;
        maxurls = 10;
        SubmitButton = null;
        PasswordField = null;
        m_t = null;
        password = new String[maxurls];
        url = new String[maxurls];
        m_t = "_self";
        SubmitButton = null;
        PasswordField = null;
        SubmitButton = new Button();
        PasswordField = new TextField("", 8);
    }

    public void destroy()
    {
    }

    public void readFile(String s)
    {
        BufferedReader bufferedreader = null;
        String s1 = getDocumentBase().toString();
        s1 = s1.substring(0, s1.lastIndexOf('/') + 1);
        try
        {
            bufferedreader = new BufferedReader(new InputStreamReader((new URL(s1 + s)).openStream()));
        }
        catch(Exception _ex)
        {
            bufferedreader = null;
        }
        int i = 0;
        do
        {
            String s2;
            try
            {
                s2 = bufferedreader.readLine();
            }
            catch(Exception _ex)
            {
                return;
            }
            if(s2 == null)
                break;
            StringTokenizer stringtokenizer = new StringTokenizer(s2, "|", false);
            if(stringtokenizer.hasMoreTokens())
                password[i] = stringtokenizer.nextToken();
            if(stringtokenizer.hasMoreTokens())
                url[i] = stringtokenizer.nextToken();
        } while(++i < maxurls);
    }

    public void actionPerformed(ActionEvent actionevent)
    {
        String s = PasswordField.getText();
        String s1 = "";
        String s2 = getDocumentBase().toString();
        s2 = s2.substring(0, s2.lastIndexOf('/') + 1);
        for(int i = 0; i < maxurls; i++)
            if(password[i] != null && url[i] != null && s.compareTo(password[i]) == 0)
            {
                s1 = s2 + url[i];
                try
                {
                    getAppletContext().showDocument(new URL(s1), m_t);
                }
                catch(Exception exception1)
                {
                    exception1.printStackTrace();
                }
            }

        s1 = s2 + "level106.php";
        try
        {
            getAppletContext().showDocument(new URL(s1), m_t);
            return;
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
        String s = getParameter("target");
        if(s != null)
            m_t = new String(s);
        s = getParameter("folder");
        if(s != null)
            readFile(s + "word.txt");
        else
            readFile("word.txt");
        SubmitButton.setLabel("submit");
        SubmitButton.addActionListener(this);
        PasswordField.setEchoChar('*');
        PasswordField.setForeground(new Color(192, 192, 192));
        add(PasswordField);
        add(SubmitButton);
        setBackground(new Color(0, 0, 0));
    }

    int maxurls;
    private Button SubmitButton;
    private TextField PasswordField;
    private String m_t;
    private String password[];
    private String url[];
}
