class Solution {
    public int[] plusOne(int[] digits) {
        boolean flag = false;
        
        for (int i = digits.length - 1; i >= 0; i--) {
            if (digits[i] == 9) {
                digits[i] = 0;
                flag = true;
            } else {
                digits[i] += 1;
                flag = false;
                break;
            }
        }
        
        if (flag) {
            digits = new int[digits.length + 1];
            digits[0] = 1;
        }
        
        return digits;
    }
}