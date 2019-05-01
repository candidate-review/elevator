import java.net.MalformedURLException;
import java.net.URL; 
import java.util.Arrays;
import java.util.logging.Level;
import java.util.logging.Logger;
import org.apache.xmlrpc.client.XmlRpcClient;
import org.apache.xmlrpc.client.XmlRpcClientConfigImpl;

class Example {
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

    // Create an Array Param
    public static Object[] aParam(Object obj) {
        return new Object[] { obj };
    }

    public static void main(String args[]) {
        try {
            XmlRpcClient client = getXmlRpcClient("http://localhost:8000");
            client.execute("test_mode", aParam(
                Arrays.asList(new Integer[] {4, 8}, new Integer[] {9, 3})
            ));

            System.out.println("Someone on floor #4 requested to go to floor #8");
            client.execute("service", aParam(new Integer[]{4, 8}));
            client.execute("move", new Integer[]{2});
            client.execute("move", new Integer[]{3});
            client.execute("move", new Integer[]{4});
            client.execute("pickup", new Object[0]); // << pick up on 4
            client.execute("move", new Integer[]{5});
            client.execute("move", new Integer[]{6});
            client.execute("move", new Integer[]{7});
            client.execute("move", new Integer[]{8});
            client.execute("dropoff", new Object[0]); // << drop off on 8

            System.out.println("Someone on floor #9 requested to go to floor #3");
            client.execute("service", aParam(new Integer[]{9, 3}));
            client.execute("move", new Integer[]{9});
            client.execute("pickup", new Object[0]); // << pick up on 9
            client.execute("move", new Integer[]{8});
            client.execute("move", new Integer[]{7});
            client.execute("move", new Integer[]{6});
            client.execute("move", new Integer[]{5});
            client.execute("move", new Integer[]{4});
            client.execute("move", new Integer[]{3});
            client.execute("dropoff", new Object[0]); // << drop off on 3

            // Invalid jump from floor 3 to floor 1
            client.execute("move", new Integer[]{1});
        } catch (Exception ex) {
            LOGGER.log(Level.SEVERE, null, ex);
        }
    }
}
