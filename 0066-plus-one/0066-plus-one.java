class Solution {
    public int[] plusOne(int[] digits) {
        int index = digits.length - 1;
        int add = 1;
        
        while (index >= 0 && add > 0) {
            digits[index] = (digits[index] + add) % 10;
            add = (digits[index] == 0) ? 1 : 0;
            
            index--;
        }
        
        // add가 1이라면 주어진 수보다 한 자리수 더 큰 수가 됨
        if (add == 1) {
            digits = new int[digits.length + 1];
            digits[0] = 1;
        }
        
        return digits;
    }
}