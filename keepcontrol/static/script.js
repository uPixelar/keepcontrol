const verificationInput = document.getElementById("verification-code");
const socket = io();

verificationInput.addEventListener("keypress", function (event) {
	if (this.value.length > 7) event.preventDefault();
})

function enterMouseMode() {
	const leftClick = document.getElementById("mouse-click-left");
	const rightClick = document.getElementById("mouse-click-right");
	const touchpad = document.getElementById("mouse-touchpad");

	leftClick.addEventListener("pointerdown", () => {
		socket.emit("mouseClick", {
			action: "press",
			button: "left"
		})
	});

	leftClick.addEventListener("pointerup", () => {
		socket.emit("mouseClick", {
			action: "release",
			button: "left"
		})
	});

	leftClick.addEventListener("touchstart", (event) => {
		event.preventDefault();
	})

	rightClick.addEventListener("pointerdown", () => {
		socket.emit("mouseClick", {
			action: "press",
			button: "right"
		})
	});

	rightClick.addEventListener("pointerup", () => {
		socket.emit("mouseClick", {
			action: "release",
			button: "right"
		})
	})

	rightClick.addEventListener("touchstart", (event) => {
		event.preventDefault();
	})

	const touch = {
		x: 0,
		y: 0,
		index: 0
	}
	
	touchpad.addEventListener("touchstart", (event) => {
		touch.index = event.touches.length-1;
		const mainTouch = event.touches[touch.index];
		touch.x = mainTouch.clientX;
		touch.y = mainTouch.clientY;
	})

	touchpad.addEventListener("touchmove", (event) => {
		event.preventDefault();

		const mainTouch = event.touches[touch.index];
		const deltaX = mainTouch.clientX - touch.x;
		const deltaY = mainTouch.clientY - touch.y;

		touch.x = mainTouch.clientX;
		touch.y = mainTouch.clientY;

		socket.emit("cursorMove", { deltaX, deltaY });
	})

	touchpad.addEventListener("click", (event) => {
		socket.emit("mouseClick", {button: "left", action: "click"})
	})
}

function leaveMouseMode() {

}

enterMouseMode();