// Source - https://stackoverflow.com/a/23994824
// Posted by Ullas, modified by community. See post 'Timeline' for change history
// Retrieved 2026-05-29, License - CC BY-SA 3.0

window.addEventListener('DOMContentLoaded', function() {
  function updateTime() {
    var today = new Date();
    var hour = String(today.getHours()).padStart(2, '0');
    var minutes = String(today.getMinutes()).padStart(2, '0');
    document.getElementById('time').textContent = hour + ':' + minutes;
  }

  updateTime();
  setInterval(updateTime, 1000);
});