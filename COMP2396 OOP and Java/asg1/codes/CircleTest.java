import java.awt.Color;

/**
 * This class tests if the Circle class is correctly implemented.
 * @author Lou Huajie
 *
 */
public class CircleTest {
	
	/**
	 * This method tests the correctness of the implementation on its call.
	 * @param args command-line arguments for the main function
	 */
	public static void main(String[] args) {
		//create a new object
		Shape s1 = new Circle();
		
		//set the instant variables
		s1.filled=true;
		s1.theta=1;
		s1.color=Color.green;
		s1.xc=1;
		s1.yc=1;
		s1.xLocal=new double[2];
		s1.yLocal=new double[2];
		
		//print the values of instant variables before any methods are called.
		System.out.println("xc (before translation) is:"+s1.xc);
		System.out.println("yc (before translation) is:"+s1.yc);
		System.out.println("theta (before rotation) is:"+s1.theta);
		System.out.println("color is:"+s1.color);
		
		//call the methods
		s1.setVertices(2);
		s1.getX();
		s1.getY();
		s1.rotate(1);
		s1.translate(1, 1);
		
		//print the values of instant variables after methods are called.
		System.out.println("The upper left vertice is:"+s1.xLocal[0]+" ,"+s1.yLocal[0]);
		System.out.println("The lower right vertice is:"+s1.xLocal[1]+" ,"+s1.yLocal[1]);
		System.out.println("is filled:"+s1.filled);
		System.out.println("theta (after rotation) is:"+s1.theta);
		System.out.println("xc (after translation) is:"+s1.xc);
		System.out.println("yc (after translation) is:"+s1.yc);
	}
}
