class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> record = new HashMap<>();
        for (int i=0; i<s.length(); i++){
            char x = s.charAt(i);
            if (record.containsKey(x)) {
                record.put(x, record.get(x) + 1);
            } else{
                record.put(x, 1);
            }
        }

        for (int j=0; j<t.length(); j++){
            char y = t.charAt(j);
            if (record.containsKey(y)) {
                if (record.get(y)==0) return false;
                record.put(y, record.get(y) - 1);
            } else{
                return false;
            }
        }

        int sum = record.values().stream().mapToInt(Integer::intValue).sum();
        boolean res = (sum == 0) ? true : false;
        return res;

    }
}