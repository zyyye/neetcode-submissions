class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashMap<Integer, Integer> recordMap = new HashMap<>();

        for (int i: nums){
            if (recordMap.containsKey(i)) return true;
            else recordMap.put(i, 1);
        }

        return false;
    }
}