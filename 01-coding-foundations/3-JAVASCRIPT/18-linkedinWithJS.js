// FOLLOW ALL THE HASHTAGS
// right click on follow and inspect it. The button has a class, so we can pick it
let hashtagBtns = document.querySelectorAll('.mn-discovery-hashtag-card__action-btn');
// now we have all the buttons in an array
hashtagBtns.forEach(btn => btn.click()); // sends a follow to all those hashtags

// UNFOLLOW ALL THE ONES WE HAVE FOLLOWED
// take the "Following" button, inspect it and take its class
let followingBtns = document.querySelectorAll('.follows-recommendation-card__follow-btn');
followingBtns.forEach(followbtn => followbtn.click()); // now every followed ones are not followed anymore