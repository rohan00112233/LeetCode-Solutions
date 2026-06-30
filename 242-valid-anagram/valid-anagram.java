class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length()!=t.length()){
            return false;
        }
        HashMap<Character, Integer> freq = new HashMap<>();

        for(char ch : s.toCharArray()){
            if(!freq.containsKey(ch)){
                freq.put(ch,1);
            }
            else{
                freq.put(ch, freq.get(ch) + 1);

            }
        }

        for(char ch : t.toCharArray()){
            if(!freq.containsKey(ch)){
                return false;
            }
            else{
                freq.put(ch, freq.get(ch) - 1);
            }
        }

        for (int value : freq.values()){
            if(value!=0){
                return false;
            }
        }
        return true;
    }
}