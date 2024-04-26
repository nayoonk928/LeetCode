class Solution {
    public int removeDuplicates(int[] nums) {
        int count = 1;
        int curr = nums[0];
        int idx = 1;
        
        for (int i = 1; i < nums.length; i++) {
            if (curr == nums[i] && count >= 2) {
                continue;
            }
            
            if (curr == nums[i]) {
                count++;
                nums[idx++] = nums[i];
            } else {
                count = 1;
                nums[idx++] = nums[i];
                curr = nums[i];
            }
        }
        
        return idx;
    }
}