class Solution {
    public class NumberPair implements Comparable<NumberPair>{
        int num;
        int freq;

        NumberPair(int num, int freq){
            this.num = num;
            this.freq = freq;
        }

        @Override 
        public int compareTo(NumberPair other){
            return Integer.compare(this.freq, other.freq);
        }
    }

    public int[] topKFrequent(int[] nums, int k) {
        @SuppressWarnings("unchecked")
        int n = nums.length;
        int[] arr = new int[2001];

        for (int i=0; i<n; i++){
            arr[nums[i] + 1000]++;
        }

        ArrayList<NumberPair>[] buckets = new ArrayList[1000];
        for (int i=0; i<1000; i++){
            buckets[i] = new ArrayList<>();
        }

        for (int i=0; i<2001; i++){
            if (arr[i]!=0){
                NumberPair pair = new NumberPair(i-1000, arr[i]);
                buckets[arr[i]].add(pair);
            }
        }

        for (ArrayList<NumberPair> buck: buckets){
            Collections.sort(buck);
        }

        int[] res = new int[k];
        int resIndex = 0;

        for (int i=999; i>=0 && resIndex<k; i--){
            for (NumberPair pair: buckets[i]){
                res[resIndex++] = pair.num;
                if (resIndex == k) break;
            }
        }

        return res;
    }
}
