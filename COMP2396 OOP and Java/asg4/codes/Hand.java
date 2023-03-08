/**
 * This method model a hand of cards played by the players, extended from CardList class.
 * @author joellau
 *
 */
public abstract class Hand extends CardList{
	
	private final CardGamePlayer player;
	
	/**
	 * This constructor construct a hand of specified player and cards.
	 * @param player A CardGamePlayer variable specifying who played this hand.
	 * @param cards A CardList variable containing the cards in this hand.
	 */
	public Hand(CardGamePlayer player, CardList cards) {
		this.player = player;
		for (int i = 0; i < cards.size(); i++) {
			this.addCard(cards.getCard(i));
		}
		this.sort();
	}
	
	/**
	 * The getter of player.
	 * @return A CardGamePlayer specifying the player who own this hand.
	 */
	public CardGamePlayer getPlayer() {
		return this.player;
	}
	
	/**
	 * This method returns the top card of this hand.
	 * @return A BigTwoCard which is the top card of this hand.
	 */
	public Card getTopCard() {
		if (!this.isEmpty()) {
			this.sort();
			return (this.getCard(this.size()-1));
		}else {
			return null;
		}
	}
	
	/**
	 * This method check whether this hand beats the specified hand.
	 * @param hand A Hand to be compared by this hand.
	 * @return A boolean which is true if this hand can beat the specified hand and is false otherwise.
	 */
	public boolean beats(Hand hand) {
		if (hand == null || !hand.isValid() ||!this.isValid() ||this.getType() != hand.getType()){
			return false;
		}
		else {
			return (this.getTopCard().compareTo(hand.getTopCard())>0);
		}
	}
	
	/**
	 * This method return whether this is a valid hand. 
	 * @return A String specifying the type of this hand.
	 */
	public abstract boolean isValid();
	
	/**
	 * This method return the type of this hand.
	 * @return A String specifying the type of this hand.
	 */
	public abstract String getType();
}
