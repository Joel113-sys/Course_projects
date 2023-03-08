import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.GridBagConstraints;
import java.awt.GridBagLayout;
import java.awt.Image;
import java.awt.Insets;
import java.awt.Point;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.StringTokenizer;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import javax.swing.JTextField;
import javax.swing.ScrollPaneConstants;


/**
 * This class implements the CardGameGUI interface. It is used to build a GUI 
 * for the BigTwo card game and handle all user actions.
 * @author joellau
 *
 */
public class BigTwoGUI implements CardGameUI{
	
	private BigTwo game; //A Big Two game associates with this GUI.
	private boolean[] selected; //A boolean array indicating which cards are being selected.
	private int activePlayer; //An integer specifying the index of the active player.
	private JFrame frame; //The main window of the application.
	private JPanel bigTwoPanel; //A panel showing the cards of each player.
	private JButton playButton; //A button for the active player to play the selected cards.
	private JButton passButton; //A button for the active player to pass the turn.
	private JTextArea msgArea; //A text area for showing the current game status as well as the end of game massages.
	private JTextArea chatArea; //A text area for showing chat messages.
	private JTextField chatInput; //A text field for players to input chat messages.
	private ArrayList<CardGamePlayer> playerList = new ArrayList<CardGamePlayer>();  //An ArrayList containing players of the game.
	private Image[][] cardImage = new Image[13][4]; //A list containing all card images.
	private ArrayList<Hand> handsOnTable; // A list of hands played on the table.
	private Image cardback; //The image of the back of cards.
	private Image[] avatars = new Image[4]; //A list of avatars of players.
	
	/**
	 * A constructor for creating a BigTwoGUI.
	 * @param game An instance simulates a BigTwo game.
	 */
	public BigTwoGUI(BigTwo game) {
		this.game = game;
		//create the frame
		frame = new JFrame();
		frame.setTitle("Big Two");
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setSize(1000,800);
		frame.setResizable(true);
		
		setActivePlayer(game.getCurrentPlayerIdx());
		handsOnTable = game.getHandsOnTable();
		playerList = game.getPlayerList();
		char[] num_arr = {'a','2','3','4','5','6','7','8','9','t','j','q','k'};
		char[] suit_arr = {'d','c','h','s'}; 
		//load the card images
		for (int i = 0; i < num_arr.length; i++) {
			for (int j = 0; j < suit_arr.length; j++) {
				Image image = new ImageIcon("cards/"+num_arr[i]+suit_arr[j]+".gif").getImage();
				cardImage[i][j] = image;
			}
		}
		//load the image of the back of cards
		cardback = new ImageIcon("cards/cardback.gif").getImage();
		for (int i = 0; i < 4; i++) {
			Image image = new ImageIcon("avatars/"+i+".png").getImage();
			avatars[i] = image;
		}
		this.selected = new boolean[13];
		//create the bigTwoPanel
		this.bigTwoPanel = new BigTwoPanel();
		bigTwoPanel.addMouseListener((BigTwoPanel)bigTwoPanel);
		playButton = new JButton("Play");
		passButton = new JButton("Pass");
		playButton.addActionListener(new PlayButtonListener());
		passButton.addActionListener(new PassButtonListener());
		//create other widgets
		JMenuBar menuBar = new JMenuBar();
        JMenu gameMenu = new JMenu("Game");
        JMenuItem connect = new JMenuItem("Connect");
        JMenuItem quit = new JMenuItem("Quit");
        connect.addActionListener(new ConnectButtonListener());
        quit.addActionListener(new QuitMenuItemListener());
        gameMenu.add(connect);
        gameMenu.add(quit);
        menuBar.add(gameMenu);
        JPanel panel = new JPanel();
        //adopt GridBagLayout
        panel.setLayout(new GridBagLayout());
		GridBagConstraints c = new GridBagConstraints();
		c.gridx = 0;
		c.gridy = 0;
		c.gridwidth = 1;
		c.gridheight = 1;
		c.weightx = 0.0;
		c.weighty = 0.0;
		c.anchor = GridBagConstraints.CENTER;
		c.fill = GridBagConstraints.BOTH;
		
		c.gridx = 0;
		panel.add(playButton,c);
		c.gridx = 1;
		panel.add(passButton,c);
		c.gridx = 2;
		JLabel msglabel = new JLabel("Message: ");
		panel.add(msglabel);
        chatInput = new JTextField(5);
        chatInput.addActionListener(new EnterListener());
        c.gridx = 3;
        panel.add(chatInput,c);
       
		frame.setLayout(new GridBagLayout());
		
		c.gridx = 0;
		c.gridy = 0;
		c.gridheight = 2;
		c.weightx = 2;
		//c.weighty = 1;
		frame.add(bigTwoPanel,c);
		
		msgArea = new JTextArea(40,35);
		msgArea.setBackground(Color.white);
		msgArea.setEditable(false);
		
		JScrollPane scroller = new JScrollPane(msgArea);
        scroller.setVerticalScrollBarPolicy(
              ScrollPaneConstants.VERTICAL_SCROLLBAR_ALWAYS);
        scroller.setHorizontalScrollBarPolicy(
              ScrollPaneConstants.HORIZONTAL_SCROLLBAR_NEVER);
		c.gridx = 1;
		c.gridy = 0;
		c.weightx = 1;
		c.weighty = 1;
		c.gridheight = 1;
		frame.add(scroller,c);
		//create the chat area
        chatArea = new JTextArea(40,35);
		chatArea.setEditable(false);
		c.gridx = 1;
		c.gridy = 1;
		c.weightx = 1;
		c.weighty = 1;
		frame.add(chatArea,c);
		c.gridx = 0;
		c.gridy = 2;
		c.gridwidth = 2;
		c.weighty = 0.1;
		frame.add(panel,c);
		frame.setJMenuBar(menuBar);
		frame.setVisible(true);
	}


	/**
	 * This method sets the index of the active player.
	 * @param activePlayer An integer that refers to a specific player.
	 */
	public void setActivePlayer(int activePlayer) {
		if (activePlayer < 0 || activePlayer >= playerList.size()) {
			this.activePlayer = -1;
		} else {
			this.activePlayer = activePlayer;
		}
	}
	
	/**
	 * This method repaints the GUI.
	 */
	public void repaint() {
		frame.repaint();
	}
	
	/**
	 * This method prints the specified string to the message area of the GUI.
	 * @param msg The message to print on the msgArea.
	 */
	public void printMsg(String msg) {
		msgArea.append(msg);
	}
	
	/**
	 * This method prints the specified string to the chat area of the GUI.
	 * @param msg The message to print on the chatArea.
	 */
	public void printChat(String msg) {
		chatArea.append(msg);
	}
	
	/**
	 *This method clears the message area if the GUI.
	 */
	public void clearMsgArea() {
		msgArea.setText(null);
	}
	
	/**
	 * This method resets the GUI.
	 */
	public void reset() {
		resetSelected();
		clearMsgArea();
		enable();
	}
	
	/**
	 * This method enables user interactions with the GUI.
	 */
	public void enable() {
		playButton.setEnabled(true);
		passButton.setEnabled(true);
	}
	
	/**
	 * This method disables user interactions with the GUI.
	 */
	public void disable() {
		playButton.setEnabled(false);
		passButton.setEnabled(false);
	}
	
	/**
	 * This method prompts the active player to select cards and make his/her move.
	 */
	public void promptActivePlayer() {
		resetSelected();
		printMsg(game.getPlayerList().get(activePlayer).getName()+"'s turn:\n");
	}
	
	/**
	 * Returns an array of indices of the cards selected through the GUI.
	 * 
	 * @return an array of indices of the cards selected, or null if no valid cards
	 *         have been selected
	 */
	public int[] getSelected() {
		int count =0;
		CardGamePlayer player = playerList.get(activePlayer);
		//count the number of cards be selected
		for(int i = 0; i < player.getNumOfCards(); i++) {
			if(selected[i]) count++;
		}
		if(count !=0) {
			int[] cardIdx = new int[count];
			count=0;
			//get the index of the selected cards
			for(int i = 0;i <  player.getNumOfCards();++i) {
				if(selected[i])
					cardIdx[count++]=i;
			}
			return cardIdx;
		}
		return null;
	}
	
	/**
	 * Resets the list of selected cards to an empty list.
	 */
	public void resetSelected() {
		for (int j = 0; j < selected.length; j++) {
			selected[j] = false;
		}
	}

	/**
	 * A method that checks if a MouseClick is on a card.
	 * @param p The location of mouse click.
	 * @return True if the mouse click is on a card, false otherwise.
	 */
	public boolean contain_click(Point p) {
		int x =p.x;
		int y =p.y;
		CardGamePlayer player = playerList.get(activePlayer);
		int numOfCards = player.getNumOfCards(); //the number of cards current player has in hand.
		//check if the mouse click is on the card.
		if (y < 30 + 142 * activePlayer - 10 || y > 30 + 80 + 142 * activePlayer) {
			return false;
		}
		if (x < 145 || x > 145 + (numOfCards - 1) * 14 + 73) {
			return false;
		}
		//obtain the index of the clicked card.
		int cardIdx = (x - 145) / 14;
		if (cardIdx >= numOfCards) {
			cardIdx = numOfCards - 1;
		}
		//check the overlap area of the unselected card(the selected card will rise up)
		if (y >= 30 + 142 * activePlayer + 80 - 10 && y <= 30 + 142 * activePlayer + 80) {
			for (int i = cardIdx; i > (cardIdx - 5 > 0 ? cardIdx - 5 : -1); i--) { 
				if (!selected[i] && x <= 145 + i * 14 + 73) {
					selected[i] = !selected[i];
					return true;
				}
			}
		}
		//check the overlap area of the selected card (the unselected card will fall)
		if (y >= 30 + 142 * activePlayer - 10 && y <= 30+142*activePlayer) {
			for (int i=cardIdx; i > (cardIdx - 5 > 0 ? cardIdx - 5: -1);i--) {
				if(selected[i] && x<=145+i*14+73) {
					selected[i] = !selected[i];
					return true;
				}
			}
		}
		//the selected card will be raise in location.
		if(selected[cardIdx]) { 
			if(y >= 30 + 142 * activePlayer-10 && y <= 30 + 80 + 142 * activePlayer - 10) {
				selected[cardIdx]=!selected[cardIdx];
				return true;
			}
		}
		else {//the unselected cards are lower
			if(y >= 30 + 142 * activePlayer && y <= 30 + 80 + 142 * activePlayer) {
				selected[cardIdx] =! selected[cardIdx];
				return true;
			}
		}
		return false;
	}
	
	/**
	 * An inner class that extends the JPanel class and implements the MouseListener interface.
	 * @author joellau
	 *
	 */
	class BigTwoPanel extends JPanel implements MouseListener {
		
		@Override
		public void paintComponent(Graphics g) {
			g.setColor(Color.green);
			g.fillRect(0, 0, 1000, 800);
			g.setColor(Color.black);
			
			for (int i=0; i < game.getPlayerList().size();++i) {
				if (game.getPlayerList().get(i) != null)
				{
					g.drawString(game.getPlayerList().get(i).getName(), 80, 30 + 142 * i - 10);
					g.drawImage(avatars[i], 40, 40 + 142 * i, 80, 80, this);
					CardList cards = game.getPlayerList().get(i).getCardsInHand();
					for (int j = 0; j < 13; j++) {
						Card card = cards.getCard(j);
						if (card == null) { 
							break;
						}
						int x = 145 + j * 14;
						int y = 30 + 142 * i;
						if (i == activePlayer && selected[j]) {
							y -= 10;
						}
						if(!game.endOfGame() && i != game.getClient().getPlayerID()) {
							g.drawImage(cardback,x, y,80,80, this);
						}
						else{
							g.drawImage(cardImage[card.getRank()][card.getSuit()],x, y, 80,80, this);
						}
					}
				}
			}
			if (!game.getHandsOnTable().isEmpty()) {
				Hand lastHand = game.getHandsOnTable().get(game.getHandsOnTable().size()-1);
				g.drawString("Played by "+lastHand.getPlayer().getName(), 10, 30 + 142 * 4 - 10);
				for (int j = 0;j < lastHand.size(); j++) {
					Card card = lastHand.getCard(j);
					int x = 10 + j * 14;
					int y = 30 + 142 * 4;
					g.drawImage(cardImage[card.getRank()][card.getSuit()], x, y, this);
				}
			}
			else {
				g.drawString("No player played cards", 10, 30 + 142 * 4 - 10);
			}
		}
		
		/**
		 * This method is to handle mouse click events.
		 * @param MouseEvent e A mouse event created by the event source.
		 */
		public void mouseReleased(MouseEvent e) {
			if (game.getClient().getStartGame()) {
				if(contain_click(e.getPoint())) {
					frame.repaint();
				}
			}
		}

		/* (non-Javadoc)
		 * @see java.awt.event.MouseListener#mousePressed(java.awt.event.MouseEvent)
		 */
		@Override
		public void mouseClicked(MouseEvent e) {}

		/* (non-Javadoc)
		 * @see java.awt.event.MouseListener#mousePressed(java.awt.event.MouseEvent)
		 */
		@Override
		public void mousePressed(MouseEvent e) {}

		/* (non-Javadoc)
		 * @see java.awt.event.MouseListener#mousePressed(java.awt.event.MouseEvent)
		 */
		@Override
		public void mouseEntered(MouseEvent e) {}

		/* (non-Javadoc)
		 * @see java.awt.event.MouseListener#mousePressed(java.awt.event.MouseEvent)
		 */
		@Override
		public void mouseExited(MouseEvent e) {}
	}
	
	/**
	 * An inner class that implements the ActionListener interface. It listens the "play" button actions
	 * and handles button click events.
	 * @author joellau
	 *
	 */
	class PlayButtonListener implements ActionListener{
		public void actionPerformed(ActionEvent e) {
			if (getSelected()==null) {
				return;
			}
			else {
				game.makeMove(activePlayer, getSelected());
			}
		}
	}
	
	/**
	 * An inner class that implements the ActionListener interface. It listens the "pass" button actions
	 * and handles button click events.
	 * @author joellau
	 *
	 */
	class PassButtonListener implements ActionListener{
		public void actionPerformed(ActionEvent e) {
			game.makeMove(activePlayer, null);
		}
	}
	
	/**
	 * An inner class that implements the ActionListener interface to listen to the "connect" button 
	 * actions and establishes a connection to the server.
	 * @author joellau
	 *
	 */
	class ConnectButtonListener implements ActionListener{
		public void actionPerformed(ActionEvent e) {
			game.getClient().connect();
		}
	}
	
	/**
	 * An inner class that implements the ActionListener interface to listen to the "quit" button 
	 * actions and quit the game.
	 * @author joellau
	 *
	 */
	class QuitMenuItemListener implements ActionListener{
		public void actionPerformed(ActionEvent e) {
			System.exit(0);
		}
	}
	
	/**
	 * An inner class that implements the ActionListener interface to listen to "Enter" actions and 
	 * send messages to the chatArea.
	 * @author joellau
	 *
	 */
	class EnterListener implements ActionListener{
		public void actionPerformed(ActionEvent e) {
			String input=chatInput.getText();
            chatInput.setText(null);
            game.getClient().sendMessage(new CardGameMessage(CardGameMessage.MSG,-1,input+"\n"));
		}
	}
}
