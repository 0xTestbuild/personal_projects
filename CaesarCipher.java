
public class CaesarCipher {
	
		/* This program is designed to encode a string 
		 * using the CaesarCipher method and print it to the console
		 * 
		 */

	public static void main(String []args){ 
	
			// check to see if valid input 	
			if ( !(args[0] instanceof String) ){
				System.out.println("The first argument must be a string!");
				System.exit(0);
				
			} else if ( Integer.parseInt(args[1]) != Integer.parseInt(args[1])){
				System.out.println("The second argument must be an integer!");
				System.exit(0);
			} else if ( Integer.parseInt(args[1]) <= 0 ){
				System.out.println("You must specific an integer greater than Zero!");

			} 
			
			String stringArg = args[0];
			int intArg = Integer.parseInt(args[1]);
			
			
			char [] charArray = stringArg.toCharArray();
			
			
			char [] encoded = new char [stringArg.length()];  
			int encodedIndex = 0;
			
			for ( char character : charArray){
				
				int tracker = (int) character;
				
				if ((tracker + intArg >= 97 && tracker+ intArg <= 122) 
						|| (tracker+ intArg >= 65 && tracker+ intArg <= 90) ){
					
					encoded[encodedIndex] = (char) (tracker + intArg);
					encodedIndex++;
					
				} else if ( character == ' ') {
					encoded[encodedIndex] = ' ';
					encodedIndex++;
					
				} else {
					System.out.println("Your arguments landed out of bounds!");
					System.exit(0);
				}				
			}
			
			String encodedString = "";
			
			for (char character : encoded){
				encodedString += Character.toString(character); 
			}
		
			System.out.println("Original input: " + stringArg);
			System.out.println("Caesar Cipher text: " + encodedString);
	}
	
	

}
