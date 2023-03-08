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
	private Color color;
	
	/**
	 * A boolean variable that specifies if the shape is filled.
	 */
	private boolean filled;
	
	/**
	 * a double variable that specifies the orientation of the center
	 */
	private double theta;
	
	/**
	 * a double value specifying x-coordinate of the center in canvas coordinate system.
	 */
	private double xc;
	
	/**
	 * a double value specifying y-coordinate of the center in canvas coordinate system.
	 */
	private double yc;
	
	/**
	 * An array of double values specifying the x-coordinates of the vertices in the local coordinate system.
	 */
	private double[] xLocal;
	
	/**
	 *  An array of double values specifying the x-coordinates of the vertices in the local coordinate system.
	 */
	private double[] yLocal;
	
	
	/**
	 * This methods retrieves the color of the shape
	 * @return color of the shape
	 */
	public Color getColor() {
		return color;
	}
	
	/**
	 * This methods retrieves the fill-type of the shape
	 * @return the fill-type of the shape
	 */
	public boolean getFilled() {
		if (filled == true) {
			return true;
		}
		else {
			return false;
		}
	}
	
	/**
	 * this method retrieves the orientation (in radians) of the shape in canvas coordinate system
	 * @return the orientation (in radians) of the shape in the canvas coordinate system
	 */
	public double getTheta() {
		return theta;
	}
	
	/**
	 * this method retrieves the x-coordinate of the center of the shape in the canvas coordinate system.
	 * @return the x-coordinate of the center of the shape in the canvas coordinate system.
	 */
	public double getXc() {
		return xc;
	}
	
	/**
	 * this method retrieves the y-coordinate of the center of the shape in the canvas coordinate system.
	 * @return the y-coordinate of the center of the shape in the canvas coordinate system.
	 */
	public double getYc() {
		return yc;
	}
	
	/**
	 * This method retrieves the x-coordinates of the vertices of the shape in local coordinate system
	 * @return the x-coordinates of the vertices of the shape in local coordinate system
	 */
	public double[] getXLocal() {
		return xLocal;
	}
	
	/**
	 * This method retrieves the y-coordinates of the vertices of the shape in local coordinate system
	 * @return the y-coordinates of the vertices of the shape in local coordinate system
	 */
	public double[] getYLocal() {
		return yLocal;
	}
	
	/**
	 * This method sets the color of the shape.
	 * @param color the color to set for the shape
	 */
	public void setColor(Color color) {
		this.color = color;
	}
	
	/**
	 * This method sets the fill-type of the shape.
	 * @param filled the fill-type of the shape
	 */
	public void setFilled(boolean filled) {
		this.filled = filled;
	}
	
	/**
	 * This method sets the orientation of the shape.
	 * @param theta the orientation of the shape.
	 */
	public void setTheta(double theta) {
		this.theta = theta;
	}
	
	/**
	 * This method sets the x-coordinate of the center of the shape in the canvas coordinate system.
	 * @param xc the x-coordinate of the center of the shape in the canvas coordinate system.
	 */
	public void setXc(double xc) {
		this.xc = xc;
	}
	
	/**
	 * This method sets the y-coordinate of the center of the shape in the canvas coordinate system.
	 * @param xc the y-coordinate of the center of the shape in the canvas coordinate system.
	 */
	public void setYc(double yc) {
		this.yc = yc;
	}
	
	/**
	 * This method sets the x-coordinates of the vertices of the shape in its local coordinate system.
	 * @param xLocal the x-coordinates of the vertices of the shape in its local coordinate system.
	 */
	public void setXLocal(double[] xLocal) {
		int lstlen = xLocal.length;
		this.xLocal = new double[lstlen];
		for (int i = 0; i < lstlen;i++) {
			this.xLocal[i] = xLocal[i];
		}
	}
	
	/**
	 * This method sets the y-coordinates of the vertices of the shape in its local coordinate system.
	 * @param xLocal the y-coordinates of the vertices of the shape in its local coordinate system.
	 */
	public void setYLocal(double[] yLocal) {
		int lstlen = yLocal.length;
		this.yLocal = new double[lstlen];
		for (int i = 0; i < lstlen;i++) {
			this.yLocal[i] = yLocal[i];
		}
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

