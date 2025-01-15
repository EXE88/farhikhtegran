import { initializeNavbar } from './top-navbar.js';
import { initializeClassPopup, initializeHomeworks, ShowProfileDropdownDatas, loginNeed, loginProccess } from './module-scripts.js';

document.addEventListener('DOMContentLoaded', async () => {
  // Initialize navbar
  initializeNavbar();

  if (await loginNeed()) {
    loginProccess();
  } 
  else {
    const accessToken = localStorage.getItem("accessToken");
    const requestHeaders = new Headers();
    requestHeaders.append("Authorization", "Bearer " + String(accessToken));
  
    const requestOptions = {
        method: "GET",
        headers: requestHeaders,
        redirect: "follow"
    };
  
    async function getGlobalData(){
      const response = await fetch("http://127.0.0.1:8000/users/getuserinfo/", requestOptions);
      const data = await response.json();
      return data;
    }

    const global_data = await getGlobalData();
    ShowProfileDropdownDatas(global_data);
    if (global_data.is_teacher === true) {
      initializeClassPopup();
    }
    else {
      initializeHomeworks();
    }
  }
  
  // Bottom navigation functionality
  const navItems = document.querySelectorAll('.nav-item');
  const bottomNav = document.querySelector('.bottom-nav');
  
  // Create and append the indicator
  const indicator = document.createElement('div');
  indicator.className = 'nav-indicator';
  bottomNav.appendChild(indicator);
  
  // Set initial position
  const initialPage = window.location.hash.slice(1) || 'home';
  const initialTab = document.querySelector(`[data-page="${initialPage}"]`);
  if (initialTab) {
    initialTab.classList.add('active');
    document.getElementById(initialPage).classList.add('active');
  }
  
  navItems.forEach(item => {
    item.addEventListener('click', (e) => {
      e.preventDefault();
      
      // Remove active class from all nav items and pages
      navItems.forEach(nav => nav.classList.remove('active'));
      document.querySelectorAll('.page').forEach(page => page.classList.remove('active'));
      
      // Add active class to clicked nav item and corresponding page
      item.classList.add('active');
      const pageId = item.getAttribute('data-page');
      document.getElementById(pageId).classList.add('active');
    });
  });
});