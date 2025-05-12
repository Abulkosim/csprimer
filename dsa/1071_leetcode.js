function gcdOfStrings(str1, str2) {
    if (str1 + str2 !== str2 + str1) {
        return "";
    }
    var l1 = str1.length;
    var l2 = str2.length;
    while (l2 != 0) {
        var temp = l2;
        l2 = l1 % temp;
        l1 = temp;
    }
    return str1.slice(0, l1);
}
;
console.log(gcdOfStrings("ABCABC", "ABC")); // Expected: "ABC"
console.log(gcdOfStrings("ABABAB", "ABAB")); // Expected: "AB"
console.log(gcdOfStrings("LEET", "CODE")); // Expected: ""
