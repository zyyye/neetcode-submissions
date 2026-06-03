class Solution {
    public int lastStoneWeight(int[] stones) {
        List<Integer> list = Arrays.stream(stones)
                                .boxed()
                                .toList();

        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(
                                                list.size(),
                                                Collections.reverseOrder());
        maxHeap.addAll(list);

        int count = list.size();
        while (count>1){
            int x = maxHeap.poll();
            int y = maxHeap.poll();

            if (x!=y) {
                maxHeap.add(Math.abs(x-y));
                count--;
            } else {
                count-=2;
            }
        }

        int leftover = (count==1)? maxHeap.poll() : 0;
        return leftover;
    }
}
