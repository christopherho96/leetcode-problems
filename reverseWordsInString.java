// https://leetcode.com/problems/reverse-words-in-a-string/
// Given an input string, reverse the string word by word.

public class Solution {
    public String reverseWords(String s) {
        
//         Regex solution
//         \\s+ stands for split all words by removing all white space
        
//         String [] words = s.split("\\s+");
//         String reverse = "";
        
//         for(int i = words.length - 1; i>-1; i--){
//             reverse += words[i];
//             if(i != 0){
//                 reverse += words[i-1].length() > 0 ? " ": "";
//             }
//         }
//         return reverse;
        
//         Using built in java functions, can do in 3 lines
//         String[] words = s.trim().split(" +");
//         Collections.reverse(Arrays.asList(words));
//         return String.join(" ", words);
        
        // O(n) solution, loop through entire string once
        String reverse = "";
        int length = s.length();
        int start = -1;
        for(int i=0; i<length; i++){
            char letter = s.charAt(i);
            if(letter != ' ' && start == -1 ) start = i; 
            else if(letter == ' ' && start != -1){
                if(reverse.length() > 0) reverse = " " + reverse;
                reverse = s.substring(start,i) + reverse;
                start = -1;
            }
        }
        if(start != -1){
            if(reverse.length() > 0) reverse = " " + reverse;
            reverse = s.substring(start, length) + reverse;
        }
        return reverse;
    }
}