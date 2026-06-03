class Solution {
    public int[][] kClosest(int[][] points, int k) {

        // Idea:
        // Add all to minHeap based of Euclidean Dist -- O(n) heapify
        // Poll() excatly k times, add to an array
        // Return arraylist


        int[][] polled = new int[k][2];  // To hold first k points
        PriorityQueue<Double[]> minHeap = new PriorityQueue<>(
            new Comparator<Double[]>(){
                public int compare (Double[] a, Double[] b){
                    return Double.compare(a[2], b[2]);
                }
            }
        );

        for (int[] pt: points){
            double x = (double) pt[0];
            double y = (double) pt[1];
            double distance = Math.sqrt(x*x + y*y);

            Double[] newpoint = {x, y, distance};
            minHeap.add(newpoint);
        }

        for (int i=0; i<k; i++){
            Double[] point = minHeap.poll();
            int[] res = new int[2];
            res[0] = point[0].intValue();
            res[1] = point[1].intValue();
            polled[i] = res;

        }

        return polled;
    }
}
