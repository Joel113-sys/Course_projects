/**
 * This class provides a model for regular n-sided polygons.
 * @author Lou Huajie
 */
public class RegularPolygon extends Shape {
	
	private int numOfSides;
	private double radius;
	
	/**
	 * A constructor for building a regular n-sided polygon with a radius of r.
	 * @param n the number of sides of the polygon
	 * @param r the radius of the polygon
	 */
	public RegularPolygon(int n, double r) {
		if (n<3) {
			numOfSides = 3;
		}
		else {
			numOfSides = n;
		}
		
		if (r<0){
			r = 0;
		}
		else{
			radius = r;
		}
		setVertices();
	}
	
	/**
	 * A constructor for building a regular n-sided polygon with a radius of 1.0
	 * @param n the number of sides of the polygon
	 */
	public RegularPolygon(int n) {
		if (n < 3) {
			numOfSides = 3;
		}
		else {
			numOfSides = n;
		}
		radius = 1.0;
		setVertices();
	}
	
	/**
	 * A constructor for building a regular 3-sided polygon with a radius of 1.0
	 */
	public RegularPolygon() {
		numOfSides = 3;
		radius = 1.0;
		setVertices();
	}
	
	/**
	 * This methods retrieves the number of sides of the polygon.
	 * @return number of sides of the polygon
	 */
	public int getNumOfSides() {
		return numOfSides;
	}
	
	/**
	 * This method retrieves the radius of the regular polygon
	 * @return the radius of the regular polygon
	 */
	public double getRadius() {
		return radius;
	}
	
	/**
	 * This method sets the number of sides of a regular n-sided polygon.
	 * @param n the number of sides of a polygon.
	 */
	public void setNumOfSides(int n) {
		if (n<3) {
			n = 3;
		}
		else {
			numOfSides = n;
		}
		setVertices();
	}
	
	/**
	 * This method sets the radius of the regular n-sided polygon.
	 * @param r the radius of the regular n-sided polygon.
	 */
	public void setRadius(double r) {
		if (r<0) {
			r = 0;
		}
		else {
			radius = r;
		}
		setVertices();
	}
	

	private void setVertices() {
		int n = getNumOfSides();
		double xcor[];
		xcor = new double[n];
		double ycor[];
		ycor = new double[n];
		double th = 2*Math.PI/n;
		
		if (n % 2 == 0) {
			for (int i = 0; i < n; i++) {
				xcor[i] = radius*Math.cos(Math.PI/n-i*th);
				ycor[i] = radius*Math.sin(Math.PI/n-i*th);
			}
		}
		else {
			for (int i = 0; i < n; i++) {
				xcor[i] = radius*Math.cos(-i*th);
				ycor[i] = radius*Math.sin(-i*th);
			}
		}
		setXLocal(xcor);
		setYLocal(ycor);
	}
	
	/**
	 * This method determines if a point(x,y) in the screen coordinate system is contained by the regular polygon.
	 * @param x the x-coordinate of the point in the screen coordinate system.
	 * @param y the y-coordinate of the point in the screen coordinate system.
	 * @return a boolean value indicating if the point is contained in the shape.
	 */
	public boolean contains(double x, double y) {

		int n = getNumOfSides();
		int c_minx;
		int c_miny;
		double l_min;
		if (n%2==0) {
			c_minx = getX()[n/2];
			c_miny = getY()[n/2];
		}
		else {
			c_minx = getX()[(n+1)/2];
			c_miny = getY()[(n+1)/2];
		}
		
		l_min = (c_minx-getXc())*Math.cos(-getTheta())-(c_miny-getYc())*Math.sin(-getTheta());
		
		double x_local = (x-getXc())*Math.cos(-getTheta())-(y-getYc())*Math.sin(-getTheta());
		double y_local = (x-getXc())*Math.sin(-getTheta())+(y-getYc())*Math.cos(-getTheta());
		
		double x_com = x_local;
		for (int i = 0; i < n; i++) {
			if (x_com<l_min) {
				return false;
			}
			x_com = x_local*Math.cos(i*2*Math.PI/n)-y_local*Math.sin(i*2*Math.PI/n);
		}
		return true;
	}
}
