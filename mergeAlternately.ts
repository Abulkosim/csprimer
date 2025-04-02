function mergeAlternately(w1: string, w2: string): string {
    const word1 = w1.split(""); 
		const word2 = w2.split(""); 
		let minLength = Math.min(word1.length, word2.length);
    let maxLength = Math.max(word1.length, word2.length);
    let mergedResult: string[] = [];
    
    for (let i = 0; i < maxLength; i++) {
        if (i < minLength) {
            mergedResult.push(word1[i]);
            mergedResult.push(word2[i]);
        } else {
            word1.length > word2.length 
                ? mergedResult.push(word1[i]) 
                : mergedResult.push(word2[i]);
        }
				console.log(mergedResult);
    }

		console.log(mergedResult.join(""));
    return mergedResult.join("");
};

mergeAlternately("dfe", "beebda"); 
