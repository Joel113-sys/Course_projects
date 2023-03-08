/**
 * This class models a single hand.
 * @author joellau
 *
 */
public class Single extends Hand{
	
	/**
	 * Construct a hand of Single with specified player and cards.
	 * @param player A CardGamePlayer specifying who own this hand.
	 * @param cards A CardList containing the cards in this hand.
	 */
	public Single(CardGamePlayer player,CardList cards) {
		super(player, cards);
	}
	
	/**
	 * This method return the type of this Single.
	 * @return A String "Single".
	 */
	public String getType() {
		return "Single";
	}
	
	/**
	 * This method check whether this is a valid Single hand.
	 * @return A boolean which is true if this is a valid Single and is false otherwise.
	 */
	public boolean isValid() {
		if (this.size() == 1) {
			return true;
		}else {
			return false;
		}
	}
}
