/*
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.
*/

class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int length = digits.size();
        if (length == 0) {
            return digits;
        }
        int carry = 0, idx = length - 1;
        while (idx >= 0) {
            if (idx == length - 1) {
                int current = digits[idx] + 1;
                carry = current / 10;
                digits[idx] = current % 10; 
            }
            else {
                int current = digits[idx] + carry;
                carry = current / 10;
                digits[idx] = current % 10;
            }
            if (carry == 0) {
                return digits;
            }
            idx --;
        }
        if (carry > 0) {
            digits.insert(digits.begin(), carry);
        }
        return digits;
    }
};
