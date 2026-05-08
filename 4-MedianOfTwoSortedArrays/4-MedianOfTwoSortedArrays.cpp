// Last updated: 5/8/2026, 4:24:01 PM
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {

        vector<int> v;
        for(auto num:nums1){
            v.push_back(num);
        }
        for(auto num:nums2){
            v.push_back(num);
        }

        sort(v.begin(),v.end());
        int n = v.size();
        double med = 0.0;

        if(n%2 !=0){
            med = v[n/2];
        }
        else{
            med = (v[n/2-1] + v[n/2])/2.0;
        }

        return med;
    }
};