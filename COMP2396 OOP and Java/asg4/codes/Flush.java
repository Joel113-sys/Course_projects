/**
 * This class model a Flush hand.
 * @author joellau
 *
 */
public class Flush extends Hand{
	
	/**
	 * Construct a hand of Flush with specified player and cards.
	 * @param player A CardGamePlayer specifying who own this hand.
	 * @param cards A CardList containing the cards in this hand.
	 */
	public Flush(CardGamePlayer player,CardList cards) {
		super(player, cards);
	}
	
	/**
	 * This method check whether this hand beats the specified hand (for the Flush class exclusively).
	 * @param hand A Hand to be compared by this hand.
	 * @return A boolean which is true if this hand can beat the specified hand and is false otherwise.
	 */
	public boolean beats(Hand hand) {
		if(hand.getType()==this.getType()) {
			if(this.getTopCard().compareTo(hand.getTopCard())>0){
				return true;
			}
			else {
				return false;
			}
		}
		else {
			if (this.size() == hand.size()) {
				if(hand.getType()=="Straight") {
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
	 * This method return the type of this Flush.
	 * @return A String "Flush".
	 */
	public String getType() {
		return "Flush";
	}
	
	/**
	 * This method check whether this is a valid Flush hand.
	 * @return A boolean which is true if this is a valid Flush and is false otherwise.
	 */
	public boolean isValid() {
		if (this.size()!=5) {
			return false;
		}
		else {
			BigTwoCard card0 = (BigTwoCard) this.getCard(0);
			BigTwoCard card1 = (BigTwoCard) this.getCard(1);
			BigTwoCard card2 = (BigTwoCard) this.getCard(2);
			BigTwoCard card3 = (BigTwoCard) this.getCard(3);
			BigTwoCard card4 = (BigTwoCard) this.getCard(4);
			if ((card0.suit == card1.suit)&&(card0.suit == card2.suit)&&(card0.suit == card3.suit)&&(card0.suit==card4.suit)){
				return true;
			}
			else {
				return false;
			}
		}
	}
}
