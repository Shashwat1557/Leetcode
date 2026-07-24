class Solution {
public:
    int uniqueXorTriplets(vector<int>& nums) {
        int mx = (*max_element(nums.begin(), nums.end())) << 1;

        vector<bool> pair(mx, false);
        for (int a : nums)
            for (int b : nums)
                pair[a ^ b] = true;

        vector<bool> ans(mx, false);
        for (int x = 0; x < mx; x++) {
            if (!pair[x]) continue;
            for (int c : nums)
                ans[x ^ c] = true;
        }

        return count(ans.begin(), ans.end(), true);
    }
};