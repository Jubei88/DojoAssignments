var glazedDonuts = [
  {
    frosting: 'glazed',
    style: 'cake',
    type: 'old fashioned',
    age: '45',
    time: 'minutes'
  },
  {
    frosting: 'glazed',
    style: 'yeast raised',
    type: 'regular',
    age: '5',
    time: 'minutes'
  },
  {
    frosting: 'glazed',
    style: 'yeast raised',
    type: 'jelly filled',
    age: '1',
    time: 'seconds'
  }
];


var numPurchase = 0;
for (var donut in glazedDonuts) {
  if((glazedDonuts[0].age < 25 || glazedDonuts[0].time == 'minutes') && glazedDonuts[0].time == 'seconds'){
    numPurchase++;
  }
  else {
    console.log('not this donut...');
  }
}
console.log(numPurchase);


// var purchase;
// if((glazedDonuts[1].age < 25 && glazedDonuts[1].time == 'minutes') || glazedDonuts[1].time == 'seconds'){
//   purchase = glazedDonuts[1];
//   console.log(purchase);
// }
// else {
//   console.log('sorry it has been out a bit longer');
// }