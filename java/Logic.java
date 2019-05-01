import java.net.MalformedURLException;
import java.net.URL; 
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.logging.Level;
import java.util.logging.Logger;
import org.apache.xmlrpc.client.XmlRpcClient;
import org.apache.xmlrpc.client.XmlRpcClientConfigImpl;

class Logic {
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
            ArrayList<ArrayList<Integer>> floor_requests = new ArrayList<ArrayList<Integer>>();

            XmlRpcClient client = getXmlRpcClient("http://localhost:8000");
            client.execute("reset", new Object[0]);
            
            while(true) {
                Object[] response = (Object[]) client.execute("check_for_elevator_request", new Object[0]);

                ArrayList<Integer> floor_request = new ArrayList<Integer>();
                for (Object o : response) {
                    floor_request.add((Integer) o);
                }

                if (floor_request.isEmpty()) {
                    System.out.println(".");
                } else {
                    floor_requests.add(floor_request);

                    System.out.printf("Someone on floor #%d requested to go to floor # %d", 
                            floor_request.get(0), floor_request.get(1));
                }

                Thread.sleep(1000);
            }
        } catch (Exception ex) {
            LOGGER.log(Level.SEVERE, null, ex);
        }
    }
}
