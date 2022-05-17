function getNameUserONeachVisit() {
        
    var nameOfUserInEachVisitInLclStorage;

    
    var nameOfUserInEachVisitInLclStorage = localStorage.getItem("nameOfUserInEachVisitInLclStorage");


    if (!nameOfUserInEachVisitInLclStorage) {
    
      nameOfUserInEachVisitInLclStorage = prompt("What is your name?: ");

      
      localStorage.setItem("nameOfUserInEachVisitInLclStorage", nameOfUserInEachVisitInLclStorage);
    }

    return nameOfUserInEachVisitInLclStorage;
  }

  var welcome;

  var date = new Date();
  var hour = date.getHours();
  var minute = date.getMinutes();
  var second = date.getSeconds();

  if (minute < 10) {
    minute = "0" + minute;
  }

  if (second < 10) {
    second = "0" + second;
  }

  if (hour < 12) {

    welcome = "Good morning " + getNameUserONeachVisit();
  } else if (hour < 17) {
    welcome = " Good afternoon " + getNameUserONeachVisit();
  } else {
    welcome = "Good evening " + getNameUserONeachVisit();
  }

  document.write("<h2>" + "<font color='red'>" + welcome + "<br></font>" + " " + "Welcome To JAMDO  ATmLocators");
  document.write("<br>" + "The time is" + " " + hour + ":" + minute + ":" + second);

  window.onbeforeunload = () => {
    localStorage.removeItem('nameOfUserInEachVisitInLclStorage');
  }
  
  function geoFindMe() {

    const status = document.querySelector('#status');
    const mapLink = document.querySelector('#map-link');

    mapLink.href = '';
    mapLink.textContent = '';

    function success(position) {
      const latitude  = position.coords.latitude;
      const longitude = position.coords.longitude;

      status.textContent = '';
      mapLink.href = `https://www.openstreetmap.org/#map=18/${latitude}/${longitude}`;
      mapLink.textContent = `Latitude: ${latitude} °, Longitude: ${longitude} °`;
    }

    function error() {
      status.textContent = 'Unable to retrieve your location';
    }

    if(!navigator.geolocation) {
      status.textContent = 'Geolocation is not supported by your browser';
    } else {
      status.textContent = 'Locating…';
      navigator.geolocation.getCurrentPosition(success, error);
    }

  }

    document.querySelector('#find-me').addEventListener('click', geoFindMe);  

    