        // freq = {}
        // for i in range(len(nums)):
        //     if nums[i] in freq:
        //         return nums[i]

        //     else:
        //         freq[nums[i]] = 1


class Solution {
    public int findDuplicate(int[] nums) {
        
        HashMap<Integer, Integer> freq = new HashMap<>();
        for(int i =0;i<nums.length;i++){
            if(freq.containsKey(nums[i])){
                return nums[i];
            }
            else{
                freq.put(nums[i], 1);
            }
        }
        return -1;
    }
}