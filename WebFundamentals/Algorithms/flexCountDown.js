// Based on earlier “Countdown By Fours”, given lowNum, highNum, mult, print multiples of mult from highNum down to lowNum, using a FOR loop.

// Example: For (2,9,3), print 9 6 3 (on successive lines).

function countDown(lowNum, highNum, mult) {
	for ( highNum; highNum > lowNum; highNum = highNum - mult ) {
		console.log(highNum);
	}
}

