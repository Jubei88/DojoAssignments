// Fancy Array
// Normally, if you print an array such as ["James", "Jill", "Jane", "Jack"], you will see the following:

// [ "James", "Jill", "Jane", "Jack" ]
// Let's make it look fancy! Write a function that will make it print like:

// 0 -> James
// 1 -> Jill
// 2 -> Jane
// 3 -> Jack
// Bonus (Only If You Have Time):

// Let the user pass in the symbol that will print (ex: "->", "=>", "::", "-----")
// Have an extra parameter reversed. If the user passes true, print the elements in reverse order

var names = [ "James", "Jill", "Jane", "Jack" ];
for ( var i = 0; i < names.length ; i++ ) {
	console.log( i + " -> " + names[i]);
}

var names = [ "James", "Jill", "Jane", "Jack" ];
function nameList(seperate) {
	for ( var i = 0; i < names.length ; i++ ) {
		console.log( i + " " + seperate + " " + names[i]);
	}
}

// occurs to me that I am not sure if you want the 0-1-2-3 in reverse order as well, but thinking not

var names = [ "James", "Jill", "Jane", "Jack" ];
function nameList(seperate, tf) {
	if ( tf == true ) {
		names.reverse();
	}
	for ( var i = 0; i < names.length ; i++ ) {
		console.log( i + " " + seperate + " " + names[i]);
	}
}