// If 2 given numbers represent your birth month and day in either order, log "How did you know?", else log "Just another day....",

// Example: given yourBirthday(4,19) or yourBirthday(19,4)

var myBday = 12 + '/' + 25;

function yourBirthday(mm, dd) {
    if (dd < 10) {
        dd = '0' + dd;
    }
    if (mm < 10) {
        mm = '0' + mm;
    }

	var bDay = mm + '/' + dd ;
	var bDayAlt = dd + '/' + mm ;
	// console.log(bDay + "," + bDayAlt);
	if ( myBday === bDay || myBday === bDayAlt ) {
		console.log("How did you know?");
	} else
		console.log("Just another day....");
}