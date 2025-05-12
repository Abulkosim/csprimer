function rob(nums) {
    const memo = {};

    function robFrom(i) {
        if (i >= nums.length) {
            return 0;
        }

        if (i in memo) {
            return memo[i]; 
        }

        const skip = robFrom(i + 1); 
        const robCurrent = nums[i] + robFrom(i + 2);
        memo[i] = Math.max(skip, robCurrent);

        return memo[i];
    }

    return robFrom(0)
}

console.log(rob([1,2,3,1]));