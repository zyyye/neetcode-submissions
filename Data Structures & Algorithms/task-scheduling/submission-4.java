class Solution {

    public int leastInterval(char[] tasks, int n) {
        int[] countList = new int[26];
        Arrays.fill(countList, 0);

        for (int i=0; i<tasks.length; i++){
            int index = (int) tasks[i] - 'A';
            countList[index] = countList[index] + 1;
        }
        
        int max = -1;
        int nonZero = 0;
        int maxCount = 0;
        for (int i=0; i<26; i++){
            if (countList[i] > max) max = countList[i];
            if (countList[i] != 0) nonZero++;
        }
        for (int i=0; i<26; i++){
            if (countList[i] == max) maxCount++;
        }

        //int size = (nonZero-1<=n)? n+1:nonZero;
        int res = (n+1)*(max-1) + maxCount;
        res = Math.max(res, tasks.length);

        return res;
    }
}
