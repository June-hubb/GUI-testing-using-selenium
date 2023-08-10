$(function() {
    // get the "stay signed in" checkbox
    var staySignedInCheckbox = $('#staySignedIn');
  
    // check if the user has previously selected "stay signed in"
    var savedUsername = localStorage.getItem('username');
    var savedPassword = localStorage.getItem('password');
    var savedStaySignedIn = localStorage.getItem('staySignedIn');
  
    // if "stay signed in" was previously selected, pre-fill the username and password fields
    if (savedStaySignedIn === 'true') {
      $('#username').val(savedUsername);
      $('#password').val(savedPassword);
      staySignedInCheckbox.prop('checked', true);
    }
  
    // handle form submission
    $('#loginForm').on('submit', function(event) {
      event.preventDefault(); // prevent form submission
  
      // get username and password from form input fields
      var username = $('#username').val();
      var password = $('#password').val();
  
      // check if username and password match the hardcoded values
      if (username === 'Junaita' && password === 'library123') {
        window.location.href = "personal.html";
  
        // save username and password to local storage if "stay signed in" is checked
        if (staySignedInCheckbox.is(':checked')) {
          localStorage.setItem('username', username);
          localStorage.setItem('password', password);
          localStorage.setItem('staySignedIn', true);
        } else {
          localStorage.removeItem('username');
          localStorage.removeItem('password');
          localStorage.removeItem('staySignedIn');
        }
  
        // do something else after successful login
      } else {
        alert('Invalid username or password.');
        // do something else after failed login attempt
      }
    });
  });
  