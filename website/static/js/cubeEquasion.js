function calculate() {
    var n = Number.parseInt(document.getElementById("sideNumber").value);
    document.getElementById("ans").innerHTML = (((Math.abs(n + 2) - Math.abs(n - 2)) / 2) * Math.pow(n, 2)) + ((n - ((Math.abs(n + 2) - Math.abs(n - 2)) / 2)) * (Math.pow(n, 2) - Math.pow((n - ((Math.abs(n + 2) - Math.abs(n - 2)) / 2)), 2)));
}