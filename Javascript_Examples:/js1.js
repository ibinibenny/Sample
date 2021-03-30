function required()
{
var empt = document.form1.text1.value;
if (empt === "")
{
alert("Please enter the Value");
return false;
}
else 
{
alert("code successfully accepted");
return true; 
}
}