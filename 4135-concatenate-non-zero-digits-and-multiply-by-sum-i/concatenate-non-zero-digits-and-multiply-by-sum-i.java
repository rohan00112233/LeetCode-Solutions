class Solution {
    // ans = 0
    //     sum = 0
    //     n1 = []
    //     n = str(n)
    //     for i in range(len(n)):
    //         if n[i] != '0':
    //             n1.append(n[i])
    //     if not n1:
    //         return 0   
    //     digitsum = 0

    //     for digit in n1:
    //         digitsum += int(digit)
        
    //     x = "".join(n1)
    //     x = int(x)

    //     return x * digitsum
    public long sumAndMultiply(int n) {
        String str = String.valueOf(n);
        StringBuilder sb = new StringBuilder();
        for(int i =0; i<str.length();i++){
            char ch = str.charAt(i);
            if (ch != '0'){
                sb.append(ch);
            }

        }
        if(sb.length() == 0){
            return 0;
        }
        long digitsum =0;
        for(int i =0;i<sb.length();i++){
            digitsum += sb.charAt(i)-'0';
        }
        long x = Integer.parseInt(sb.toString());
        return x * digitsum;
        
    }
}