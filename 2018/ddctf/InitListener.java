package com.didichuxing.ctf.listener;

import com.didichuxing.ctf.model.Flag;
import com.didichuxing.ctf.service.FlagService;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintStream;
import java.security.InvalidKeyException;
import java.security.Key;
import java.security.KeyStore;
import java.security.KeyStoreException;
import java.security.NoSuchAlgorithmException;
import java.security.SecureRandom;
import java.security.UnrecoverableKeyException;
import java.security.cert.CertificateException;
import java.util.Properties;
import java.util.UUID;
import javax.crypto.BadPaddingException;
import javax.crypto.Cipher;
import javax.crypto.IllegalBlockSizeException;
import javax.crypto.Mac;
import javax.crypto.NoSuchPaddingException;
import javax.crypto.spec.SecretKeySpec;
import javax.servlet.ServletContext;
import org.apache.commons.io.FileUtils;
import org.springframework.beans.factory.InitializingBean;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.ApplicationContext;
import org.springframework.context.ApplicationEvent;
import org.springframework.context.ApplicationListener;
import org.springframework.web.context.WebApplicationContext;

public class InitListener
  implements ApplicationListener, InitializingBean
{
  final String k = "sdl welcome you !";

  @Autowired
  private FlagService flagService;
  private Properties properties = new Properties();
  private String p;

  public void afterPropertiesSet() throws Exception {
    System.out.println("afterPropertiesSet");
    try
    {
      InputStream inputStream = getClass().getClassLoader().getResourceAsStream("/properties/conf.properties");
      this.properties.load(inputStream);
    } catch (Exception e) {
      e.printStackTrace();
    }

    this.p = "sdl welcome you !".substring(0, "sdl welcome you !".length() - 1).trim().replace(" ", "");
  }

  public void onApplicationEvent(ApplicationEvent event)
  {
    if (!(event.getSource() instanceof ApplicationContext)) {
      return;
    }
    WebApplicationContext ctx = (WebApplicationContext)event.getSource();
    if (ctx.getParent() != null) {
      return;
    }

    String regenflag = this.properties.getProperty("regenflag");
    if ((regenflag != null) && ("false".equals(regenflag))) {
      System.out.println("skip gen flag");
      return;
    }

    try
    {
      this.flagService.deleteAll();
      int id = 1;

      String path = ctx.getServletContext().getRealPath("/WEB-INF/classes/emails.txt");
      String ksPath = ctx.getServletContext().getRealPath("/WEB-INF/classes/sdl.ks");
      System.out.println(path);

      String emailsString = FileUtils.readFileToString(new File(path), "utf-8");
      String[] emails = emailsString.trim().split("\n");

      KeyStore keyStore = KeyStore.getInstance(KeyStore.getDefaultType());
      FileInputStream inputStream = new FileInputStream(ksPath);
      keyStore.load(inputStream, this.p.toCharArray());
      Key key = keyStore.getKey("www.didichuxing.com", this.p.toCharArray());
      Cipher cipher = Cipher.getInstance(key.getAlgorithm());
      cipher.init(1, key);
      SecretKeySpec signingKey = new SecretKeySpec("sdl welcome you !".getBytes(), "HmacSHA256");
      Mac mac = Mac.getInstance("HmacSHA256");
      mac.init(signingKey);

      SecureRandom sr = new SecureRandom();
      for (String email : emails) {
        String flag = "DDCTF{" + Math.abs(sr.nextLong()) + "}";
        String uuid = UUID.randomUUID().toString().replace("-", "s");

        byte[] data = cipher.doFinal(flag.getBytes());
        byte[] e = mac.doFinal(String.valueOf(email.trim()).getBytes());

        Flag flago = new Flag();
        flago.setId(Integer.valueOf(id));
        flago.setFlag(byte2hex(data));
        flago.setEmail(byte2hex(e));
        flago.setOriginFlag(flag);
        flago.setUuid(uuid);
        flago.setOriginEmail(email);

        this.flagService.save(flago);
        System.out.println(email + "同学的入口链接为：http://116.85.48.102:5050/welcom/" + uuid);
        id++;
        System.out.println(flago);
      }
    }
    catch (KeyStoreException e)
    {
      e.printStackTrace();
    } catch (IOException e) {
      e.printStackTrace();
    } catch (NoSuchAlgorithmException e) {
      e.printStackTrace();
    } catch (CertificateException e) {
      e.printStackTrace();
    } catch (UnrecoverableKeyException e) {
      e.printStackTrace();
    } catch (NoSuchPaddingException e) {
      e.printStackTrace();
    } catch (InvalidKeyException e) {
      e.printStackTrace();
    } catch (IllegalBlockSizeException e) {
      e.printStackTrace();
    } catch (BadPaddingException e) {
      e.printStackTrace();
    }
  }

  public static String byte2hex(byte[] b)
  {
    StringBuilder hs = new StringBuilder();

    for (int n = 0; (b != null) && (n < b.length); n++) {
      String stmp = Integer.toHexString(b[n] & 0xFF);
      if (stmp.length() == 1)
        hs.append('0');
      hs.append(stmp);
    }
    return hs.toString().toUpperCase();
  }
}