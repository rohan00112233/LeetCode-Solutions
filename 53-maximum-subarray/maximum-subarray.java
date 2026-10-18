class Solution {
    public int maxSubArray(int[] nums) {
        int n = nums.length;
        int curr_sum =0;
        int max_sum = nums[0];
        for (int i =0;i<n;i++){
            curr_sum += nums[i];
            if(curr_sum>max_sum){
                max_sum = curr_sum;
            }
            if(curr_sum<0){
                curr_sum = 0;
            }
       
        }
        return max_sum;
        

    }
}