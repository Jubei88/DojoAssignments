
// How much was the reward after 30 days?
// remember, a penny isn't 1, but 0.01

// Bonus (Only If You Have Time):

// How many days would it take the servant to make $10,000?
// How about 1 billion?
// In JavaScript, there is a value Infinity, how many days until the servant has infinite money?

// Here we can see how much $ in X days

var gift = .01;

function giftValue(days) {
	for ( var days = 30; days >= 0; days-- ) {
		gift = gift * 2;
		console.log("$" + gift);
	}
}

// Here we switch it to see how many days to reach - or exceed our goal $$

function giftTotal(amt) {
	for ( var i = 1; i >= 0; i++ ) {
		gift = gift * 2;
		if ( gift >= amt ) {
			console.log("You have reached " + "$" + gift + " in " + i + " days");
			break
		}

		console.log( "so far you have " + "$" + gift);
	}
}


// For infinite - I will come back with spare timne on this.  So far not wortking out for me, but it should be infinite days
// var gift = .01;
// for ( var i = 1; i >= 0; i++ ) {
// 		gift = gift * 2;
// 		if ( gift >= infinite ) {
// 			console.log("You have reached " + "$" + gift + " in " + i + " days");
// 			break
// 		}

// 		console.log( "so far you have " + "$" + gift);
// 	}


