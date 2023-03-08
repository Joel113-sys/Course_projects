/**
 * This class provides a model for triangles.
 * @author Lou Huajie
 *
 */
public class Triangle extends Shape{
	
	/**
	 * This method sets the local coordinates of the 3 vertices of a 
	 * standard triangle.
	 * @param d the distance from the center of the triangle to any of its vertices.
	 */
	public void setVertices(double d) {
		xLocal = new double[3];
		yLocal = new double[3];
		xLocal[0]=d;
		xLocal[1]=-d*Math.cos(Math.PI/3);
		xLocal[2]=-d*Math.cos(Math.PI/3);
		yLocal[0]=0;
		yLocal[1]=d*Math.sin(Math.PI/3);
		yLocal[2]=-d*Math.sin(Math.PI/3);
	}
}