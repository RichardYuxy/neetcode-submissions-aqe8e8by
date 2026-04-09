class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> count;
        vector<vector<int>> sameFreq(nums.size() +1);

        for(int num : nums){
            count[num]++;
        }
        for(const auto& ele : count){
            sameFreq[ele.second].push_back(ele.first);
        }

        vector<int> result;
        for(int i = sameFreq.size() - 1; i > 0; i--){
            for(int n : sameFreq[i]){
                result.push_back(n);
                            if(result.size() == k){
                return result;
                }
            }
        }
        return result;
    }
};
