/**
 * This class provides a model for squares
 * @author Lou Huajie
 *
 */
public class Square extends Shape{
	
	/**
	 * This method sets the local coordinates of the 4 vertices of a 
	 * standard square.
	 * @param d half of the length of an edge
	 */
	public void setVertices(double d) {
		xLocal = new double[4];
		yLocal = new double[4];
		xLocal[0]=d;
		xLocal[1]=-d;
		xLocal[2]=-d;
		xLocal[3]=d;
		yLocal[0]=d;
		yLocal[1]=d;
		yLocal[2]=-d;
		yLocal[3]=-d;
	}
}
