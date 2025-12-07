class Solution {
    public int numOfSubarrays(int[] arr) {
        final int MOD = 1_000_000_007;
        
        // Track count of prefix sums with even and odd parity
        int evenCount = 1;  // Empty prefix has sum 0 (even)
        int oddCount = 0;
        
        int prefixSum = 0;
        long result = 0;
        
        for (int num : arr) {
            prefixSum += num;
            
            // Check if current prefix sum is odd or even
            if (prefixSum % 2 == 1) {
                // Current prefix is odd
                // To get odd subarray sum: odd - even = odd
                result = (result + evenCount) % MOD;
                oddCount++;
            } else {
                // Current prefix is even
                // To get odd subarray sum: even - odd = odd
                result = (result + oddCount) % MOD;
                evenCount++;
            }
        }
        
        return (int) result;
    }
}