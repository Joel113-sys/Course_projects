/**
 * This class model a FullHouse hand.
 * @author joellau
 *
 */
public class FullHouse extends Hand{
	
	/**
	 * Construct a hand of FullHouse with specified player and cards.
	 * @param player A CardGamePlayer specifying who own this hand.
	 * @param cards A CardList containing the cards in this hand.
	 */
	public FullHouse(CardGamePlayer player,CardList cards) {
		super(player, cards);
	}
	
	/**
	 * This method return the type of this FullHouse.
	 * @return A String "FullHouse".
	 */
	public String getType() {
		return "FullHouse";
	}
	
	/**
	 * This method return the top card of this hand.
	 * @return A BigTwoCard which is the top card of this hand.
	 */
	@Override public Card getTopCard() {
		if (!this.isEmpty()) {
			this.sort();
			return (this.getCard(2));
		}else {
			return null;
		}
	}
	
	/**
	 * This method check whether this hand beats the specified hand (for the FullHouse class exclusively).
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
			if (this.size() == hand.size()){
				if(hand.getType()=="Flush"||hand.getType()=="Straight") {
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
	}
	
	/**
	 * This method check whether this is a valid FullHouse hand.
	 * @return A boolean which is true if this is a valid FullHouse and is false otherwise.
	 */
	public boolean isValid() {
		if (this.size() != 5) {
			return false;
		}
		else {
			BigTwoCard card0 = (BigTwoCard) this.getCard(0);
			BigTwoCard card1 = (BigTwoCard) this.getCard(1);
			BigTwoCard card2 = (BigTwoCard) this.getCard(2);
			BigTwoCard card3 = (BigTwoCard) this.getCard(3);
			BigTwoCard card4 = (BigTwoCard) this.getCard(4);
			if (((card0.rank==card1.rank)&&(card1.rank==card2.rank)&&(card3.rank==card4.rank))||((card2.rank==card3.rank)&&(card3.rank==card4.rank)&&(card0.rank==card1.rank))) {
				return true;
			}
			else {
				return false;
			}
		}
	}

}
