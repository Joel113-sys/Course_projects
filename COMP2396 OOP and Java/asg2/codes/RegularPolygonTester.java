/**
 * This class tests if the RegularPolygon class is correctly implemented.
 * @author Lou Huajie
 *
 */
public class RegularPolygonTester {
	/**
	 * This method tests the correctness of the implementation on its call.
	 * @param args command-line arguments for the main function
	 */
	public static void main(String[] args) {
		
		boolean flag = true;
		
		//initialize the triangle using the constructor
		RegularPolygon poly = new RegularPolygon(3,10);
		
		System.out.println("the initial number of sides is:"+poly.getNumOfSides());
		if (poly.getNumOfSides()!=3) {
			flag = false;
		}
		
		System.out.println("the initial value of radius is:"+poly.getRadius());
		if (poly.getRadius()!=10) {
			flag = false;
		}
		
		//call the methods to reset the number of sides and the values of radius
		poly.setNumOfSides(4);
		poly.setRadius(20);
		
		//print the number of sides and radius after resetting the value
		System.out.println("the number of sides after resetting is:"+poly.getNumOfSides());
		if (poly.getNumOfSides()!=4) {
			flag = false;
		}
		
		System.out.println("the value of radius after resetting is:"+poly.getRadius());
		if (poly.getRadius()!=20) {
			flag = false;
		}
		
		//test if point(3,4)(in canvas coordinate system) is contained by the square
		if (poly.contains(3,4) == true) {
			System.out.println("Point (3,4) is contained in the polygon");
		}
		else {
			System.out.println("Point (3,4) is not contained in the polygon");
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
