/**
 * This class model a Pair hand.
 * @author joellau
 *
 */
public class Pair extends Hand{
	
	/**
	 * Construct a hand of Pair with specified player and cards.
	 * @param player A CardGamePlayer specifying who own this hand.
	 * @param cards A CardList containing the cards in this hand.
	 */
	public Pair(CardGamePlayer player,CardList cards) {
		super(player, cards);
	}
	
	/**
	 * This method return the type of this Pair.
	 * @return A String "Pair".
	 */
	public String getType() {
		return "Pair";
	}
	
	/**
	 * This methods checks whether this is a valid pair hand or not.
	 * @return A boolean which is true if this is a valid Pair and is false otherwise.
	 */
	public boolean isValid(){
		if (this.size() != 2) {
			return false;
		}
		else {
			BigTwoCard card0 = (BigTwoCard) this.getCard(0);
			BigTwoCard card1 = (BigTwoCard) this.getCard(1);
			if (card0.rank != card1.rank) {
				return false;
			}else {
				return true;
			}
		}
	}
}
