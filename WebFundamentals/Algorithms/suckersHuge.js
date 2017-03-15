// Add odd integers from -300,000 to 300,000, and console.log the final sum. Is there a shortcut?

var sumTotal = 0;
	for ( var i = -299999; i <= 300000; i = i + 2) {
	sumTotal = sumTotal + i;
	}
	console.log(sumTotal);

// I looked at a couple of other ways - but they weren't any shorter