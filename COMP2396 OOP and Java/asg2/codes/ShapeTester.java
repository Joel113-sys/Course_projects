import java.awt.Color;

/**
 * This class tests if the Shape class is correctly implemented.
 * @author Lou Huajie
 *
 */
public class ShapeTester {
	
	/**
	 * This method tests the correctness of the implementation on its call.
	 * @param args command-line arguments for the main function
	 */
	public static void main(String[] args) {
		
		boolean flag = true;
		
		//create a new object
		Shape s1 = new Shape();
		
		//set the instant variables
		s1.setFilled(true);
		s1.setTheta(1.0);
		s1.setColor(Color.black);
		s1.setXc(1);
		s1.setYc(1);
		
		double[] x_cor = {1,2,3,4};
		double[] y_cor = {1,2,3,4};
		s1.setXLocal(x_cor);
		s1.setYLocal(y_cor);
		
		//print the values of instant variables before any methods are called.
		System.out.println("xc (before translation) is:"+s1.getXc());
		System.out.println("yc (before translation) is:"+s1.getYc());
		System.out.println("theta (before rotation) is:"+s1.getTheta());
		System.out.println("color is:"+s1.getColor());
		
		//call the methods
		System.out.println("x-coordinates in the local coordinate system:");
		for (int i = 0; i <s1.getXLocal().length;i++) {
			double a = s1.getXLocal()[i];
			System.out.println(a);
		}
		
		System.out.println("y-coordinates in the local coordinate system:");
		for (int i = 0; i <s1.getYLocal().length;i++) {
			double b = s1.getYLocal()[i];
			System.out.println(b);
		}
		
		System.out.println("x-coordinates in the canvas coordinate system:");
		for (int i = 0; i <s1.getX().length;i++) {
			int c = s1.getX()[i];
			System.out.println(c);
		}
		
		System.out.println("y-coordinates in the canvas coordinate system:");
		for (int i = 0; i <s1.getY().length;i++) {
			int d = s1.getY()[i];
			System.out.println(d);
		}
		
		s1.rotate(1);
		s1.translate(1, 1);
		
		//print the values of instant variables after methods are called.
		System.out.println("is filled:"+s1.getFilled());
		if (s1.getFilled() == false) {
			flag = false;
		}
		System.out.println("theta (after rotation) is:"+s1.getTheta());
		if (s1.getTheta() != 2.0) {
			flag = false;
		}
		System.out.println("xc (after translation) is:"+s1.getXc());
		if (s1.getXc() != 2.0) {
			flag = false;
		}
		System.out.println("yc (after translation) is:"+s1.getYc());
		if (s1.getYc() != 2.0) {
			flag = false;
		}
		if (flag == false) {
			System.out.println("something went wrong(");
		}
		else {
			System.out.println("No bugs in the program:)");
		}
	}
}