import java.net.MalformedURLException;
import java.net.URL; 
import java.util.Arrays;
import java.util.HashMap;
import java.util.logging.Level;
import java.util.logging.Logger;
import org.apache.xmlrpc.client.XmlRpcClient;
import org.apache.xmlrpc.client.XmlRpcClientConfigImpl;

class Example2 {
    private final static Logger LOGGER = Logger.getLogger(Logger.GLOBAL_LOGGER_NAME);
    
    public static XmlRpcClient getXmlRpcClient(String url) {
        XmlRpcClient xmlRpcClient = new XmlRpcClient();
        try {
            XmlRpcClientConfigImpl config = new XmlRpcClientConfigImpl();
            config.setServerURL(new URL(url));
            xmlRpcClient.setConfig(config);
        } catch (MalformedURLException ex) {
            LOGGER.log(Level.SEVERE, null, ex);
        }
        return xmlRpcClient;
    }

    public static void main(String args[]) {
        try {
            XmlRpcClient client = getXmlRpcClient("http://localhost:8000");
            client.execute("test_mode", new Object[]{
                Arrays.asList(new Integer[]{4, 8}, new Integer[]{9, 3})
            });

            HashMap<String, Integer> id1 = new HashMap<String, Integer>() {{ put("id", 1); }};
            HashMap<String, Integer> id2 = new HashMap<String, Integer>() {{ put("id", 2); }};

            System.out.println("Someone on floor #4 requested to go to floor #8");
            client.execute("service", new Object[]{ new Integer[]{4, 8}, id1 });
            System.out.println("Someone on floor #9 requested to go to floor #3");
            client.execute("service", new Object[]{ new Integer[]{9, 3}, id2 });

            client.execute("move", new Object[]{2, id1});
            client.execute("move", new Object[]{2, id2});
            client.execute("move", new Object[]{3, id1});
            client.execute("move", new Object[]{3, id2});
            client.execute("move", new Object[]{4, id1});
            client.execute("move", new Object[]{4, id2});
            client.execute("pickup", new Object[]{id1});
            client.execute("move", new Object[]{5, id1});
            client.execute("move", new Object[]{5, id2});
            client.execute("move", new Object[]{6, id1});
            client.execute("move", new Object[]{6, id2});
            client.execute("move", new Object[]{7, id1});
            client.execute("move", new Object[]{7, id2});
            client.execute("move", new Object[]{8, id1});
            client.execute("move", new Object[]{8, id2});
            client.execute("dropoff", new Object[]{id1});
            client.execute("move", new Object[]{9, id2});
            client.execute("pickup", new Object[]{id2});
            client.execute("move", new Object[]{8, id2});
            client.execute("move", new Object[]{7, id2});
            client.execute("move", new Object[]{6, id2});
            client.execute("move", new Object[]{5, id2});
            client.execute("move", new Object[]{4, id2});
            client.execute("move", new Object[]{3, id2});
            client.execute("dropoff", new Object[]{id2});

            // Invalid jump from floor 3 to floor 1
            client.execute("move", new Object[]{1, id2});

            // Invalid jump from floor 8 to floor 1
            client.execute("move", new Object[]{1, id1});
        } catch (Exception ex) {
            LOGGER.log(Level.SEVERE, null, ex);
        }
    }
}
