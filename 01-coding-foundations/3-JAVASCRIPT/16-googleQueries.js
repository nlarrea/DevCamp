/* this is code to use in the Developers tools from Google Chrome */

// TAKE THE SEARCH BAR FROM GOOGLE
//const searchBar = document.querySelector(".gsfi");
// another way to do the same and change its value
$(".gsfi").value = 'JavaScript tips'; // this works on google's developers tool

// TAKE THE SEARCH BUTTON -> it hasn't its own class, so we gotta do it this way
$('.jsb'); // this gives us the entire div -> we need to find the button inside it
$('.jsb').childNodes; // returns a list -> we can see where it is the item we're trying to take
$('.jsb').childNodes[0]; // this gives us all the buttons, but we only want one
$('.jsb').childNodes[0].childNodes; // we can see all the buttons an check which one is the one we want
$('.jsb').childNodes[0].childNodes[0].click(); // the search button will be clicked