exports.palindrome = function(word) {
    alphabet="abcdefghijklmnopqrstuvwxyz"
    numbers="1234567890"
    alphanumeric=[]
    for (let char in word.toString()) {
        if (alphabet.includes(char) || numbers.includes(char)) {
            alphanumeric.push(char)
        }
    }
    return alphanumeric===alphanumeric.reverse()
};
