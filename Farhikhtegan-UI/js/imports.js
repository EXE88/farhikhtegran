//top navbar import
fetch('../html/top-navbar.html')
.then(response => response.text())
.then(data => {
  document.getElementById('top-navbar-div').innerHTML = data;
})
.catch(error => console.error('Error loading HTML:',error));

//tabs content import

//home
fetch('../html/home-tab.html')
.then(response => response.text())
.then(data => {
    document.getElementById('tabs-content').insertAdjacentHTML("beforeend",data)
})
.catch(error => console.error('Error loading HTML:',error));

//profile
fetch('../html/profile-tab.html')
.then(response => response.text())
.then(data => {
    document.getElementById('tabs-content').insertAdjacentHTML("beforeend",data)
})
.catch(error => console.error('Error loading HTML:',error));

//scores
fetch('../html/scores-tab.html')
.then(response => response.text())
.then(data => {
    document.getElementById('tabs-content').insertAdjacentHTML("beforeend",data)
})
.catch(error => console.error('Error loading HTML:',error));

//messages
fetch('../html/messages-tab.html')
.then(response => response.text())
.then(data => {
    document.getElementById('tabs-content').insertAdjacentHTML("beforeend",data)
})
.catch(error => console.error('Error loading HTML:',error));

//homeworks
fetch('../html/homeworks-tab.html')
.then(response => response.text())
.then(data => {
    document.getElementById('tabs-content').insertAdjacentHTML("beforeend",data)
})
.catch(error => console.error('Error loading HTML:',error));

//attendance
fetch('../html/attendance-tab.html')
.then(response => response.text())
.then(data => {
    document.getElementById('tabs-content').insertAdjacentHTML("beforeend",data)
})
.catch(error => console.error('Error loading HTML:',error));

//bottom navbar import
fetch('../html/bottom-navbar.html')
.then(response => response.text())
.then(data => {
  document.getElementById('bottom-navbar-div').innerHTML = data;
})
.catch(error => console.error('Error loading HTML:',error));