// Compare two version numbers version1 and version2.
// If version1 > version2 return 1; if version1 < version2 return -1;otherwise return 0.
// https://leetcode.com/problems/compare-version-numbers/

class Solution {
    public int compareVersion(String version1, String version2) {
        int i = 0, j =0;
        String tmp1 = "0", tmp2 = "0";
        while(i<version1.length() || j< version2.length()){
            while(i<version1.length() && version1.charAt(i) != '.'){
                tmp1 += version1.charAt(i);
                i++;
            }
            
            while(j<version2.length() && version2.charAt(j) != '.'){
                tmp2 += version2.charAt(j);
                j++;
            }
            
            if(Integer.parseInt(tmp1) > Integer.parseInt(tmp2)) return 1;
            else if(Integer.parseInt(tmp1) < Integer.parseInt(tmp2)) return -1;
            else{
                tmp1 = "0";
                tmp2 = "0";
                i++;
                j++;
            }
        }
        return 0;
    }
}