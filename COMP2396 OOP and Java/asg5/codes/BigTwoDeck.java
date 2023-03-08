/**
 * This class models the deck used in the BigTwoCard game.
 * @author joellau
 *
 */
public class BigTwoDeck extends Deck{
	/**
	 * This method initializes the deck containing 52 BigTwoCards.
	 */
	@Override public void initialize() {
		removeAllCards();
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 13; j++) {
				BigTwoCard card = new BigTwoCard(i, j);
				addCard(card);
			}
		}
	}
}
