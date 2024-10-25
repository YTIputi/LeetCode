import java.util.HashMap;
import java.util.Map;
import java.util.Arrays; 

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> d = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int diff = target - nums[i];
            if (d.containsKey(diff)) {
                return new int[] {d.get(diff), i};
            }
        d.put(nums[i], i);
        }
    return new int[] {};
    }
}

class TwoSum {
    public static void main(String[] args){
        Solution s = new Solution();
        int[] nums = {2, 7, 11, 15};
        int target = 9;
        int[] res = s.twoSum(nums, target);
        System.out.println(Arrays.toString(res));
    }

}


