class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> seen = new HashSet<>();

        for (int i: nums){
            if (!seen.add(i)) return true;
        }

        return false;
    }
}