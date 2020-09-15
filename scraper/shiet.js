var counterdiv = document.getElementsByClassName("counterdiv")[0];
var divs = counterdiv.getElementsByTagName("DIV");
var dict = {};
var x;
var current = "";

for (x of divs) {
    if (x["className"].includes("counter-title")) {
	current = String(x.textContent);
	dict[current] = {};
    } else if (x["className"].includes("counter-header") || x["className"].includes("counter-group")) {
	var value = x.getElementsByClassName("counter-number")[0].textContent;
	if (x["className"].includes("double")) {
	    var header = x.getElementsByClassName("counter-item-double")[0].textContent;
	} else {
	    var header = x.getElementsByClassName("counter-item")[0].textContent;
	}
	dict[current][header] = value;
    }
}

return dict;
