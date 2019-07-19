// https://leetcode.com/problems/sqrtx/submissions/
// Implement the function sqrt(x) to closest whole integer

class Solution {
    public int mySqrt(int x) {
        long left = 1;
        long right = x;
        long mid = 0;
        
        while(left+1<right){
            mid = left + (right - left)/2;
            if(mid*mid==x){
                return (int)mid;
            }else if(mid*mid>x){
                right = mid;
            }else{
                left = mid;
            }
        }
        
        return left*left < x ? (int)left: (int)right;
    }
}