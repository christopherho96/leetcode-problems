// https://leetcode.com/problems/add-binary/submissions/
// Given two binary strings, return their sum (also a binary string).
class Solution {
    public String addBinary(String a, String b) {
        int s1 = a.length()-1, s2 = b.length()-1;
        int aDigit, bDigit; 
        int carry = 0;
        String answer = "";
        
        while(s1 > -1 || s2 > -1 || carry ==1){
            
            aDigit = getBinaryDigit(a, s1);
            bDigit = getBinaryDigit(b, s2);
            
            int sum = aDigit + bDigit + carry;
            carry = sum > 1 ? 1: 0;
            int nextDigit = sum % 2;
            
            answer = Integer.toString(nextDigit) + answer; 
            
            s1--;
            s2--;
        }
        
        return answer;
    }
    
    private int getBinaryDigit(String binaryString, int index) {
        return index>-1 ? Character.getNumericValue(binaryString.charAt(index)) : 0;
    }
}