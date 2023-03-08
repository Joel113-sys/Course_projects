import java.util.ArrayList;

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
	private BigTwoGUI ui;
	
	/**
	 * This is the default constructor of the class.
	 */
	public BigTwo() {
		CardGamePlayer player0 = new CardGamePlayer();
		CardGamePlayer player1 = new CardGamePlayer();
		CardGamePlayer player2 = new CardGamePlayer();
		CardGamePlayer player3 = new CardGamePlayer();
		this.playerList.add(player0);
		this.playerList.add(player1);
		this.playerList.add(player2);
		this.playerList.add(player3);
		this.ui = new BigTwoGUI(this);
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
	 * This method  starts the game.
	 * @param The deck used in the BigTwo card game.
	 */
	public void start(Deck deck) {
		for (int i = 0; i < 4; i++) {
			this.playerList.get(i).removeAllCards();
		}
		handsOnTable.clear();
		deck.initialize();
		deck.shuffle();
		for (int i = 0; i < 52; i=i+4) {
			BigTwoCard card = (BigTwoCard) deck.removeCard(0);
			this.playerList.get(0).addCard(card);
			card = (BigTwoCard) deck.removeCard(0);
			this.playerList.get(1).addCard(card);
			card = (BigTwoCard) deck.removeCard(0);
			this.playerList.get(2).addCard(card);
			card = (BigTwoCard) deck.removeCard(0);
			this.playerList.get(3).addCard(card);
		}
		for (int i = 0; i < 4; i++) {
			this.playerList.get(i).sortCardsInHand();
		}
		BigTwoCard card = new BigTwoCard(0,2);
		for (int i = 0; i < 4; i++) {
			if (this.playerList.get(i).getCardsInHand().contains(card)) {
				currentPlayerIdx = i;
				this.ui.setActivePlayer(i);
			}
		}
		this.ui.repaint();
		//this.//ui.promptActivePlayer();
	}
	
	/**
	 * This method makes a move by a player with the specified index using the cards specified by a list of indexes.
	 * @param playerIdx An integer specifying the index of the current player.
	 * @param cardIdx An array of integer containing the indexes of the cards selected by the player.
	 */
	public void makeMove(int playIdx, int[] cardIdx) {
		this.checkMove(playIdx, cardIdx);
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
						ui.printMsg("{"+hand.getType()+"} ");
						
						if (endOfGame()==false) {
							if (playIdx == 3) {
								ui.setActivePlayer(0);
							}
							else {
								ui.setActivePlayer(playIdx+1);
							}
							ui.repaint();
							//ui.promptActivePlayer();
						}
						else {
							//ui.setActivePlayer(-1);
							ui.repaint();
							
							
						}
					}
					else {
						ui.printMsg("Not a legal move!!!\n");
						//ui.promptActivePlayer();
					}
				}
				else {
					this.playerList.get(playIdx).removeCards(cards);
					this.handsOnTable.add(hand);
					if (endOfGame()==false) {
						if (playIdx == 3) {
							ui.setActivePlayer(0);
						}
						else {
							ui.setActivePlayer(playIdx+1);
							}
						ui.repaint();
						//ui.promptActivePlayer();
					}
					else {
						//ui.setActivePlayer(-1);
						ui.repaint();
						
					}
				}
			}
			else {
				if (hand.contains(first_card)) {
					this.playerList.get(playIdx).removeCards(cards);
					this.handsOnTable.add(hand);
					ui.printMsg("{"+hand.getType()+"} ");
					if (playIdx == 3) {
						ui.setActivePlayer(0);
					}
					else {
						ui.setActivePlayer(playIdx+1);
					}
					ui.repaint();
					//ui.promptActivePlayer();
				}
				else {
					ui.printMsg("Not a legal move!!!\n");
					ui.repaint();
					//ui.promptActivePlayer();
				}
			}
		}
		else{
			ui.resetSelected();
			if (handsOnTable.size() != 0) {
				if (cardIdx == null) {
					if (handsOnTable.get(handsOnTable.size() - 1).getPlayer() != player) {
						//ui.printMsg("{Pass}");
						//ui.printMsg("");
						if (playIdx == 3) {
							ui.setActivePlayer(0);
						}
						else {
							ui.setActivePlayer(playIdx+1);
							}
						ui.repaint();
						//ui.promptActivePlayer();
					}
					else {
						ui.printMsg("Not a legal move!!!\n");
						//ui.promptActivePlayer();
					}
				}
				else{
					ui.printMsg("Not a legal move!!!\n");
					//ui.promptActivePlayer();
				}
			}
			else {
				if (cardIdx == null) {
					ui.printMsg("Not a legal move!!!\n");
					//ui.promptActivePlayer();
				}
			}
		}
	}
	
	/**
	 * This method checks if it is the end of a game.
	 * @return A boolean variable, true if it is the end of the game, false otherwise.
	 */
	public boolean endOfGame() {
		for (int i = 0; i < 4; i ++) {
			if (this.playerList.get(i).getNumOfCards() == 0) {
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
		BigTwoDeck deck = new BigTwoDeck();
		deck.shuffle();
		game.start(deck);
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
		
		if (cards.size() == 5) {
			StraightFlush straightflush = new StraightFlush(player,cards);
			if (straightflush.isValid()) {
				return straightflush;
			}
			Flush flush = new Flush(player,cards);
			if (flush.isValid()) {
				return flush;
			}
			FullHouse fullhouse = new FullHouse(player,cards);
			if (fullhouse.isValid()) {
				return fullhouse;
			}
			Straight straight = new Straight(player,cards);
			if (straight.isValid()) {
				return straight;
			}
			Quad quad = new Quad(player,cards);
			if (quad.isValid()) {
				return quad;
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
