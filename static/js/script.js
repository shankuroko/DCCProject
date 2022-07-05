function replaceSuggestion(suggs) {
	document.getElementById("out").innerHTML = "";
	for (let i = 0; i < suggs.length; i++) {
		let item = document.createElement("li");
		item.className = "suggestion-item";
		item.innerText = suggs[i];
		item.onclick = () => {
			document.getElementById("input").value += " " + suggs[i];
		};
		document.getElementById("out").appendChild(item);
	}
}
var input = document.getElementById("input");
input.addEventListener("keypress", function (event) {
	if (event.key === " ") {
		value = document.getElementById("input").value;
		lastSentence = value.split(".");
		sen = lastSentence.length > 1 ? lastSentence.slice(-1) : lastSentence[0];
		console.log(sen);
		inVal = sen.split(" ");
		console.log(inVal);
		inVal = inVal.length > 3 ? inVal.slice(-3).join(" ") : inVal.join(" ");
		console.log(inVal);
		$.ajax({
			type: "GET",
			url: "/getSuggestionList",
			timeout: 15000,
			data: {
				val: inVal,
			},
			success: (jq) => {
				j = JSON.parse(jq.replace(/&#39;/g, '"'));
				replaceSuggestion(j);
			},
		});
	}
});
function getSuggestions() {
	value = document.getElementById("input").value;
	$.ajax({
		type: "GET",
		url: "/getSuggestionList",
		timeout: 15000,
		data: {
			val: value,
		},
		success: (jq) => {
			j = JSON.parse(jq.replace(/&#39;/g, '"'));
			replaceSuggestion(j);
		},
	});
}
