

// If it's more than 30 days, print a sad message.

// If it's less than 30 days, print a message sound excited!

// If it's less than 5 days, SCREAM IT!

// ONCE IT'S YOUR BIRTHDAY HAVE PARTY!


var daysUntilMyBirthday = 60;

for (var daysUntilMyBirthday = 60; daysUntilMyBirthday >=0; daysUntilMyBirthday--) {
	if ( daysUntilMyBirthday >= 30 ) {
		console.log(daysUntilMyBirthday + " days until my birthday. Such a long time... :(");
	} else if ( daysUntilMyBirthday > 5 && daysUntilMyBirthday < 30 ) {
		console.log(daysUntilMyBirthday + " days left until my birthday!");
	} else if ( daysUntilMyBirthday > 0 && daysUntilMyBirthday <= 5 ) {
		console.log(daysUntilMyBirthday + " DAYS UNTIL MY BIRTHDAY!!!");
	} else {
		console.log("♪ღ♪*•.¸¸¸.•*¨¨*•.¸¸¸.•*•♪ღ♪¸.•*¨¨*•.¸¸¸.•*•♪ღ♪•*\n♪ღ♪░H░A░P░P░Y░ B░I░R░T░H░D░A░Y░░♪ღ♪\n*•♪ღ♪*•.¸¸¸.•*¨¨*•.¸¸¸.•*•♪¸.•*¨¨*•.¸¸¸.•*•♪ღ♪•«");
	}
}