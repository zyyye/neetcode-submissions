class Solution {
    public int findKthLargest(int[] nums, int k) {
        List<Integer> arr = Arrays.stream(nums)
                                    .boxed()
                                    .toList();

        PriorityQueue<Integer> maxHeap = new PriorityQueue<>((a,b) -> b-a);
        maxHeap.addAll(arr);

        int res = -1;
        for (int i=0; i<k; i++){
            res = maxHeap.poll();
        }

        return res;
    }
}
