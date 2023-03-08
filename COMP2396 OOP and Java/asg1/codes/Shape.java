import java.awt.Color;
import java.lang.Math;

/**
 * This class provides instance variables and methods for shapes, 
 * and it serves as the superclass for the other three subclasses.
 * @author Lou Huajie
 */
public class Shape {
	
	/**
	 * A variable that specifies the color of the shape
	 */
	Color color;
	
	/**
	 * A boolean variable that specifies if the shape is filled.
	 */
	boolean filled;
	
	/**
	 * a double variable that specifies the orientation of the center
	 */
	double theta;
	
	/**
	 * a double value specifying x-coordinate of the center
	 */
	double xc;
	
	/**
	 * a double value specifying y-coordinate of the center
	 */
	double yc;
	
	/**
	 * An array of double values specifying the x-coordinates of the vertices.
	 */
	double[] xLocal;
	
	/**
	 *  An array of double values specifying the x-coordinates of the vertices.
	 */
	double[] yLocal;
	
	/**
	 * This is dummy method for setting the local coordinates of the
	 * vertices of a shape. It is supposed to be overridden in the subclasses.
	 * @param d a unit length for the vertices
	 */
	public void setVertices(double d) {
		
	}
	
	/**
	 * This method translate the center of the shape by dx and dy
	 * @param dx distance along the x-axis
	 * @param dy distance along the y-axis
	 */
	public void translate(double dx, double dy) {
		xc = xc + dx;
		yc = yc + dy;
	}
	
	/**
	 * This method rotates the shape about its center by an angle of dt
	 * @param dt an angle to rotate
	 */
	public void rotate(double dt) {
		theta = theta + dt;
	}
	
	/**
	 * This method retrieves the x-coordinate of the vertices
	 * @return an array of x-coordinates on the canvas coordination
	 */
	public int[] getX() {
		int xcor[];
		xcor = new int[xLocal.length];
		for (int i=0;i<xLocal.length;i++)
		{
			xcor[i]=(int) Math.round(xLocal[i]*Math.cos(theta)-yLocal[i]*Math.sin(theta)+xc);
		}
		return xcor;
	}
	
	/**
	 * This method retrieves the y-coordinate of the vertices
	 * @return an array of y-coordinates on the canvas coordination
	 */
	public int[] getY(){
		int ycor[];
		ycor = new int[yLocal.length];
		for (int i=0;i<yLocal.length;i++)
		{
			ycor[i]=(int) Math.round(xLocal[i]*Math.sin(theta)+yLocal[i]*Math.cos(theta)+yc);
		}
		return ycor;
	}
}





