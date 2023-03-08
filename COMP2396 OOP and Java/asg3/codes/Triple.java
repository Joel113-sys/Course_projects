/**
 * This class models a Triple hand.
 * @author joellau
 *
 */
public class Triple extends Hand{
	
	/**
	 * Construct a hand of Triple with specified player and cards.
	 * @param player A CardGamePlayer specifying who own this hand.
	 * @param cards A CardList containing the cards in this hand.
	 */
	public Triple(CardGamePlayer player,CardList cards) {
		super(player, cards);
	}
	
	/**
	 * This method return the type of this Triple.
	 * @return A String "Triple".
	 */
	public String getType() {
		return "Triple";
	}
	
	/**
	 * This method check whether this is a valid Triple hand.
	 * @return A boolean which is true if this is a valid Triple and is false otherwise.
	 */
	public boolean isValid(){
		if (this.size() != 3) {
			return false;
		}
		else {
			Card card0 = this.getCard(0);
			Card card1 = this.getCard(1);
			Card card2 = this.getCard(2);
			if ((card0.rank != card1.rank)||(card0.rank != card2.rank)||(card1.rank != card2.rank)) {
				return false;
			}else {
				return true;
			}
		}
	}
}
