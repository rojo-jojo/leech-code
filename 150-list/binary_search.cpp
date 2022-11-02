#include <iostream>
#include <vector>

class Solution {
public:
    int search(vector<int>& nums, int target) {
        int n = nums.size();
        int beg = 0;
        int end = n;
        int mid;
        for (int i=0; i<n; i++) {
            mid = (int)(beg + end)/2;
            if (nums[mid] == target) {
                return mid;
            }
            else if (nums[mid] > target) {
                end = mid - 1;

            }
            else if (nums[mid] < target) {
                beg = mid + 1;
            }
        }
        return -1;
    }

};
