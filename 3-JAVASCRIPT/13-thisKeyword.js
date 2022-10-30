// 'this' IS VERY USED IN OBJECTS

var guide = {
	title: "Guide to programming",
	content: "Content will go here",
	visibleToUser: function(viewingUserRole){
		if(viewingUserRole === 'paid'){
			return true;
		} else{
			return false;
		}
	},
	renderContent: function(userRole){
		/* he have to use 'this' here because program needs to know the exact instance we're refering to.
		If we don't use it, the program will check through the global name space and check if there is a 'visibleToUser'
		function and if not, there's gonna return us an undefined. But with 'this', it knows we're refering to this
		object's visibleToUser method */
		if(this.visibleToUser(userRole)){ // we can call methods
			console.log(this.title + " - " + this.content); // we can call attributes
		} else{
			this.content = ''; // we can change the values of the attributes
			console.log(this.title + " - " + this.content);
		}
	}
}
user = {role: 'paid'};
guide.renderContent(user.role); // prints: Guide to programming - Content will go here
userTwo = {role: 'free'};
guide.renderContent(userTwo.role); // prints: Guide to programming - 