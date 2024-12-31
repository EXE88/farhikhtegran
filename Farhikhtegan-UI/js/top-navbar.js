export function initializeNavbar() {
  const profileButton = document.querySelector('.profile-button');
  const dropdownContent = document.querySelector('.dropdown-content');
  const dropdownItems = document.querySelectorAll('.dropdown-item[data-page]');

  profileButton.addEventListener('click', (e) => {
    e.stopPropagation();
    dropdownContent.classList.toggle('show');
  });

  // Handle dropdown item clicks
  dropdownItems.forEach(item => {
    item.addEventListener('click', (e) => {
      e.preventDefault();
      const pageId = item.getAttribute('data-page');
      // Find and click the corresponding nav item
      document.querySelector(`.bottom-nav .nav-item[data-page="${pageId}"]`).click();
      // Close the dropdown
      dropdownContent.classList.remove('show');
    });
  });

  // Close dropdown when clicking outside
  document.addEventListener('click', (e) => {
    if (!dropdownContent.contains(e.target) && !profileButton.contains(e.target)) {
      dropdownContent.classList.remove('show');
    }
  });
}