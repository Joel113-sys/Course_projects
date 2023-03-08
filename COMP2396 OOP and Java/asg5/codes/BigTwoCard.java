/**
 * This class is model a card used in Big Two card game, extended from Card class.
 * @author joellau
 *
 */
public class BigTwoCard extends Card{
	/**
	 * This constructor constructs a card of the specified suit and rank.
	 * @param suit An integer from 0 to 3 specifying the suit of this card. 0,1,2,3 representing Diamond, Club, Heart, Spade respectively.
	 * @param rank An integer from 0 to 12 specifying the suit of this card. 0-12 representing A-K respectively.
	 */
	public BigTwoCard(int suit, int rank) {
		super(suit, rank);
	}
	
	/**
	 * This method compares this card with the specified card. It overrides the method in the Card class.
	 * @return Return an integer. If this card is larger, return 1. If the specified card is larger, return -1. return 0 otherwise.
	 */
	@Override public int compareTo(Card card) {
		if ((this.rank <= 1) && (card.rank > 1)){
			return 1;
		}
		else if ((this.rank > 1) && (card.rank <= 1)){
			return -1;
		}
		else if ((this.rank > 1)&&(card.rank > 1)) {
			if (this.rank > card.rank) {
				return 1;
			}
			else if (this.rank < card.rank) {
				return -1;
			}
			else if (this.suit > card.suit){
				return 1;
			}
			else if (this.suit < card.suit) {
				return -1;
			}
			else {
				return 0;
			}
		}
		else {
			if (this.rank > card.rank) {
				return 1;
			}
			else if (this.rank < card.rank) {
				return -1;
			}
			else if (this.suit > card.suit) {
				return 1;
			}
			else if (this.suit < card.suit) {
				return -1;
			}
			else {
				return 0;
			}
		}

	}
}
