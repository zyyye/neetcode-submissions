public class KthLargest {

    // Sort Original Array, then split to 2 parts
    // Min heap for first k sorted values
    // Remaining are not required for this scenario
    // This way, we can easily peek "k-th" largest item in O(1)

    private final PriorityQueue<Integer> firstKth = new PriorityQueue<>(); // min heap
    private int heapSize = 0;
    private int K;

    public KthLargest(int k, int[] nums) {
        K = k;

        for (int i: nums) {
            firstKth.add(i);  // Add all item to heap
            heapSize++;
        }

        while (heapSize>k){
            firstKth.poll();  // Remove non top k, leaving k largest behind
            heapSize--;
        }
    }
    
    public int add(int val) {
        int benchmark = (firstKth.peek()!=null) ? firstKth.peek() : -999999;

        if (val > benchmark){
            firstKth.add(val);
            heapSize++;
        }

        if (heapSize>K) {
            firstKth.poll();
            heapSize--;
        }
        
        benchmark = firstKth.peek();
        return benchmark;
    }
}
