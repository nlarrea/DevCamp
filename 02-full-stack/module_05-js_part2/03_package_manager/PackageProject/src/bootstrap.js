// ES6 code goes here
import moment from 'moment';    // importamos moment desde node_modules

// date object
/*
const rightNow = moment();
console.log(rightNow);
*/

// custom date object
/*
const birthday = moment('1998-06-29', 'YYYY-MM-DD');
console.log(birthday.format('dddd'));   // Monday
console.log(birthday.fromNow());        // 25 years ago
console.log(birthday.format('MMM Do YYYY'));    // Jun 29th 1998

const randomDate = moment('2023-02-26');
console.log(randomDate.fromNow());        // 9 days ago
*/

// calculations
const twoWeeksFromNow = moment().add(14, 'days');
// const twoWeeksFromNow = moment().add(2, 'weeks'); -> sería lo mismo
console.log(twoWeeksFromNow.toString());    // Mon Mar 20 2023 15:12:52 GMT+0100

const sixMonthAgo = moment().subtract(6, 'months');
console.log(sixMonthAgo.toString());        // Tue Sep 06 2022 15:12:52 GMT+0100