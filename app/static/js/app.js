var img = document.createElement("img");
var smile = document.getElementById("smile")

document.querySelector("#atm").addEventListener("click",()=>{
  console.log("yehey")

  let atmstatus = "working"
  img.src = (atmstatus == "working")? "https://cdn.shopify.com/s/files/1/1061/1924/products/16_large.png?v=1571606116" : "https://hotemoji.com/images/emoji/m/1dssedz11rcxjm.png"
  smile.innerHTML += '<img  width="100" height="100" src="'+img. src+'" />';
}) 

Query( document ).ready( function( $ ) {
  //Welcome Message
  //If this is the user's first time on the site, make a json call
  //and insert a welcome message above the QA menu
  if ( $.cookie( welcome_message.cookie ) == null ) {
    $( welcome_message.prepend ).prepend( '<div id="' + welcome_message.div + '">' + welcome_message.message + '</div>' );
    $( '#' + welcome_message.div ).fadeIn('slow');
    $.cookie( welcome_message.cookie, '1', { expires: parseInt( welcome_message.expiration ), path: '/', domain: welcome_message.domain } );
  }
});
  