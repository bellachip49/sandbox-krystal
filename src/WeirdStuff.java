import java.util.Scanner; //to ask user for input
import java.lang.Character; //to compare characters

public class WeirdStuff {
    public static void main(String [] args){
        CheckABC isLetter = new CheckABC();
        Scanner msg = new Scanner(System.in);

        StringBuilder outputVal = new StringBuilder();
        boolean onCaps = true;

        System.out.println("Type something.");
        String answer = msg.nextLine();
        for(int i = 0; i < answer.length(); i++){
            if(isLetter.checkIfABC(answer.charAt(i))){
                if(onCaps){
                    outputVal.append(Character.toLowerCase(answer.charAt(i)));
                    onCaps = false; //switch to alt
                }else {
                    outputVal.append(Character.toUpperCase(answer.charAt(i)));
                    onCaps = true; //switch to alt
                }
            }else {
                outputVal.append(answer.charAt(i));
            }
        }
        //loop ends, output's construction finished; now prints out result
        System.out.println(outputVal);
    }
}
