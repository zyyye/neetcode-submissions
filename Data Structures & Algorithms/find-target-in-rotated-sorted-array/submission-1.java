class Solution {
    public int search(int[] nums, int target) {
        int l = 0;
        int r = nums.length-1;
        int mid = Math.min((int) r/2 + 1, r);

        while (l<=r) {
            if (nums[l]==target){
                return l;
            } else if (nums[r]==target){
                return r;
            } else if (nums[mid]==target){
                return mid;
            } else if (nums[l]<nums[mid]){
                if (nums[l]<target && target<nums[mid]){
                    r = mid - 1;
                } else l = mid + 1;
            } else {
                if (nums[mid]<target && target<nums[r]){
                    l = mid + 1;
                } else r = mid - 1;
            }
            mid = (int) (r+l)/2;
        }
        return -1;
    }
}
