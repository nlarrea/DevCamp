// TAKE ELEMENTS FROM THE HTML DOCUMENT
document.getElementsByClassName('b1'); // this would take all of the class="b1" elements
document.getElementsByClassName('b1')[0]; // this would take only the first match or element with that class

// CHANGE THE VALUE OF SOMETHING
document.getElementsByClassName('b1')[0].innerHTML = "Hi there";
// this changes the "Some text" of the HTML document and now we see "Hi there" instead