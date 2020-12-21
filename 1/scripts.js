function Shiphron()
{
	var alph = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz";
	var z = document.getElementById("teext").value;
	var klch = document.getElementById("klch").value;
	klch++;
	klch--;
	var i = 0;
	var y = "";
	var n = 0;
	while(i<z.length && n<26){
		if(z[i]==alph[n]){
			y+=alph[n+klch];
			i++;
			n = 0;
		}else{
			n++;
		}
	}
	alert(y);
}
function Shiphroff()
{
	var alph1 = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz";
	var z1 = document.getElementById("teext").value;
	var klch = document.getElementById("klch").value;
	var i1 = 0;
	var y1 = "";
	var n1 = 26;
	klch++;
	klch--;
	while(i1<z1.length && n1<53){
		if(z1[i1]==alph1[n1]){
			y1+=alph1[n1-klch];
			i1++;
			n1 = 26;
		}else{
			n1++;
		}
	}
	alert(y1);
}