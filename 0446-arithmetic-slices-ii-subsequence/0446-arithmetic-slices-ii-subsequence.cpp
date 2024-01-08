class Solution {
public:
    int numberOfArithmeticSlices(vector<int>& nums) {
        vector<map<long long, long long>> d(nums.size());
        long long c = 0;
        for(int i = 1; i < nums.size(); i++){
            for(int j = 0; j < i; j++){
                long long v = (long long)nums[i] - nums[j];
                d[i][v] = d[i][v]+d[j][v]+1;
                c += d[j][v];
            }
        }
        return c;
    }
};