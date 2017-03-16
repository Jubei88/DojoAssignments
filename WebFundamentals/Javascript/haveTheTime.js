// If minutes less than 30, "just after" the hour, more than 30, "almost" the next hour
// AM / PM, "in the morning", "in the evening",

// Bonus (Only If You Have Time):
// Add functionality for "quarter after", "half past", "5 after" ...
// Distinguish between "in the afternoon", "at night", "noon", "midnight" ...


// I will look to add to this as well to get more out of it

function myTime( hour, minute, period ) {
	if ( period == "AM" ) {
		period = "morning";
	} else {
		period = "afternoon";
	}

	if ( minute >= 00 && minute < 15 ) {
				console.log("It is " + minute + "s past " + hour + " in the " + period);
		} else if ( minute == 15 ) {
				console.log("It is qurter after " + hour + " in the " + period);
		} else if ( minute >= 16 && minute < 30 ) {
				console.log("It is " + minute + "s past " + hour + " in the " + period);
		} else if ( minute == 30 ) {
				console.log("It is half past " + hour + " in the " + period);
		} else if ( minute >= 31 && minute < 44 ) {
				console.log("It is " + minute + "s past " + hour + " in the " + period);
		} else if ( minute == 45 ) {
				console.log("It is quarter till " + hour + " in the " + period);
		} else if ( minute >= 46 && minute < 60 ) {
				minute = 60 - minute;
				console.log("It is " + minute + "s until " + hour + " in the " + period);
		}


}


