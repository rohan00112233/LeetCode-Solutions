class Solution {
    public int firstUniqChar(String s) {
        HashMap<Character,Integer> freq = new HashMap<>();
        for(char ch : s.toCharArray()){
            if(!freq.containsKey(ch)){
                // freq[ch] =1;
                freq.put(ch,1);
            }
            else{
                freq.put(ch,freq.get(ch)+ 1);
            }
        
        }
        for(int i =0; i<s.length();i++){
            if(freq.get(s.charAt(i))==1){
                return i;
            }
        }
        return -1;
        }
        
    
}