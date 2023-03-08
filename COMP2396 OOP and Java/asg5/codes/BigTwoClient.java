import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.Socket;
import java.util.ArrayList;
import javax.swing.JOptionPane;

/**
 * A class that implements the NetworkGame interface, and is used to model a Big Two game client
 * that is responsible for establishing a connection and communicating with the Big Two game server.
 * @author joellau
 *
 */
public class BigTwoClient implements NetworkGame{
	
	private BigTwo game; //the BitTwo game
	private BigTwoGUI gui;//The GUI of the game
	private Socket sock; //A socket to the game server
	private ObjectOutputStream oos;//An ObjectOutputStream for sending messages to the server.
	private int playerID; //The ID of the player
	private String playerName; //The name of the local player
	private String serverIP; //The server's IP address
	private int serverPort; //An integer specifying the TCP port of the game server.
	private ArrayList <CardGamePlayer> playerList;
	private boolean startGame; //A boolean variable indicating if the game has started or not
	private boolean connected; //A boolean variable indicating if a client has been connected to a server.
	
	/**
	 * A constructor for creating a Big Two client.
	 * @param game A reference to a BigTwo object associated with this client.
	 * @param gui A reference to a BigTwoGUI object associated with the BigTwo object.
	 */
	public BigTwoClient(BigTwo game, BigTwoGUI gui) {
		this.game = game;
		this.gui = gui;
		this.playerList = game.getPlayerList();
		this.startGame = false;
		this.connected = false;
		setServerIP("127.0.0.1");
		setServerPort(2396);
		String name = (String) JOptionPane.showInputDialog("Please enter your name:");
		if (name == null) {
			name = "";
		}
		setPlayerName(name);
		gui.disable();
		connect();
	}
	
	/**
	 * A public getter of the startGame variable
	 * @return A boolean variable indicating if the game has started
	 */
	public boolean getStartGame() {
		return this.startGame;
	}
	
	/**
	 * Returns the playerID (index) of the local player.
	 * 
	 * @return the playerID (index) of the local player
	 */
	public int getPlayerID() {
		return this.playerID;
	}
	
	/**
	 * Sets the playerID (index) of the local player.
	 * 
	 * @param playerID the playerID (index) of the local player.
	 */
	public synchronized void setPlayerID(int playerID) {
		this.playerID = playerID;
	}
	
	/**
	 * Returns the name of the local player.
	 * 
	 * @return the name of the local player
	 */
	public String getPlayerName() {
		return this.playerName;
	}
	
	/**
	 * Sets the name of the local player.
	 * 
	 * @param playerName
	 *            the name of the local player
	 */
	public synchronized void setPlayerName(String playerName) {
		this.playerName = playerName;
	}
	
	/**
	 * Returns the IP address of the server.
	 * 
	 * @return the IP address of the server
	 */
	public String getServerIP() {
		return this.serverIP;
	}
	
	/**
	 * Sets the IP address of the server.
	 * 
	 * @param serverIP
	 *            the IP address of the server
	 */
	public void setServerIP(String serverIP) {
		this.serverIP = serverIP;
	}
	
	/**
	 * Returns the TCP port of the server.
	 * 
	 * @return the TCP port of the server
	 */
	public int getServerPort() {
		return this.serverPort;
	}
	
	/**
	 * Sets the TCP port of the server
	 * 
	 * @param serverPort
	 *            the TCP port of the server
	 */
	public void setServerPort(int serverPort) {
		this.serverPort = serverPort;
	}
	
	/**
	 * This method makes a network connection to the server.
	 */
	public void connect() {
		if(connected) {
			gui.printMsg("Already connected to server!\n");
			return;
			}
		try {
			connected = true;
			sock = new Socket(this.serverIP, this.serverPort);
			oos = new ObjectOutputStream(sock.getOutputStream());
			ServerHandler threadJob = new ServerHandler();
			Thread myThread = new Thread(threadJob); 
			myThread.start();
		} catch (Exception ex){
			gui.printMsg("Server connection failed.\n");
			connected = false;
			ex.printStackTrace();
		}
	};
	
	/**
	 * This method parses the specified message received from the server.
	 * 
	 * @param message
	 *            the specified message received from the server
	 */
	public synchronized void parseMessage(GameMessage message) {
		switch (message.getType()) {
		case CardGameMessage.PLAYER_LIST:
			String[] names=(String[])message.getData();
			for (int i = 0;i < game.getPlayerList().size(); i++) {
				if(names[i] != null) {
					game.getPlayerList().set(i,new CardGamePlayer(names[i]));
				}
				else {
					game.getPlayerList().set(i, null);
				}
			}
			setPlayerID(message.getPlayerID());
			sendMessage(new CardGameMessage(CardGameMessage.JOIN, -1, playerName));
			gui.repaint();
			break;
		case CardGameMessage.JOIN:
			game.getPlayerList().set(message.getPlayerID(), new CardGamePlayer((String)message.getData()));
			gui.printMsg(playerList.get(message.getPlayerID()).getName() + " joined the game.\n");
			gui.repaint();
			if (this.playerID == message.getPlayerID()) {
				sendMessage(new CardGameMessage(CardGameMessage.READY, -1, null));
			}
			break;
		case CardGameMessage.FULL:
			gui.printMsg("Game Server is full!\n");
			gui.repaint();
			break;
		case CardGameMessage.QUIT:
			if(!game.endOfGame()) {
				this.startGame = false;
				game.getHandsOnTable().clear();
				for(int i = 0; i < 4; i++) {
					playerList.get(i).removeAllCards();
				}
				sendMessage(new CardGameMessage(CardGameMessage.READY, -1, null));
			}
			gui.printMsg( this.playerList.get(message.getPlayerID()).getName() + " left the game.\n");
			game.getPlayerList().set(message.getPlayerID(),null);
			gui.disable();
			gui.repaint();
			break;
		case CardGameMessage.READY:
			gui.printMsg(playerList.get(message.getPlayerID()).getName() + " is ready!\n");
			gui.repaint();
			break;
		case CardGameMessage.START:
			gui.printMsg("Game starts!\n");
			this.startGame = true;
			BigTwoDeck deck = new BigTwoDeck();
			deck = (BigTwoDeck) message.getData();
			game.start(deck);
			gui.repaint();
			break;
		case CardGameMessage.MOVE:
			game.checkMove(message.getPlayerID(), (int[])message.getData());
			gui.repaint();
			break;
		case CardGameMessage.MSG:
			gui.printChat((String)message.getData());
			break;
		default:
			System.out.print("Unrecognized message!");
			break;
		}
	}
	
	/**
	 * This method sends the specified message to the server.
	 * 
	 * @param message
	 *            the specified message to be sent the server
	 */
	public void sendMessage(GameMessage message) {
		try {
			oos.writeObject(message);
		} catch(Exception ex) {
			gui.printMsg("Failure to send messages!\n");
			ex.printStackTrace();
		}
	}
	
	
	/**
	 * An inner class that implements the Runnable interface.
	 * @author joellau
	 *
	 */
	class ServerHandler implements Runnable{
		private ObjectInputStream ois;
		
		/**
		 * A constructor of ServerHandler class.
		 */
		public ServerHandler() {
			try {
				ois = new ObjectInputStream(sock.getInputStream());
			} catch (Exception ex) {
				gui.printMsg("Failure on input stream!\n");
				ex.printStackTrace();
			}
		}
		
		/**
		 * A method that will be put on top of the thread's stack when start() is called.
		 */
		public void run() {
			try {
				while(true) {
					CardGameMessage msg = (CardGameMessage) ois.readObject();
					parseMessage(msg);
				}
			} catch (Exception ex) {
				connected = false;
				gui.disable();
				ex.printStackTrace();
			}
		}
	}
}
