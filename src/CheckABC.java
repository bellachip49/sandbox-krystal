class CheckABC {
    //field
    String alphabet = "abcdefghijklmnopqrstuvwxyz";

    //constructor
    CheckABC(){}

    //other methods
    boolean checkIfABC(char letter){
        boolean isLetter = false;
        for(int i = 0; i < alphabet.length(); i++){
            if (letter == alphabet.charAt(i)) {
                isLetter = true;
                break;
            }
        }
        return isLetter;
    }
}
