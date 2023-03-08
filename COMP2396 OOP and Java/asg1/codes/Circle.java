/**
 * This class provides a model for circles
 * @author Lou Huajie
 */
public class Circle extends Shape {
	
	/**
	 * This method sets the local coordinates of the upper left and 
	 * lower left vertices of an axis-aligned bounding box of a standard circle.
	 * @param d the radius of the circle
	 */
	public void setVertices(double d) {
		 xLocal = new double[2];
		 yLocal = new double[2];
		 xLocal[1]=d;
		 yLocal[1]=d;
		 xLocal[0]=-d;
		 yLocal[0]=-d;
	}
	
	/**
	 * This method retrieves the x-coordinates of the upper left and lower right
	 * vertices of an axis-aligned bounding box of a standard circle.
	 * @return an array of x-coordinates on the canvas coordination
	 */
	public int[] getX() {
		int xcor[];
		xcor = new int[2];
		for (int i=0;i<2;i++)
		{
			xcor[i]=(int) Math.round(xLocal[i]+xc);
		}
		return xcor;
	}
	
	/**
	 * This method retrieves the y-coordinates of the upper left and lower right
	 * vertices of an axis-aligned bounding box of a standard circle.
	 * @return an array of y-coordinates on the canvas coordination
	 */
	public int[] getY(){
		int ycor[];
		ycor = new int[2];
		for (int i=0;i<2;i++)
		{
			ycor[i]=(int) Math.round(yLocal[i]+yc);
		}
		return ycor;
	}
}
