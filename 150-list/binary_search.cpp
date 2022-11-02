#include <iostream>
#include <vector>

class Solution {
public:
    int search(std::vector<int>& nums, int target) {
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

int main() {
    std::vector<int> ints = {10, 20, 30, 40, 50};
    Solution obj;
    std::cout << "Solution is\n";
    std::cout << obj.search(ints,20);
    std::cout << "\n\n";
};
