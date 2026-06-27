class Solution {
    public int[] twoSum(int[] nums, int target) {
        int n  = nums.length;
        HashMap<Integer,Integer> dict = new HashMap<>();

        for(int i =0; i<n; i++){
            int rem = target - nums[i];
            if(dict.containsKey(rem)){
                return new int[]{dict.get(rem),i};

            }
            dict.put(nums[i],i);
        }
        return new int[]{};
    }
}