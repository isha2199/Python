
const user = {
	name: "Isha",
	greet() {
		setTimeout(() => {
			console.log(this.name);
		}, 100);
	}
}
user.greet();
