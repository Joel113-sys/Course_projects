import java.util.ArrayList;
import javax.swing.JOptionPane;

/**
 * This class models a Big Two card game.
 * @author joellau
 *
 */
public class BigTwo implements CardGame{
	private int numOfPlayers;
	private Deck deck;
	private ArrayList<CardGamePlayer> playerList = new ArrayList<CardGamePlayer>();
	private ArrayList<Hand> handsOnTable = new ArrayList<Hand>();
	private int currentPlayerIdx;
	private BigTwoGUI gui;
	private BigTwoClient client;
	
	/**
	 * This is the default constructor of the class.
	 */
	public BigTwo() {
		for(int i = 0;i < 4; i++) {
			playerList.add(null);
		}
		this.gui = new BigTwoGUI(this);
		this.client = new BigTwoClient(this, gui);
	}
	
	/**
	 * The getter of numOfPlayers.
	 * @return An integer specifying the number of players
	 */
	public int getNumOfPlayers() {
		return this.numOfPlayers;
	}
	
	/**
	 * The getter of the deck.
	 * @return The deck in the BigTwo card game.
	 */
	public Deck getDeck() {
		return this.deck;
	}
	
	/**
	 * The getter of the player list.
	 * @return An ArrayList containing all players in the game.
	 */
	public ArrayList<CardGamePlayer> getPlayerList(){
		return this.playerList;
	}
	
	/**
	 * The getter of handsOnTable.
	 * @return A Hand ArrayList containing the hands have been played.
	 */
	public ArrayList<Hand> getHandsOnTable(){
		return this.handsOnTable;
	}
	
	/**
	 * The getter of currentPlayerIdx.
	 * @return A integer specifying the index of current player in playerList.
	 */
	public int getCurrentPlayerIdx() {
		return currentPlayerIdx;
	}
	
	/**
	 * The getter of the client
	 * @return The client of the game.
	 */
	public BigTwoClient getClient() {
		return this.client;
	}
	
	/**
	 * This method  starts the game.
	 * @param The deck used in the BigTwo card game.
	 */
	public void start(Deck deck) {
		//clear all hands on the table first
		handsOnTable.clear();
		for (int n = 0; n < 4; n++) {
			CardGamePlayer player = playerList.get(n);
			player.removeAllCards();
			//distribute 13 to each player
			for (int i = 0; i < 13; i++) {
				BigTwoCard addedCard = (BigTwoCard) deck.getCard(n * 13 + i);
				player.addCard(addedCard);
				//determine the first player to play
				if (addedCard.suit == 0 && addedCard.rank == 2) {
					currentPlayerIdx = n;
					gui.setActivePlayer(n);
				}
			}
			//sort the cards in hand based on the rule of Big Two
			player.sortCardsInHand();
		}
		if (currentPlayerIdx == client.getPlayerID()) {
			gui.enable();
		}
		this.gui.repaint();
		gui.promptActivePlayer();
	}
	
	/**
	 * This method makes a move by a player with the specified index using the cards specified by a list of indexes.
	 * @param playerIdx An integer specifying the index of the current player.
	 * @param cardIdx An array of integer containing the indexes of the cards selected by the player.
	 */
	public void makeMove(int playIdx, int[] cardIdx) {
		CardGameMessage message = new CardGameMessage(CardGameMessage.MOVE, client.getPlayerID(), cardIdx);
		client.sendMessage(message);
	}
	
	/**
	 *  This method checks a move made by a player. This is called inside the makeMove method.
	 * @param playerIdx -An integer specifying the index of the current player.
	 * @param cardIdx -An array of integer containing the indexes of the cards selected by the player.
	 */
	public void checkMove(int playIdx, int[] cardIdx) {
		CardGamePlayer player = playerList.get(playIdx);
		CardList cards = player.play(cardIdx);
		Hand hand = composeHand(this.playerList.get(playIdx),cards);
		Card first_card = new Card(0,2);
		
		if(hand!=null) {
			if (handsOnTable.size() != 0) {
				if (handsOnTable.get(handsOnTable.size() - 1).getPlayer() != player) {
					if (hand.beats(handsOnTable.get(handsOnTable.size() - 1))) {
						this.playerList.get(playIdx).removeCards(cards);
						this.handsOnTable.add(hand);
						gui.printMsg("{"+hand.getType()+"} ");
						gui.printMsg(printHand(hand)+"\n");
						nextPlayer();
					}
					else {
						gui.printMsg("Not a legal move!!!\n");
						gui.promptActivePlayer();
					}
				}
				else {
					this.playerList.get(playIdx).removeCards(cards);
					this.handsOnTable.add(hand);
					gui.printMsg("{"+hand.getType()+"} ");
					gui.printMsg(printHand(hand)+"\n");
					nextPlayer();
				}
			}
			else {
				if (hand.contains(first_card)) {
					this.playerList.get(playIdx).removeCards(cards);
					this.handsOnTable.add(hand);
					gui.printMsg("{"+hand.getType()+"} ");
					gui.printMsg(printHand(hand)+"\n");
					nextPlayer();
				}
				else {
					gui.printMsg("Not a legal move!!!\n");
					gui.resetSelected();
					gui.promptActivePlayer();
				}
			}
		}
		else{
			gui.resetSelected();
			if (handsOnTable.size() != 0) {
				if (cardIdx == null) {
					if (handsOnTable.get(handsOnTable.size() - 1).getPlayer() != player) {
						gui.printMsg("{Pass}\n");
						nextPlayer();
					}
					else {
						gui.printMsg("Not a legal move!!!\n");
						gui.promptActivePlayer();
					}
				}
				else{
					gui.printMsg("Not a legal move!!!\n");
					gui.promptActivePlayer();
				}
			}
			else {
				if (cardIdx == null) {
					gui.printMsg("Not a legal move!!!\n");
					gui.promptActivePlayer();
				}
			}
		}
	}
	
	/**
	 * This method checks if it is the end of a game.
	 * @return A boolean variable, true if it is the end of the game, false otherwise.
	 */
	public boolean endOfGame() {
		for (int i = 0; i < getPlayerList().size(); i++) {
			if (this.playerList.get(i).getCardsInHand().size() == 0) {
				return true;
			}
		}
		return false;
	}
	
	/**
	 * This is the main method to start the program.
	 * @param args Not applicable for this program.
	 */
	public static void main(String[] args) {
		BigTwo game = new BigTwo();
	}
	
	private String printHand(Hand hand) {
		String handStr = "[";
		for (int i = 0; i < hand.size() - 1; i++) {
			handStr += hand.getCard(i).toString()+" ";
		}
		handStr += hand.getCard(hand.size() - 1).toString()+"]";
		return handStr;
	}
	
	private void nextPlayer() {
		if (endOfGame() == true) {
			gui.repaint();
			gui.printMsg("\nGame ends\n");
			String result = printResult();
			JOptionPane.showMessageDialog(null,result);
			CardGameMessage msg = new CardGameMessage(CardGameMessage.READY, -1, null);
			client.sendMessage(msg);
		}
		else {
			currentPlayerIdx = idxUpdate(currentPlayerIdx);
			gui.setActivePlayer(currentPlayerIdx);
			if (currentPlayerIdx == client.getPlayerID()) {
				gui.enable();
			}
			else {
				gui.disable();
			}
			gui.repaint();
			gui.promptActivePlayer();
		}
	}
	
	private int idxUpdate(int idx) {
		if (idx == 3) {
			return 0;
		}
		else {
			return idx + 1;
		}
	}
	
	private String printResult() {
		String printResult = "";
		for (int i = 0; i < 4; i++) {
			CardGamePlayer player=playerList.get(i);
			if (player.getNumOfCards() == 0) {
				printResult += player.getName()+" wins the game.";
			}
			else {
				printResult += player.getName()+" has "+player.getNumOfCards()+" cards in hand.";
			}
			printResult += "\n";
		}
		return printResult;
	}
	
	/**
	 * This method returns a valid hand from the specified list of cards of the player.
	 * @param player A CardGamePlayer variable specifying who tried to play these cards.
	 * @param cards A CardList variable containing the cards the player tried to play.
	 * @return A hand instance that is composed from the list of cards. It returns null if no valid hand can be composed.
	 */
	public static Hand composeHand(CardGamePlayer player, CardList cards) {
		if (cards == null) {
			return null;
		}
		//In case a hand is of multiple types simultaneously, the order matters
		if (cards.size() == 5) {
			StraightFlush straightflush = new StraightFlush(player,cards);
			if (straightflush.isValid()) {
				return straightflush;
			}
			Quad quad = new Quad(player,cards);
			if (quad.isValid()) {
				return quad;
			}
			FullHouse fullhouse = new FullHouse(player,cards);
			if (fullhouse.isValid()) {
				return fullhouse;
			}
			Flush flush = new Flush(player,cards);
			if (flush.isValid()) {
				return flush;
			}
			Straight straight = new Straight(player,cards);
			if (straight.isValid()) {
				return straight;
			}
		}
		else if (cards.size() == 3) {
			Triple triple = new Triple(player,cards);
			if (triple.isValid()) {
				return triple;
			}
		}
		else if (cards.size() == 2) {
			Pair pair = new Pair(player,cards);
			if (pair.isValid()) {
				return pair;
			}
		}
		else if (cards.size() == 1) {
			Single single = new Single(player,cards);
			if (single.isValid()) {
				return single;
			}
		}
		return null;
	}
}
