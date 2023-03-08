/**
 * This class models a Straight hand.
 * @author joellau
 *
 */
public class Straight extends Hand{
	
	/**
	 * Construct a hand of Straight with specified player and cards.
	 * @param player A CardGamePlayer specifying who own this hand.
	 * @param cards A CardList containing the cards in this hand.
	 */
	public Straight(CardGamePlayer player,CardList cards) {
		super(player, cards);
	}
	
	/**
	 * This method return the type of this Straight.
	 * @return A String "Straight".
	 */
	public String getType() {
		return "Straight";
	}
	
	/**
	 * This method check whether this hand beats the specified hand (for the Straight class exclusively).
	 * @param hand A Hand to be compared by this hand.
	 * @return A boolean which is true if this hand can beat the specified hand and is false otherwise.
	 */
	@Override public boolean beats(Hand hand) {
		if(hand.getType()==this.getType()) {
			if(this.getTopCard().compareTo(hand.getTopCard())>0){
				return true;
			}
			else {
				return false;
			}
		}
		else {
			return false;
		}
	}
	
	/**
	 * This method check whether this is a valid Straight hand.
	 * @return A boolean which is true if this is a valid Straight and is false otherwise.
	 */
	public boolean isValid() {
		if (this.size() == 5) {
			for(int i=0;i<4;i++) {
				if(this.getCard(i+1).rank!=nextRank(this.getCard(i).rank)) {
					return false;
				}
			}
			return true;
		}
		return false;
	}
	
	private int nextRank(int i) {
		if(i==12) {
			return 0;
		}
		if(i==1) {
			return -1;
		}
		return i+1;
	}

}
